"""Lab 13 · Định giá agent và lập kế hoạch pilot (Gate 2a) — bài làm của nhóm (file nộp).
Chạy trong thư mục src/: python3 lab13.py   (cần pandas; Nhiệm vụ D cần thêm statsmodels)
Không cần khoá API. Điền các chỗ ghi VIẾT Ở ĐÂY (đánh dấu TODO CP1…CP4). Dữ liệu trong hai file CSV là giả lập.
Bản gốc chưa sửa nằm ở lab13_starter.py.
"""
import math
import pandas as pd

# Bảng giá GIẢ ĐỊNH của lab (không phải giá thật của nhà cung cấp nào)
GIA_VAO = 26        # đồng cho 1.000 token đầu vào
GIA_RA = 130        # đồng cho 1.000 token đầu ra
GIA_TOOL = 15       # đồng cho 1 lần gọi tool
LUONG_PHUT = 2000   # đồng cho 1 phút của nhân viên (đã gồm bảo hiểm, văn phòng)
BASELINE = 12000    # đồng cho 1 yêu cầu khi nhân viên tự làm (6 phút)


# ---------- Nhiệm vụ A1 · Kinh tế của việc chạy lại ----------
# TODO CP1: viết ba hàm dưới đây cho tới khi kiem_tra_dap_an_biet_truoc() in ĐẠT.
def so_lan_chay_ky_vong(p, k=None):
    """Số lần chạy trung bình cho 1 yêu cầu khi mỗi lần đúng với xác suất p.
    k = số lần chạy tối đa; k=None nghĩa là chạy lại đến khi đúng."""
    return 1 / p if k is None else (1 - (1 - p) ** k) / p


def ti_le_thanh_cong(p, k=None):
    """Xác suất yêu cầu thành công sau tối đa k lần chạy."""
    return 1.0 if k is None else 1 - (1 - p) ** k


def he_so_chi_phi_moi_viec_thanh_cong(p, k=None):
    """Chi phí mỗi việc thành công, tính bằng bội số của giá một lần chạy."""
    return so_lan_chay_ky_vong(p, k) / ti_le_thanh_cong(p, k)


def kiem_tra_dap_an_biet_truoc():
    """Ba phép thử bắt buộc đạt 100% trước khi tính trên dữ liệu."""
    assert abs(so_lan_chay_ky_vong(0.8, 2) - 1.20) < 1e-9, 'p=0,8, tối đa 2 lần → 1,20 lần chạy'
    assert abs(so_lan_chay_ky_vong(0.8) - 1.25) < 1e-9, 'p=0,8, chạy đến khi đúng → 1,25 lần chạy'
    assert abs(he_so_chi_phi_moi_viec_thanh_cong(0.8, 3) - 1.25) < 1e-9, 'p=0,8, tối đa 3 lần → 1,25 lần giá một lần chạy'
    print('Ba phép thử đáp án biết trước: ĐẠT')


# ---------- Nhiệm vụ A2 · Mô hình chi phí từ trace ----------
# TODO CP1: viết mo_hinh; CP2 gọi lại hàm này với tham số giá và hệ số đã đổi.
def mo_hinh(runs, reqs, gia_vao=26, gia_ra=130, gia_tool=15, luong_phut=2000,
            he_so_xem_lai=1.0, he_so_lam_lai=1.0, max_lan_chay=None):
    """Trả về dict gồm: token, tool, xem_lai, lam_lai, tong, thanh_cong, cps (chi phí mỗi việc thành công).
    - token, tool: cộng trên MỌI lần chạy trong runs, kể cả lần lỗi.
    - xem_lai, lam_lai: số phút (cột *_simulated) × LUONG_PHUT. Đây là số GIẢ LẬP, phải ghi nhãn simulated khi báo cáo.
    - thanh_cong: số yêu cầu có ket_qua == 'thanh_cong'.
    - Các tham số giá/hệ số/max_lan_chay dùng cho Nhiệm vụ B (độ nhạy, giới hạn số lần chạy); giữ mặc định ở A2.
    """
    reqs = reqs.copy()
    runs = runs[runs['request_id'].isin(reqs['request_id'])]
    if max_lan_chay is not None:  # dùng cho B1, B3
        runs = runs[runs['attempt'] <= max_lan_chay]
        vuot = reqs['so_lan_chay'] > max_lan_chay
        reqs.loc[vuot, 'ket_qua'] = 'chuyen_nhan_vien'
        reqs.loc[vuot, ['phut_xem_lai_simulated', 'phut_lam_lai_simulated']] = 0
    tien_token = runs['tokens_in'] / 1000 * gia_vao + runs['tokens_out'] / 1000 * gia_ra
    tien_tool = runs['tool_calls'] * gia_tool
    xem_lai = reqs['phut_xem_lai_simulated'].sum() * luong_phut * he_so_xem_lai
    lam_lai = reqs['phut_lam_lai_simulated'].sum() * luong_phut * he_so_lam_lai
    tong = tien_token.sum() + tien_tool.sum() + xem_lai + lam_lai
    thanh_cong = (reqs['ket_qua'] == 'thanh_cong').sum()
    return dict(token=tien_token.sum(), tool=tien_tool.sum(),
                chay_lai=(tien_token + tien_tool)[runs['attempt'] > 1].sum(),
                xem_lai=xem_lai, lam_lai=lam_lai, tong=tong,
                thanh_cong=thanh_cong, cps=tong / thanh_cong,
                hoa_don_moi_yc=(tien_token.sum() + tien_tool.sum()) / len(reqs))


if __name__ == '__main__':
    runs = pd.read_csv('logix_runs.csv')
    reqs = pd.read_csv('logix_requests.csv', keep_default_na=False)
    kiem_tra_dap_an_biet_truoc()
    ket_qua = mo_hinh(runs, reqs)
    for ten, gia_tri in ket_qua.items():
        print(f'{ten:12s} {gia_tri:>14,.0f}')
    # TODO CP1 · Nhiệm vụ A3: tính lại theo từng giá trị của cột loai.
    print('\n--- A3 · Tách theo loại yêu cầu ---')
    cac_loai = ['noi_dia', 'hang_nang', 'quoc_te', 'doi_tac']
    for l in cac_loai:
        sub_reqs = reqs[reqs['loai'] == l]
        sub_runs = runs[runs['request_id'].isin(sub_reqs['request_id'])]
        kq = mo_hinh(runs, sub_reqs)
        so_yc = len(sub_reqs)
        ti_le_tc = kq['thanh_cong'] / so_yc * 100
        lan_chay_tb = len(sub_runs) / so_yc
        cps = kq['cps']
        so_baseline = cps / BASELINE
        print(f'{l:10s} | YC: {so_yc:3d} | TC: {ti_le_tc:5.1f}% | Lần chạy/yc: {lan_chay_tb:4.2f} | CPS: {cps:7,.0f} đ [simulated] | So với 12k: {so_baseline:4.2f}x')

    runs_loai = runs.merge(reqs[['request_id', 'loai']], on='request_id')
    runs_loai['is_ok'] = runs_loai['status'] == 'ok'
    pivot = runs_loai.pivot_table(index='loai', columns='attempt', values='is_ok', aggfunc='mean')
    print('\nTỉ lệ status == ok theo attempt:')
    print((pivot * 100).round(1))

    # Nhiệm vụ A4 · Chi phí cố định (phạm vi noi_dia + hang_nang)
    print('\n--- A4 · Chi phí cố định (noi_dia + hang_nang) ---')
    reqs_pilot = reqs[reqs['loai'].isin(['noi_dia', 'hang_nang'])]
    kq_pilot = mo_hinh(runs, reqs_pilot)
    tc_mau = kq_pilot['thanh_cong']  # 900
    cps_bien_doi = kq_pilot['cps']   # 3.414 đ

    for nhan, yc_thang in [('45.000 yêu cầu/tháng', 45000), ('Một nửa khối lượng', 22500)]:
        tc_thang = yc_thang * (tc_mau / len(reqs))
        cp_co_dinh_moi_viec = 40_000_000 / tc_thang
        cps_tong = cps_bien_doi + cp_co_dinh_moi_viec
        so_baseline = cps_tong / BASELINE
        print(f'{nhan:22s} | Việc TC/tháng: {tc_thang:6,.0f} | Cố định/việc: {cp_co_dinh_moi_viec:5,.0f} đ | CPS + cố định: {cps_tong:5,.0f} đ [simulated] | So với 12k: {so_baseline:4.2f}x')
    # TODO CP2 · Nhiệm vụ B1: đổi từng yếu tố, ghi vào bảng độ nhạy.
    print('\n--- B1 · Bảng độ nhạy (9 kịch bản đổi từng yếu tố) ---')
    kich_ban = {
        'Giá token gấp đôi':        dict(gia_vao=52, gia_ra=260),
        'Giá token giảm một nửa':   dict(gia_vao=13, gia_ra=65),
        'Xem lại gấp đôi':          dict(he_so_xem_lai=2),
        'Xem lại giảm một nửa':     dict(he_so_xem_lai=0.5),
        'Làm lại gấp đôi':          dict(he_so_lam_lai=2),
        'Làm lại giảm một nửa':     dict(he_so_lam_lai=0.5),
        'Lương tăng 25%':           dict(luong_phut=2500),
        'Tối đa 2 lần chạy':        dict(max_lan_chay=2),
        'Chỉ 1 lần chạy':           dict(max_lan_chay=1),
    }
    goc = mo_hinh(runs, reqs)['cps']
    print(f'{"Gốc (A2)":27s} {goc:8,.0f} đ [simulated]')
    for ten, kw in kich_ban.items():
        cps = mo_hinh(runs, reqs, **kw)['cps']
        thay_doi = (cps / goc - 1) * 100
        print(f'{ten:27s} {cps:8,.0f} đ [simulated] {thay_doi:+6.1f}%')

    # Nhiệm vụ B2 · Đổi một cặp và xếp hạng
    print('\n--- B2 · Đổi một cặp và xếp hạng ---')
    cps_cap = mo_hinh(runs, reqs, gia_vao=52, gia_ra=260, he_so_xem_lai=2)['cps']
    thay_doi_cap = (cps_cap / goc - 1) * 100
    print(f'Giá token x2 + Xem lại x2: {cps_cap:8,.0f} đ [simulated] ({thay_doi_cap:+5.1f}%)')

    # Nhiệm vụ B3 · Giới hạn chạy lại có thật sự rẻ hơn
    print('\n--- B3 · Giới hạn chạy lại có thật sự rẻ hơn ---')
    for k in [1, 2, 3]:
        kq_k = mo_hinh(runs, reqs, max_lan_chay=k)
        ktc = len(reqs) - kq_k['thanh_cong']
        ca_he_thong = kq_k['tong'] + ktc * BASELINE
        print(f'Giới hạn {k} lần | Tổng trợ lý: {kq_k["tong"]:9,.0f} đ [simulated] | Không TC: {ktc:3d} | Cả hệ thống: {ca_he_thong:9,.0f} đ [simulated] | CPS: {kq_k["cps"]:5,.0f} đ [simulated]')

    # Nhiệm vụ B4 · Nếu phải xem lại tất cả (noi_dia + hang_nang)
    print('\n--- B4 · Nếu phải xem lại tất cả (noi_dia + hang_nang) ---')
    runs_p = runs[runs['request_id'].isin(reqs_pilot['request_id'])]
    tien_token_p = runs_p['tokens_in'] / 1000 * GIA_VAO + runs_p['tokens_out'] / 1000 * GIA_RA
    tien_tool_p = runs_p['tool_calls'] * GIA_TOOL
    token_tool_p = tien_token_p.sum() + tien_tool_p.sum()
    yc_ok = runs_p[runs_p['status'] == 'ok']['request_id'].nunique()  # 948
    tien_xl_100 = yc_ok * 5 * LUONG_PHUT  # 9.480.000 đ
    ca_ll = (reqs_pilot['ket_qua'] == 'lam_lai').sum()  # 48 ca
    thanh_cong_p = (reqs_pilot['ket_qua'] == 'thanh_cong').sum()  # 900

    # TH1: Làm lại 9 phút/ca
    tong_9m = token_tool_p + tien_xl_100 + ca_ll * 9 * LUONG_PHUT
    cps_9m = tong_9m / thanh_cong_p
    # TH2: Làm lại 15,3 phút/ca
    tong_15m = token_tool_p + tien_xl_100 + ca_ll * 15.3 * LUONG_PHUT
    cps_15m = tong_15m / thanh_cong_p

    print(f'Xem lại 100% (làm lại 9 phút):   CPS = {cps_9m:6,.0f} đ [simulated] ({cps_9m/BASELINE:4.2f}x so với 12k)')
    print(f'Xem lại 100% (làm lại 15.3 phút): CPS = {cps_15m:6,.0f} đ [simulated] ({cps_15m/BASELINE:4.2f}x so với 12k)')
    # TODO CP4 · Nhiệm vụ D: cỡ mẫu.
    #   from statsmodels.stats.proportion import proportion_effectsize
    #   from statsmodels.stats.power import NormalIndPower\n

    # ===== D1_GATE2A_OFFICIAL =====
    # Nhiem vu D1: tinh co mau va so sanh phuong an phan nhom.
    from statistics import NormalDist
    from statsmodels.stats.power import NormalIndPower
    from statsmodels.stats.proportion import proportion_effectsize

    print("\\n--- D1 · Cỡ mẫu và lựa chọn phân nhóm ---")

    def co_mau_hai_ty_le(p1, p2, alpha=0.05, power=0.80):
        z_alpha = NormalDist().inv_cdf(1 - alpha / 2)
        z_power = NormalDist().inv_cdf(power)
        p_bar = (p1 + p2) / 2
        tu_so = (
            z_alpha * math.sqrt(2 * p_bar * (1 - p_bar))
            + z_power * math.sqrt(
                p1 * (1 - p1) + p2 * (1 - p2)
            )
        ) ** 2
        return math.ceil(tu_so / (p2 - p1) ** 2)

    icc = 0.02
    so_nhan_vien_moi_nhom = 20
    so_depot_moi_nhom = 6

    # D1a: phan nhom theo request, MDE 5 diem phan tram.
    n_request = co_mau_hai_ty_le(0.70, 0.75)

    # D1b: phan nhom theo staff, trung binh 75 request/nguoi.
    m_trung_binh = 75
    de_staff_75 = 1 + (m_trung_binh - 1) * icc
    n_staff_75 = math.ceil(n_request * de_staff_75)
    staff_can_moi_nhom = math.ceil(n_staff_75 / m_trung_binh)

    # D1c va D1d: gioi han mau hieu dung theo so cum.
    hieu_dung_staff = so_nhan_vien_moi_nhom / icc
    hieu_dung_depot = so_depot_moi_nhom / icc

    # D1e: MDE 6 diem phan tram, tu 70% len 76%.
    n_6_diem = co_mau_hai_ty_le(0.70, 0.76)
    m_toi_thieu = math.ceil(
        n_6_diem * (1 - icc)
        / (so_nhan_vien_moi_nhom - n_6_diem * icc)
    )
    de_6_diem = 1 + (m_toi_thieu - 1) * icc
    hieu_dung_6_diem = (
        so_nhan_vien_moi_nhom * m_toi_thieu / de_6_diem
    )

    # Kiem tra power neu hieu qua thuc te chi la 5 diem phan tram.
    power_5_diem = NormalIndPower().power(
        proportion_effectsize(0.70, 0.75),
        nobs1=n_6_diem,
        alpha=0.05,
        ratio=1,
        alternative="two-sided"
    )

    print(f"D1a - Request-level: {n_request:,} request/nhom")
    print(
        f"D1b - Staff-level, m=75: {n_staff_75:,} request/nhom; "
        f"{staff_can_moi_nhom} nhan vien/nhom"
    )
    print(f"D1c - 20 staff/nhom: {hieu_dung_staff:,.0f} mau hieu dung")
    print(f"D1d - 6 depot/nhom: {hieu_dung_depot:,.0f} mau hieu dung")
    print(f"D1e - MDE 6 diem phan tram: {n_6_diem:,} request/nhom")
    print(f"D1e - Request toi thieu moi nhan vien: {m_toi_thieu}")
    print(f"D1e - Design effect: {de_6_diem:.2f}")
    print(f"D1e - Effective sample: {hieu_dung_6_diem:.2f}")
    print(f"Power neu MDE chi 5 diem phan tram: {power_5_diem:.4f}")
    # ===== END D1_GATE2A_OFFICIAL =====

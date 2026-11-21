# Team

## Thông tin nhóm

- Tên nhóm: Nhom4Nam
- Lớp: L3A
- Repo nhóm: `K5-L3A-DAY13-Nhom4Nam-LaunchEconomics` (xem [SUBMISSION.md](SUBMISSION.md))
- URL repo, nhánh nộp, commit chốt:  https://github.com/trngtnh/K5-L3A-DAY13-Nhom4Nam-LaunchEconomics.git

## Thành viên

| STT | Họ tên | MSSV | Email | GitHub | Vai trò |
| --: | ------ | ---- | ----- | ------ | ------- |
|   1 | Trần Dương Trung Tính | 2A202603488 | 26ai.tinhtdt@vinuni.edu.vn | trngtnh | Người viết code (Nhiệm vụ A và B, CP1–CP2) |
| 2 | Trần Anh Duy | 2A202603494 | 26ai.duyta@vinuni.edu.vn | duyanhtran2005 | Người gắn nhãn 2, kiêm giữ hồ sơ launch v0 |
| 3 | Nguyễn Nhựt Linh | 2A202603492 | 26ai.linhnn2@vinuni.edu.vn | codenhenhe | Người gắn nhãn 1, phụ trách bảng lỗi CP3 và hoàn thiện báo cáo nhóm sau chấm chéo |
|   4 |        |      |       |        |         |

Bốn vai của lab:

- **Người viết code:** viết và chạy `src/lab13.py`.
- **Người kiểm số:** tính tay một con số để đối chiếu, điền bảng.
- **Người gắn nhãn 1:** đọc đề, theo dõi điều kiện "Xong khi"; gắn nhãn 20 ca độc lập ở CP3.
- **Người gắn nhãn 2, kiêm giữ hồ sơ:** điền `report/team/ho_so_launch_v0.md` từ đầu buổi; gắn nhãn 20 ca độc lập ở CP3.

Đổi người viết code sau giờ giải lao, để ít nhất hai người trong nhóm tự tay tính được chi phí.

## Cá nhân

Mỗi thành viên đồng thời tạo một báo cáo riêng trong `report/` theo dạng:

```text
report/team/MSSV_HoTen.md
```

Ví dụ: `report/team/20241234_NguyenVanAn.md`.

Sao chép mục dưới đây cho từng thành viên.

## Trần Anh Duy — 2A202603494

### Phần việc phụ trách

- CP3: gắn nhãn 20 ca lỗi ở cột người gắn nhãn 2.
- CP5: tính chỉ số, đặc tả event, tổng hợp rủi ro kinh tế và hồ sơ launch v0.

### Đóng góp cụ thể

- Tính và đối chiếu ba chỉ số trên 1.200 yêu cầu.
- Đặc tả 7 event có `trace_id` và tổng hợp hai rủi ro kinh tế từ B1 và B4.

### Bằng chứng

- Commit `c19b331`.
- [Chỉ số và rủi ro](report/team/chi_so.md), [hồ sơ launch](report/team/ho_so_launch_v0.md), [bảng lỗi](report/team/bang_loi.md).

## Trần Dương Trung Tính — 2A202603488

### Phần việc phụ trách

- CP1: viết ba hàm A1 và hàm `mo_hinh`, tính chi phí theo loại yêu cầu và cộng chi phí cố định.
- CP2: chạy 9 kịch bản độ nhạy, kịch bản đổi hai yếu tố, so sánh giới hạn 1–3 lần chạy và kịch bản xem lại 100%.

### Đóng góp cụ thể

- Hoàn thành phần A–B trong `src/lab13.py`, vượt qua ba phép thử đáp án biết trước (1,20 · 1,25 · 1,25) và bàn giao bảng A–B cho Vĩ và Duy lúc 15:20.
- Điền hoàn chỉnh `bang_chi_phi.md`, xác định mức CPS 4.472 đ [simulated], chỉ ra `quoc_te` không hiệu quả và giới hạn 2 lần chạy rẻ nhất cho công ty.

### Bằng chứng

- Commit `83a65ee`.
- [Bảng chi phí](report/team/bang_chi_phi.md), [mã nguồn lab13.py](src/lab13.py).

## Nguyễn Nhựt Linh — 2A202603492

### Phần việc phụ trách

- CP3: rà soát và chốt 20 nhãn ở cột người gắn nhãn 1, đối chiếu với bộ nhãn của Duy và hoàn thiện bảng khắc phục.
- Sau chấm chéo Gate 2a: tiếp quản phần hoàn thiện báo cáo nhóm và tổng hợp kết quả từ hai phiếu chấm.

### Đóng góp cụ thể

- Ghi nhận hai cột nhãn trùng **20/20 ca**. Hoàn thiện **5 phương án khắc phục** cho các ca 1, 7, 18, 19 và 17, mỗi loại lỗi một ca.
- Cập nhật mục Kết quả của báo cáo nhóm với điểm, quyết định của hội đồng và nội dung hỏi đáp về cách giảm tần suất xem lại mà vẫn bảo đảm an toàn.

### Bằng chứng

- Commit `1ffb09d` và `4c94e7b` ghi nhận phần rà soát nhãn, đối chiếu và hoàn thiện bảng khắc phục.
- [Bảng lỗi](report/team/bang_loi.md), [báo cáo nhóm](report/team/group_report.md), [báo cáo cá nhân](report/team/2A202603492_NguyenNhutLinh.md).

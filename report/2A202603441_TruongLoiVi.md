# Báo cáo cá nhân — Trương Lợi Vĩ

## 1. Thông tin thành viên

- **Họ tên:** Trương Lợi Vĩ
- **MSSV:** 2A202603441
- **Email:** 26ai.vitl@vinuni.edu.vn
- **Vai trong nhóm:** Người kiểm số (phụ trách CP4 – D1 và thiết kế kế hoạch pilot; đồng thời tích hợp phần tính toán D1 vào mã nguồn).

## 2. Phần việc phụ trách

Phụ trách **CP4 – D1: Cỡ mẫu và thiết kế pilot (Gate 2a)**, bao gồm:

- Tính toán cỡ mẫu cần thiết cho thử nghiệm ở cấp request và cấp nhân viên (staff-level).
- Phân tích Design Effect (DE), Intraclass Correlation Coefficient (ICC) và giới hạn cỡ mẫu hiệu dụng khi phân nhóm theo nhân viên hoặc depot.
- Phân tích tính khả thi của thiết kế thử nghiệm với số lượng nhân viên và depot hiện có.
- Đánh giá phương án điều chỉnh Minimum Detectable Effect (MDE) để phù hợp với nguồn lực triển khai.
- Đề xuất đơn vị phân nhóm, tỷ lệ phân bổ control/treatment, cách tổ chức nhóm đối chứng và nhóm thử nghiệm.
- Xây dựng các điều kiện nhận diện tác động, rủi ro spillover, tiêu chí dừng thử nghiệm (stop rules) và phương án rollback.
- Hoàn thiện file `report/team/pilot_plan.yaml` và tích hợp phần tính toán D1 vào `src/lab13.py`.

## 3. Đóng góp cụ thể

### 3.1. Tính toán cỡ mẫu và đánh giá thiết kế thử nghiệm (D1)

Thực hiện các phép tính D1a–D1e dựa trên các giả định của bài lab:

- Baseline success rate: 70%.
- Significance level (alpha): 0.05.
- Statistical power: 0.80.
- ICC: 0.02.

Kết quả:

| Hạng mục | Kết quả |
|---|---:|
| D1a – Request-level, MDE 5 điểm phần trăm | 1.251 requests/nhóm |
| D1b – Staff-level, trung bình 75 requests/nhân viên | DE = 2.48; 3.103 requests/nhóm |
| D1b – Số nhân viên cần thiết | 42 nhân viên/nhóm |
| D1c – 20 nhân viên/nhóm | Tối đa 1.000 mẫu hiệu dụng |
| D1d – 6 depot/nhóm | Tối đa 300 mẫu hiệu dụng |
| D1e – MDE 6 điểm phần trăm | 859 requests/nhóm |
| D1e – Requests tối thiểu/nhân viên | 299 |
| D1e – Design Effect | 6.96 |
| D1e – Effective sample | 859.20 |
| Power nếu hiệu ứng thực tế chỉ đạt 5 điểm phần trăm với cỡ mẫu 859/nhóm | 0.6417 |

Từ kết quả trên, nhận thấy thiết kế với MDE 5 điểm phần trăm không khả thi khi chỉ có khoảng 40 nhân viên và 6 depot. Vì vậy, phân tích phương án nâng MDE lên 6 điểm phần trăm để giảm yêu cầu cỡ mẫu, đồng thời ghi nhận sự đánh đổi về khả năng phát hiện hiệu ứng nhỏ hơn.

### 3.2. Xây dựng kế hoạch pilot và stop rules

Hoàn thiện `report/team/pilot_plan.yaml`, trong đó:

- Đề xuất phân nhóm ở cấp nhân viên (staff-level).
- Xác định nhóm đối chứng và nhóm thử nghiệm vận hành đồng thời.
- Xác định rủi ro chia sẻ câu trả lời và quy trình giữa nhân viên (spillover risk).
- Đề xuất khóa trước primary metric, MDE, stop rules, rollback và decision date.
- Xây dựng ba nhóm điều kiện dừng:
  1. **Safety:** Theo dõi tỷ lệ mở lại trong 7 ngày; dừng trợ lý khi vượt ngưỡng an toàn đã xác định.
  2. **Cost:** Tạm dừng mở rộng nếu chi phí trên mỗi tác vụ thành công vượt ngưỡng 12.000 VND trong hai tuần liên tiếp.
  3. **Adoption:** Tạm dừng mở rộng và thực hiện phỏng vấn nhân viên nếu tỷ lệ bypass vượt 40% trong một tuần.
- Xây dựng phương án rollback: người phụ trách vận hành kích hoạt kill switch trong vòng 30 phút và chuyển khách hàng về quy trình xử lý thủ công.

### 3.3. Tích hợp và kiểm tra mã nguồn

- Tích hợp hàm tính cỡ mẫu hai tỷ lệ và các phép tính D1 vào `src/lab13.py`.
- Sử dụng `NormalDist`, `NormalIndPower` và `proportion_effectsize` để thực hiện các phép tính thống kê.
- Chạy chương trình để kiểm tra kết quả A1–B4 và D1 sau khi tích hợp.
- Kiểm tra cú pháp Python bằng `python -m py_compile lab13.py`.
- Kiểm tra tính hợp lệ của YAML bằng PyYAML.
- Kiểm tra thay đổi Git bằng `git diff --check`.

## 4. Bằng chứng

Các file và kết quả liên quan đến phần việc đã thực hiện:

| Bằng chứng | Nội dung |
|---|---|
| `src/lab13.py` | Phần mã nguồn tính toán D1 được tích hợp vào chương trình chính |
| `report/team/pilot_plan.yaml` | Kế hoạch pilot, thiết kế phân nhóm, stop rules và rollback |
| Commit `66f083c` | `Implement D1 pilot sizing and pilot plan` |
| Merge commit `e19895c` | Tích hợp nhánh `origin/main` vào main local để đồng bộ các đóng góp của nhóm |
| Output chạy `python lab13.py` | Các kết quả A1–B4 và D1 được thực thi thành công |
| Python compile | `python -m py_compile lab13.py` không phát sinh lỗi |
| YAML validation | YAML hợp lệ, đọc được các trường owner, assignment, MDE và decision date |
| Git validation | `git diff --check` không phát hiện lỗi whitespace |

Các kết quả D1 được in trực tiếp khi chạy chương trình, bao gồm cỡ mẫu request-level, staff-level, effective sample, Design Effect và statistical power.

## 5. Công cụ AI đã dùng

- **ChatGPT:** Hỗ trợ phân tích yêu cầu CP4, giải thích công thức tính cỡ mẫu, Design Effect, ICC và effective sample; hỗ trợ rà soát logic thiết kế pilot, stop rules và phương án rollback; hướng dẫn tích hợp và kiểm tra mã nguồn.
- **Python và các thư viện thống kê:** Sử dụng `statsmodels` và `statistics` để tính toán, kiểm tra cỡ mẫu và statistical power.
- **PyYAML:** Kiểm tra cú pháp và khả năng đọc dữ liệu trong `pilot_plan.yaml`.
- **Git/GitHub và Terminal:** Quản lý phiên bản, kiểm tra commit, đồng bộ thay đổi và tích hợp phần việc với nhánh chính của nhóm.

**Cách tự kiểm tra kết quả AI:** Không sử dụng nội dung AI đề xuất như kết quả mặc định. Các công thức và kết quả tính toán được chạy lại bằng Python; mã nguồn được kiểm tra bằng Python compile; file YAML được parse bằng PyYAML; các thay đổi được kiểm tra bằng Git. Kết quả A1–B4 và D1 được đối chiếu qua output thực thi chương trình.

## 6. Tự đánh giá

Tôi đã hoàn thành các nhiệm vụ được phân công ở CP4, bao gồm tính toán cỡ mẫu, đánh giá tính khả thi của thiết kế pilot, đề xuất các điều kiện dừng và phương án rollback, đồng thời tích hợp phần tính toán D1 vào mã nguồn chính.

Một đóng góp quan trọng là phân tích được sự khác biệt giữa request-level và staff-level randomization. Kết quả cho thấy việc phân nhóm theo nhân viên làm tăng yêu cầu cỡ mẫu do ảnh hưởng của ICC và Design Effect. Với nguồn lực giới hạn của bài toán, việc điều chỉnh MDE từ 5 lên 6 điểm phần trăm là một phương án cần thiết để cân nhắc khi xây dựng pilot.

Trong quá trình thực hiện, tôi cũng chú trọng đến khả năng tái lập kết quả thông qua mã nguồn, kiểm tra cú pháp, xác thực YAML và quản lý phiên bản bằng Git.

**Điểm cần tiếp tục cải thiện:** Cần rà soát thêm tính nhất quán giữa cỡ mẫu thống kê, số lượng nhân viên thực tế, các giai đoạn rollout và điều kiện vận hành trước khi nhóm đưa ra quyết định pilot cuối cùng. Ngoài ra, cần tiếp tục phối hợp với các thành viên để bảo đảm các giả định và ngưỡng dừng được thống nhất trên toàn bộ báo cáo.


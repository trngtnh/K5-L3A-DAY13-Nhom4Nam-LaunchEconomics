# Báo cáo cá nhân — Trần Dương Trung Tính — 2A202603488

## 1. Thông tin thành viên

- Họ tên: Trần Dương Trung Tính
- MSSV: 2A202603488
- Email: 26ai.tinhtdt@vinuni.edu.vn
- Vai trong nhóm: Người viết code (Nhiệm vụ A và B, CP1–CP2).

## 2. Phần việc phụ trách

Tôi phụ trách thực hiện toàn bộ CP1 và CP2 (Nhiệm vụ A và B):
- **CP1 (Nhiệm vụ A):** Xây dựng mô hình kinh tế chạy lại với 3 hàm A1 có đáp án biết trước; viết hàm `mo_hinh` tính toán chi phí thật từ trace (A2); phân tích chi phí và hiệu quả theo từng loại yêu cầu (A3); tính toán tác động của chi phí cố định 40 triệu đ/tháng cho phạm vi `noi_dia` + `hang_nang` ở 2 mức quy mô (A4).
- **CP2 (Nhiệm vụ B):** Thực hiện phân tích độ nhạy 9 kịch bản đổi từng yếu tố (B1); đánh giá kịch bản đổi cặp yếu tố để chứng minh tính cộng tuyến tính (B2); phân tích tối ưu chi phí cả hệ thống qua việc so sánh các giới hạn 1, 2, 3 lần chạy (B3); tính toán kịch bản xem lại 100% trên phạm vi pilot để tìm mốc hòa vốn thời gian xem lại (B4).
- **Điều phối và kỹ thuật:** Bàn giao kịp thời số liệu lúc 15:20 cho Vĩ và Duy; chuyển giao file `src/lab13.py` sau giờ giải lao cho Vĩ tiếp quản làm D1; phụ trách rà soát kỹ thuật và đồng bộ mã nguồn repository của nhóm.

## 3. Đóng góp cụ thể

- Trực tiếp triển khai mã nguồn Python trong `src/lab13.py`, hoàn thành và kiểm thử đạt 100% ba phép thử A1 (1,20 · 1,25 · 1,25).
- Tính toán chính xác từ 2 file CSV: Chi phí mỗi việc thành công toàn mẫu là 4.472 đ [simulated], gấp 16,3 lần hóa đơn token + tool (274,7 đ), chứng minh giờ nhân viên chiếm tới 92,5% chi phí (làm lại 51,8%, xem lại 40,7%).
- Phân tích hiệu quả theo loại yêu cầu: chứng minh loại `quoc_te` không hiệu quả (CPS 22.515 đ = 1,88× baseline 12.000 đ, chạy lại tới lần 3 tỉ lệ đúng chỉ còn 2,2%) để nhóm chốt phạm vi pilot tối ưu là `noi_dia` + `hang_nang`.
- Thực hiện 9 kịch bản độ nhạy, xếp hạng 3 yếu tố nhạy nhất: (1) Số ca làm lại (±51,8%), (2) Tỉ lệ xem lại (±40,7%), (3) Lương nhân viên (+23,1%).
- Chỉ ra rằng giới hạn 2 lần chạy là rẻ nhất cho toàn công ty (6.901.220 đ [simulated]), không trùng với mức CPS thấp nhất của trợ lý (1 lần: 4.111 đ), giúp công ty tránh lãng phí 548.561 đ.
- Hoàn thiện 100% báo cáo `report/team/bang_chi_phi.md`, đảm bảo mọi con số giả lập đều có nhãn `[simulated]` và câu trả lời súc tích, có số liệu thực tế.

## 4. Bằng chứng

- Commit `83a65ee`: Hoàn thành mô hình chi phí (Task A) và bảng độ nhạy (Task B).
- Mã nguồn: [src/lab13.py](../../src/lab13.py) (các hàm `so_lan_chay_ky_vong`, `ti_le_thanh_cong`, `he_so_chi_phi_moi_viec_thanh_cong`, `mo_hinh` và các khối phân tích A3, A4, B1–B4).
- Hồ sơ: [report/team/bang_chi_phi.md](bang_chi_phi.md).

## 5. Công cụ AI đã dùng

- **Công cụ:** Trợ lý AI (Gemini / ChatGPT).
- **Mục đích sử dụng:** Hỗ trợ giải thích các thuật toán xác suất kỳ vọng trong A1, kiểm tra cú pháp Python và hỗ trợ định dạng bảng biểu Markdown theo đúng rubric chấm điểm của bài lab.
- **Cách tự kiểm tra kết quả:** Tôi tự tay thiết lập môi trường ảo `.venv`, trực tiếp chạy script `lab13.py` trên dữ liệu thực tế trong terminal, kiểm tra từng phép tính thông qua các lệnh `assert` của đề bài. Tôi tự tính tay đối chiếu lại một số phép tính (tỷ lệ phần trăm và chi phí cả hệ thống) để đối chiếu chéo với slide đáp án của giảng viên, đảm bảo mọi số liệu đều xuất phát từ code và dữ liệu thật, không có số liệu bịa đặt.

## 6. Tự đánh giá

- Tôi đã hoàn thành tốt toàn bộ phần việc A–B được nhóm phân công, bàn giao đúng hạn mốc 15:20 để các bạn Vĩ và Duy hoàn thiện CP4 và CP5.
- Code viết rõ ràng, đúng chuẩn, không gây lỗi khi các bạn tiếp quản. Báo cáo bảng chi phí tuân thủ nghiêm ngặt quy định về nhãn `simulated` và không vi phạm các từ cấm của Gate 2a.

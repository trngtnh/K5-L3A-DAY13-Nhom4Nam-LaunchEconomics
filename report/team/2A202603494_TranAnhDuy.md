# Báo cáo cá nhân — Trần Anh Duy — 2A202603494

## 1. Thông tin thành viên

- Họ tên: Trần Anh Duy
- MSSV: 2A202603494
- Email: 26ai.duyta@vinuni.edu.vn
- Vai trong nhóm: Người gắn nhãn 2, kiêm giữ hồ sơ launch v0.

## 2. Phần việc phụ trách

Tôi phụ trách CP5, gồm đặc tả chỉ số, danh sách event, rủi ro kinh tế và tổng hợp hồ sơ launch v0. Ở CP3, tôi phụ trách bộ nhãn thứ hai cho 20 ca lỗi.

## 3. Đóng góp cụ thể

- Tính ba chỉ số từ `logix_requests.csv`: đóng trong 24 giờ và không mở lại trong 7 ngày 82,83% (994/1.200), bỏ qua gợi ý 27,12% (48/177), mở lại trong 7 ngày 4,25% (51/1.200).
- Đề xuất hai chỉ số cho pilot và đặc tả 7 event có `trace_id`. Tôi ghi cách nối event để tính từng chỉ số.
- Tổng hợp hai rủi ro kinh tế từ B1 và B4, cập nhật hồ sơ launch v0 và điền 20 nhãn ở cột người gắn nhãn 2.

## 4. Bằng chứng

- Commit `c19b331`: phần chỉ số CP5, bản nháp hồ sơ launch và bộ nhãn CP3.
- File: [chi_so.md](chi_so.md), [ho_so_launch_v0.md](ho_so_launch_v0.md), [bang_loi.md](bang_loi.md).

## 5. Công cụ AI đã dùng

Tôi dùng ChatGPT để hiểu công thức và soạn nội dung theo mẫu Markdown. Tôi tự chạy phép tính trên CSV, kiểm tra tử số và mẫu số của ba chỉ số, rồi đối chiếu số chi phí với bảng B1 và B4 của nhóm.

## 6. Tự đánh giá

Tôi đã đối chiếu được cả ba chỉ số với dữ liệu chạy thử. Khi có dữ liệu pilot, tôi cần kiểm tra các event có nối được theo `request_id` và các yêu cầu đã đủ thời gian theo dõi 7 ngày trước khi tính chỉ số mở lại.
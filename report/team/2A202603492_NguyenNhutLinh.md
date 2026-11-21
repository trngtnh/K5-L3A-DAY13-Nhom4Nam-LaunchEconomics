# Báo cáo cá nhân — Nguyễn Nhựt Linh — 2A202603492

## 1. Thông tin thành viên

- Họ tên: Nguyễn Nhựt Linh
- MSSV: 2A202603492
- Email: 26ai.linhnn2@vinuni.edu.vn
- Vai trong nhóm: Người gắn nhãn 1, phụ trách bảng lỗi ở nhiệm vụ C (CP3) và hoàn thiện báo cáo nhóm sau chấm chéo.

## 2. Phần việc phụ trách

Tôi phụ trách rà soát và chốt nhãn cho 20 ca lỗi ở cột người gắn nhãn 1. Khi Duy hoàn thành cột thứ hai, tôi phụ trách tổng hợp kết quả đối chiếu và hoàn thiện bảng khắc phục cho năm loại lỗi.

Sau chấm chéo Gate 2a, tôi tiếp quản phần hoàn thiện báo cáo nhóm và tổng hợp kết quả từ hai phiếu chấm.

## 3. Đóng góp cụ thể

- Rà soát và xác nhận 20 nhãn ở cột 1 theo năm loại lỗi của đề bài.
- Hoàn thiện bảng đối chiếu với cột nhãn của Duy. Hai cột trùng **20/20 ca (100%)**, nên bảng ghi nhận không có ca lệch nhãn.
- Hoàn thiện phương án khắc phục cho các ca **1, 7, 18, 19 và 17**, mỗi loại một ca. Mỗi phương án ghi cách phát hiện có thể đo được, hành động xử lý và một vai trò phụ trách. Với ca 7, tôi đưa vào bảng phương án đối soát thông báo hoàn tiền với sổ cái theo `trace_id` và mã lệnh hoàn.
- Hoàn thiện mục Kết quả trong báo cáo nhóm. Tôi ghi Nhom4Nam chấm Nhóm 9999 **30/30** và Nhóm 9999 chấm Nhom4Nam **30/30**, cả hai với quyết định **Go có điều kiện**. Tôi cũng tóm tắt phần hỏi đáp về cách giảm tần suất xem lại mà vẫn bảo đảm an toàn.

## 4. Bằng chứng

- Commit `1ffb09d` ghi 20 nhãn đã rà soát vào cột người gắn nhãn 1.
- Commit `4c94e7b` hoàn thiện kết quả đối chiếu và bảng khắc phục cho năm ca.
- Kết quả được lưu trong [bảng lỗi của nhóm](bang_loi.md).
- Kết quả chấm chéo được tổng hợp trong [mục Kết quả của báo cáo nhóm](group_report.md#4-kết-quả).

## 5. Công cụ AI đã dùng

Tôi dùng Codex để tham khảo cách phân loại, nhận gợi ý nhãn, so sánh từng dòng của hai cột và soạn nháp bảng khắc phục cùng báo cáo cá nhân. Tôi rà soát và xác nhận 20 nhãn gợi ý trước khi đưa vào bảng. Kết quả 20/20 được kiểm tra bằng cách so hai cột theo mã ca và mô tả mức trùng giữa hai cột hiện có. Sau chấm chéo, tôi dùng Codex để tổng hợp điểm, quyết định và phần hỏi đáp từ hai phiếu vào báo cáo nhóm.

## 6. Tự đánh giá

Tôi đã hoàn thiện bảng đối chiếu và bàn giao năm phương án khắc phục để nhóm đưa vào hồ sơ launch. Ca 7 giúp tôi thấy một biện pháp dễ kiểm chứng cần nêu rõ tín hiệu phải đối soát, tần suất kiểm tra và ai chịu trách nhiệm. Lần sau, tôi sẽ lưu bộ nhãn tự gắn trước khi xem gợi ý để nhóm có thể đo mức đồng thuận độc lập.

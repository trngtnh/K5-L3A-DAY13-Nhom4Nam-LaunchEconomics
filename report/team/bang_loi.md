# Bảng lỗi và cách khắc phục · Nhiệm vụ C

20 ca lỗi nằm trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`. Năm loại theo Google PAIR: **Do người dùng · Hệ thống · Ngữ cảnh · Giới hạn hệ thống · Ngầm**. Gắn nhãn theo nguyên nhân gốc, không theo chỗ cần sửa.

## Hai bộ nhãn độc lập

Người gắn nhãn 1: Nguyễn Nhựt Linh · Người gắn nhãn 2: Trần Anh Duy (gắn trong 8 phút, không trao đổi)

| Ca | Nhãn người 1 | Nhãn người 2 | Trùng? | Nhãn thống nhất |
| --: | --- | --- | --- | --- |
| 1 | Do người dùng | Do người dùng | Có | Do người dùng |
| 2 | Hệ thống | Hệ thống | Có | Hệ thống |
| 3 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 4 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 5 | Ngầm | Ngầm | Có | Ngầm |
| 6 | Do người dùng | Do người dùng | Có | Do người dùng |
| 7 | Hệ thống | Hệ thống | Có | Hệ thống |
| 8 | Hệ thống | Hệ thống | Có | Hệ thống |
| 9 | Do người dùng | Do người dùng | Có | Do người dùng |
| 10 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 11 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 12 | Ngầm | Ngầm | Có | Ngầm |
| 13 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 14 | Do người dùng | Do người dùng | Có | Do người dùng |
| 15 | Hệ thống | Hệ thống | Có | Hệ thống |
| 16 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 17 | Ngầm | Ngầm | Có | Ngầm |
| 18 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 19 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 20 | Hệ thống | Hệ thống | Có | Hệ thống |

**Tỉ lệ đồng thuận:** 20/20 = 100%.

## Quy tắc phân biệt cho các ca không trùng

Mỗi ca không trùng một câu. Đồng thuận dưới 80% thì ghi định nghĩa đã viết lại.

- Không có ca lệch nhãn.

## Bảng khắc phục cho 5 ca, mỗi loại một ca

Cách phát hiện phải đo được (event, ngưỡng, tần suất). Người phụ trách là một vai trò, không ghi "cả đội". Các event, ngưỡng và tần suất dưới đây là đề xuất cho pilot.

| Ca | Loại lỗi | Phát hiện bằng gì | Khắc phục thế nào | Ai phụ trách |
| --: | --- | --- | --- | --- |
| 1 | Do người dùng | Kiểm tra mỗi lần khách gửi thông tin hoàn tiền. Ghi `refund_account_validation_failed` nếu số tài khoản thiếu chữ số theo quy tắc của ngân hàng đã chọn. Chặn ngay khi kiểm tra thất bại. | Đánh dấu ô số tài khoản, giải thích lỗi và cho khách nhập lại. Chỉ tạo lệnh hoàn khi số tài khoản qua kiểm tra. | Kỹ sư tích hợp thanh toán |
| 7 | Hệ thống | Mỗi 5 phút, đối soát `refund_success_sent` với `ledger_refund_committed` theo `trace_id` và mã lệnh hoàn. Cảnh báo khi có ít nhất 1 thông báo thành công thiếu bản ghi sổ cái tương ứng. | Chỉ gửi thông báo thành công sau khi sổ cái xác nhận. Nếu API vẫn lỗi sau 3 lần thử, báo khách yêu cầu đang xử lý và chuyển cho nhân viên kiểm tra. | Kỹ sư phụ trách sổ cái |
| 18 | Ngữ cảnh | Trước mỗi lần gửi, kiểm tra nội dung có đủ phí gốc, tỷ lệ hoàn và số tiền hoàn. Ghi `refund_breakdown_missing` và giữ lại tin nhắn nếu thiếu ít nhất 1 mục. | Dùng mẫu thông báo hiển thị phép tính, ví dụ **30.000 đ × 50% = 15.000 đ**. Gửi lại thông báo có đủ thông tin nếu khách đã nhận bản thiếu. | Trưởng nhóm CSKH |
| 19 | Giới hạn hệ thống | Kiểm tra ngày tạo đơn ở mỗi lượt tra cứu. Ghi `order_outside_lookup_window` khi đơn cũ hơn 12 tháng và chuyển nhân viên ngay. | Thông báo rõ cửa sổ tra cứu 12 tháng. Chuyển yêu cầu kèm mã đơn, thời điểm đặt hàng và lý do chuyển để nhân viên tra hồ sơ lưu trữ. | Trưởng nhóm CSKH |
| 17 | Ngầm | Hằng ngày, đối soát các khoản hoàn của đơn dưới 2 kg với phiên bản bảng giá có hiệu lực tại thời điểm áp dụng. Cảnh báo khi phát hiện ít nhất 1 ca dùng sai phiên bản. | Xóa bộ nhớ đệm khi bảng giá mới có hiệu lực và ghi mã phiên bản vào trace. Rà soát các đơn bị ảnh hưởng để điều chỉnh số tiền theo quy trình. | Kế toán trưởng |

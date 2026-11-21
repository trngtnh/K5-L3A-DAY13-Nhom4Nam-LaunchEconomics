# Đặc tả chỉ số, event và rủi ro kinh tế · Nhiệm vụ E1, E2

## E1 · Đặc tả chỉ số

| Loại | Chỉ số | Công thức | Tính thử trên 1.200 yêu cầu |
| --- | --- | --- | --- |
| Chính (kết quả) | % yêu cầu đóng trong 24 giờ và không mở lại trong 7 ngày | Số yêu cầu có `dong_trong_24h = 1` và `mo_lai_trong_7_ngay = 0` chia tổng số yêu cầu | 82,83% (994/1.200) |
| Dùng | Tỉ lệ bỏ qua gợi ý | Số yêu cầu đã xem lại có `quyet_dinh_xem_lai` là `sua` hoặc `bo` chia số yêu cầu có `duoc_xem_lai = 1` | 27,12% (48/177) |
| An toàn | Tỉ lệ lỗi lọt đến khách | Số yêu cầu có `mo_lai_trong_7_ngay = 1` chia tổng số yêu cầu | 4,25% (51/1.200) |
| Dùng | Tỉ lệ mở trợ lý trên yêu cầu đủ điều kiện | Số yêu cầu đủ điều kiện có lượt mở trợ lý chia tổng số yêu cầu đủ điều kiện của nhóm can thiệp | Không cần tính |
| An toàn | Tỉ lệ đơn hoàn sai số tiền trong mẫu kiểm tra hằng tuần | Số đơn trong mẫu có số tiền đã hoàn khác số tiền đúng chia tổng số đơn đã kiểm tra | Không cần tính |

Tỉ lệ đóng trong 24 giờ và không mở lại trong 7 ngày ở đợt chạy thử là 82,83% (994/1.200). Đợt chạy thử không có nhóm đối chứng nên chưa đo được tác động của trợ lý.

## Danh sách event

| Event | Ai tạo | Thuộc tính chính | Thời điểm |
| --- | --- | --- | --- |
| `refund_request_created` | Hệ thống ticket | `trace_id`, `request_id`, `created_at`, `arm`, `loai`, `eligible` | Khi tiếp nhận yêu cầu ở cả hai nhóm |
| `agent_opened` | Giao diện CSKH | `trace_id`, `request_id`, `opened_at`, `staff_id` | Khi nhân viên mở trợ lý cho yêu cầu |
| `staff_review_decision` | Giao diện CSKH | `trace_id`, `request_id`, `reviewed_at`, `decision` (`giu`, `sua`, `bo`), `phut_xem_lai` | Khi nhân viên lưu quyết định xem lại |
| `staff_rework_completed` | Giao diện CSKH | `trace_id`, `request_id`, `completed_at`, `phut_lam_lai`, `reason` | Khi nhân viên làm lại xong yêu cầu |
| `ticket_closed` | Hệ thống ticket | `trace_id`, `request_id`, `closed_at` | Khi yêu cầu được đóng ở một trong hai nhóm |
| `ticket_reopened` | Hệ thống ticket | `trace_id`, `request_id`, `reopened_at`, `reason` | Khi yêu cầu được mở lại ở một trong hai nhóm |
| `audit_sample_checked` | Kế toán | `trace_id`, `request_id`, `checked_at`, `so_tien_da_hoan`, `so_tien_dung` | Khi kiểm tra xong từng đơn trong mẫu hằng tuần |

**Kiểm tra chéo:** Nối event bằng `request_id` và đếm mỗi yêu cầu một lần. Khi tính các chỉ số có cửa sổ 7 ngày, chỉ dùng các yêu cầu đã đủ thời gian theo dõi.

- Đóng trong 24 giờ và không mở lại trong 7 ngày: lấy mốc tạo từ `refund_request_created`, mốc đóng từ `ticket_closed` và tra `ticket_reopened` trong 7 ngày sau khi đóng.
- Bỏ qua gợi ý: dùng quyết định cuối cùng trong `staff_review_decision` của mỗi yêu cầu đã xem lại. Tử số gồm `sua` và `bo`.
- Mở lại trong 7 ngày: dùng `refund_request_created` để xác định tập yêu cầu, rồi nối `ticket_closed` và `ticket_reopened` để kiểm tra cửa sổ 7 ngày sau khi đóng.
- Mở trợ lý: lọc `eligible = true` và nhóm can thiệp từ `refund_request_created`, rồi đếm số yêu cầu có `agent_opened`.
- Hoàn sai tiền: dùng `audit_sample_checked` để so `so_tien_da_hoan` với `so_tien_dung` trên từng đơn được kiểm tra.

## E2 · Rủi ro kinh tế

| Rủi ro | Tác động đã tính | Dấu hiệu theo dõi | Hành động | Người phụ trách |
| --- | --- | --- | --- | --- |
| Số ca làm lại tăng gấp đôi | B1: Chi phí mỗi việc thành công lên 6.787 đ, tăng 51,8% so với mức gốc [simulated]. | Tỉ lệ yêu cầu có `staff_rework_completed` vượt 7% trong tuần (ngưỡng đề xuất). | Rà 20 trace làm lại để tìm nguyên nhân. Nếu lỗi tập trung ở `hang_nang`, thu hẹp pilot về `noi_dia`. | PM trợ lý hoàn phí |
| Phải xem lại 100% trong phạm vi `noi_dia` và `hang_nang` | B4: Chi phí mỗi việc thành công là 11.743 đ với 9 phút làm lại mỗi ca, hoặc 12.415 đ với 15,3 phút mỗi ca [simulated]. Mốc nhân viên tự làm là 12.000 đ/yêu cầu. | Cuối bước rollout 25%, hơn 50% yêu cầu có `staff_review_decision` (ngưỡng đề xuất). Theo dõi thêm số phút xem lại thực tế. | Rà các nhóm yêu cầu cần xem lại. Chỉ giảm tỉ lệ xem lại theo từng bước khi đạt ngưỡng an toàn trong `pilot_plan.yaml`. | Trưởng nhóm CSKH |
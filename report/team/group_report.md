# Báo cáo nhóm

Báo cáo ngắn, tối đa 2 trang. Số liệu chi tiết nằm trong các file hồ sơ; ở đây chỉ dẫn lại con số chính.

## 1. Thông tin nhóm

- Tên nhóm: Nhom4Nam
- Lớp: L3A
- Thành viên: xem `TEAM.md`

## 2. Mục tiêu và cách tiếp cận

Nhóm đánh giá chi phí của trợ lý hoàn phí LogiX-VN và thiết kế pilot có đối chứng. Phân tích dùng 1.200 yêu cầu và 1.624 lần chạy agent trong bộ dữ liệu của lab.

## 3. Giải pháp

- A–B: Tính chi phí từ token, tool, thời gian xem lại và làm lại. So sánh chi phí theo loại yêu cầu và theo giới hạn số lần chạy. Xem [bảng chi phí](bang_chi_phi.md).
- C: Đối chiếu nhãn của 20 ca theo nguyên nhân gốc và đề xuất 5 phương án phát hiện, khắc phục, mỗi loại lỗi một phương án. Xem [bảng lỗi](bang_loi.md).
- D: Thiết kế pilot chia ngẫu nhiên theo nhân viên, có đối chứng cùng thời gian và luật dừng. Xem [kế hoạch pilot](pilot_plan.yaml).
- E: Tính chỉ số chạy thử, đặc tả event và tổng hợp rủi ro để trình Gate 2a. Xem [chỉ số](chi_so.md) và [hồ sơ launch](ho_so_launch_v0.md).

## 4. Kết quả

Chi phí trên toàn mẫu là 4.472 đ/việc thành công trước chi phí cố định [simulated]. Ba chỉ số chạy thử là 82,83% đóng trong 24 giờ và không mở lại trong 7 ngày, 27,12% bỏ qua gợi ý và 4,25% mở lại trong 7 ngày.

- Đề xuất cuối của nhóm: Go có điều kiện cho pilot giới hạn ở `noi_dia` và `hang_nang`.
- Chấm chéo do Nhom4Nam thực hiện: nhóm 9999 được **30/30**, với quyết định **Go có điều kiện**. Nhóm chấm hỏi về ngưỡng giảm xem lại 15%. Đội trình đề xuất hậu kiểm ngẫu nhiên 5% đơn được duyệt tự động. Xem [phiếu chấm nhóm 9999](phieu_cham.md).
- Kết quả Nhom4Nam nhận từ hội đồng nhóm 9999: **30/30** (10/10 ở cả ba tiêu chí), với quyết định **Go có điều kiện** cho `noi_dia` và `hang_nang`. Khi hội đồng hỏi cách giảm xem lại mà vẫn bảo đảm an toàn, nhóm đề xuất dùng dữ liệu tuần đầu để phân tầng rủi ro, chỉ giảm xem lại ở nhóm rủi ro thấp khi đạt yêu cầu chất lượng, duy trì xem lại 100% ở nhóm rủi ro cao và quay lại mức xem lại trước đó nếu tỷ lệ bỏ sót tăng.

## 5. Khó khăn và cách xử lý

Với 20 nhân viên mỗi nhóm, cỡ mẫu hiệu dụng tối đa không đủ cho mục tiêu phát hiện chênh lệch 5 điểm phần trăm. Nhóm thiết kế pilot cho mức chênh lệch 6 điểm phần trăm, với ít nhất 299 yêu cầu mỗi nhân viên.

## 6. Tổng hợp đóng góp

Tính phụ trách A–B. Vĩ phụ trách D và kiểm số. Linh phụ trách tổng hợp bảng lỗi. Duy gắn bộ nhãn thứ hai và phụ trách CP5. Xem [TEAM.md](../../TEAM.md).

## 7. Hạn chế và hướng cải thiện

Đợt chạy thử chưa có nhóm đối chứng. Trong pilot, nhóm sẽ dùng nhóm đối chứng chạy cùng thời gian và đo thời gian xem lại, làm lại thực tế để cập nhật chi phí.

## 8. Tài liệu tham khảo

- [Dữ liệu và công thức Lab 13](../../docs/du_lieu_va_cong_thuc.md).
- [Hướng dẫn chi tiết Lab 13](../../docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md).

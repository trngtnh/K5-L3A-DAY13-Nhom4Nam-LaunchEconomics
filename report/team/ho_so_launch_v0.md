# Hồ sơ launch v0 · Trợ lý hoàn phí LogiX-VN · Gate 2a

Một trang. Cột trạng thái chỉ nhận: **Xong, có bằng chứng · Chưa · Giả lập**. Mục nào dựa trên cột `_simulated` ghi Giả lập. Người phụ trách là một vai trò, không ghi "cả đội". Gate 2a chỉ duyệt kế hoạch pilot: không viết như thể trợ lý đã được duyệt chạy chính thức (xem quy tắc 5 trong `README.md`).

Nhóm: Nhom4Nam · Lớp: L3A

| Mục | Con số chính | Trạng thái | Người phụ trách |
| --- | --- | --- | --- |
| 1 · Chi phí mỗi việc thành công | 4.472 đ/việc thành công trên toàn mẫu 1.200 yêu cầu, chưa cộng chi phí cố định [simulated]. | Giả lập | PM trợ lý hoàn phí |
| 2 · Ba yếu tố nhạy nhất | Làm lại gấp đôi: +51,8%; xem lại gấp đôi: +40,7%; lương tăng 25%: +23,1% [simulated]. | Giả lập | PM trợ lý hoàn phí |
| 3 · So với nhân viên tự làm | Với giới hạn 3 lần chạy, tổng chi phí hệ thống gồm cả phần nhân viên làm thay là 5.865 đ/yêu cầu trên toàn mẫu [simulated], so với 12.000 đ/yêu cầu khi nhân viên tự làm. | Giả lập | Giám đốc vận hành |
| 4 · Chỉ số chính, chỉ số dùng, chỉ số an toàn | Đợt chạy thử: đóng trong 24 giờ và không mở lại trong 7 ngày 82,83% (994/1.200); bỏ qua gợi ý 27,12% (48/177); mở lại trong 7 ngày 4,25% (51/1.200). | Xong, có bằng chứng | PM trợ lý hoàn phí |
| 5 · Bảng lỗi và cách khắc phục | Hai bộ nhãn độc lập trùng 20/20 ca. Bảng khắc phục có 5 biện pháp cho 5 loại lỗi, mỗi biện pháp có cách phát hiện và vai trò phụ trách. | Xong, có bằng chứng | PM trợ lý hoàn phí |
| 6 · Pilot plan | Chia ngẫu nhiên theo nhân viên, 20 người mỗi nhóm, có đối chứng cùng thời gian. Cần 859 yêu cầu hiệu dụng mỗi nhóm, tương ứng ít nhất 299 yêu cầu/nhân viên, để phát hiện chênh lệch 6 điểm phần trăm với power 80%. Nếu chênh lệch thực tế là 5 điểm, power còn 64,17%. | Xong, có bằng chứng | Giám đốc vận hành |
| 7 · Rủi ro kinh tế | Làm lại gấp đôi: 6.787 đ/việc thành công (+51,8%). Xem lại 100%: 12.415 đ/việc thành công nếu mỗi ca làm lại mất 15,3 phút [simulated cho cả hai kịch bản]. | Giả lập | PM trợ lý hoàn phí |

- Giám đốc vận hành kiểm tra đủ 20 nhân viên mỗi nhóm và xác nhận mức chênh lệch tối thiểu 6 điểm phần trăm vào 21/11/2026.
- Trưởng nhóm CSKH kiểm tra dữ liệu xem lại và làm lại vào 21/11/2026. Nếu phải xem lại 100%, rà chi phí trước khi tăng mức rollout.
- PM trợ lý hoàn phí kiểm tra các event có `trace_id` và xác nhận các biện pháp an toàn cần thiết đã sẵn sàng vào 21/11/2026.

**Đề xuất:** Go có điều kiện cho pilot giới hạn ở `noi_dia` và `hang_nang`.

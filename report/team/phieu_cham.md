# Phiếu chấm hội đồng Gate 2a

Nhóm số n chấm nhóm số n + 1; nhóm cuối chấm nhóm 1. Chấm theo bằng chứng trong hồ sơ, không theo cách trình bày: một đề xuất No-go có lý do bằng số được điểm cao hơn một đề xuất Go bỏ qua con số bất lợi.

- Nhóm chấm (hội đồng): Nhom4Nam
- Nhóm được chấm: 9999

| Tiêu chí | 0 điểm | 5 điểm | 10 điểm | Điểm | Lý do (có số) |
| --- | --- | --- | --- | ---: | --- |
| Đề xuất khớp bằng chứng | Mâu thuẫn với số của chính nhóm | Khớp nhưng bỏ qua một con số bất lợi | Khớp, nêu cả con số bất lợi và cách xử lý | 10 | Nhóm 9999 đề xuất 'Go có điều kiện' khớp với dữ liệu, nêu rõ 2 con số bất lợi: power giảm còn ~0,64 nếu tác động thật 5 điểm (cần MDE 6 điểm để đạt power 0,80), và xem lại 100% chi phí lên đến 11.743 đ (0,98×) hoặc 12.415 đ (1,03× với 15,3p làm lại) [simulated]; đi kèm 4 điều kiện cụ thể (idempotency_key, chốt MDE 6đ, đo thật thay simulated sau tuần 1, giảm xem lại theo bậc) có người phụ trách và hạn hoàn thành rõ ràng. |
| Số giả lập và phạm vi | Không nhãn; phạm vi "mọi yêu cầu" | Có nhãn hoặc có thu hẹp phạm vi | Nhãn ở mọi số giả lập; phạm vi thu hẹp có lý do bằng số | 10 | Gắn đầy đủ nhãn [simulated] ở toàn bộ các con số giả lập (Mục 1, 2, 3, 7 và trong đề xuất); thu hẹp phạm vi pilot về `noi_dia` (0,22×) + `hang_nang` (0,69×) có lý do định lượng (loại `quoc_te` 1,88× và `doi_tac` 0,85×); tính đầy đủ chi phí cố định 40 triệu đ/tháng thành 4.599 đ (0,38× ở 45k yc/tháng) hoặc 5.784 đ (0,48× ở 22,5k yc/tháng) [simulated]. |
| Pilot ra được quyết định | Không đối chứng hoặc thiếu cỡ mẫu | Đủ cỡ mẫu, luật dừng chung chung | Tách được tác động, đủ mẫu, luật dừng có ngưỡng, thời hạn, người có quyền dừng | 10 | Thiết kế tách được tác động qua phân nhóm đối chứng ngẫu nhiên theo nhân viên 20 + 20 (phân tầng depot), rollout 10%→25%→50%; đủ mẫu hiệu dụng n=859/nhánh (m≥299 yc/NV, DE=6,96); đủ 3 luật dừng 4 vế (mở lại ≥+2đ hoặc >6%, chi phí >8.000 đ, bỏ qua >40%), rollback 30 phút, ngày quyết định `2027-01-26` và người có quyền dừng là Giám đốc vận hành LogiX-VN. |
| **Tổng** | | | | **30 / 30** | |

**Quyết định của hội đồng:** Go có điều kiện

**Lý do:** Hồ sơ của nhóm 9999 đạt chất lượng xuất sắc, đầy đủ 7 mục; các con số chính xác và minh bạch; nhận diện đúng 3 rủi ro kinh tế lớn nhất (làm lại +51,8%, xem lại 100% lên tới 1,03×, cố định tăng gấp đôi khi giảm nửa khối lượng) và mốc hòa vốn thời gian xem lại ≤4,8–5,1 phút; thiết kế kế hoạch pilot chặt chẽ, tách được tác động và đưa ra 4 điều kiện kiểm soát rủi ro rõ ràng trước khi nâng rollout.

**Một câu hỏi cho đội trình:** Trong Điều kiện 4, nhóm đưa ra mốc hòa vốn thời gian xem lại là ≤4,8–5,1 phút/lần và quy tắc giảm xem lại theo bậc cho đơn `noi_dia` khi `sua + bo < 15%`. Đội căn cứ vào cơ sở dữ liệu nào để chọn mốc 15% và cơ chế giám sát thực tế để không bỏ lọt các ca sai sót là gì?

**Câu trả lời của đội trình (ghi lại tại buổi):** Đội giải thích: Tỉ lệ bỏ qua (`sua + bo`) hiện tại trong đợt chạy thử là 27,12% (48/177). Ngưỡng 15% thể hiện độ chính xác của agent đã cải thiện gần gấp đôi so với đợt chạy thử. Về kiểm soát, đội kết hợp lấy mẫu ngẫu nhiên 5% đơn đã duyệt tự động để hậu kiểm (post-audit) và dùng telemetry bắt event `review_completed` để tính thời gian thực; nếu tỉ lệ mở lại 7 ngày tăng vượt mốc 3,97% sẽ kích hoạt luật dừng chi phí và quay lại mức xem lại ban đầu.

> **Phạm vi nộp:** Bài cá nhân
> **Người thực hiện / branch:** `ntthduong`

# 01 — Problem Scan & Quick Problem Cards

## Phạm vi và cách sử dụng dữ liệu

Đóng vai AI Product Engineer tại Vin Smart Future theo bối cảnh của đề bài. Các quy trình dưới đây là **giả thuyết nghiệp vụ để scoping**, tham khảo worksheet/inspiration kit; chưa có phỏng vấn hay dữ liệu vận hành nội bộ. Mọi thời gian, khối lượng và mục tiêu là **giả định thiết kế/target**, không phải thống kê đã được Vingroup xác nhận. Trước pilot phải đo baseline và xác minh với chủ quy trình.

## Phase 1 — SCAN: quét cơ hội qua 4 lenses

| # | Đơn vị | Lens | Actor và bài toán cụ thể | Bằng chứng cần thu thập |
|---|---|---|---|---|
| 1 | Xanh SM | Tốn thời gian; Stakeholder Pain | Điều phối viên chuyển qua nhiều màn hình khi tài xế báo pin thấp; tài xế chờ xác minh trạm/cứu hộ và tin hướng dẫn. | Timestamp ticket, thời gian tra cứu, cuộc gọi đã ẩn danh; phỏng vấn dispatcher. |
| 2 | VinFast | Lặp lại | Kế toán đối chiếu phiên sạc với hóa đơn, nhập tay mã phiên và phát hiện lệch tiền/kWh. | Bảng phiên sạc và hóa đơn mẫu, tỷ lệ thiếu mã phiên; kiểm tra rule join trước. |
| 3 | Vinhomes | AI-upgrade; Lặp lại | CSKH đọc phản ánh tiếng Việt tự do, xác định tòa nhà/loại sự cố và viết nháp phản hồi đầu tiên. | Ticket gán nhãn bởi nhân viên, lịch sử chuyển nhầm bộ phận và mẫu phản hồi được duyệt. |
| 4 | Vinmec | Tốn thời gian; Stakeholder Pain | Bác sĩ tổng hợp nhiều ghi chú để soạn tóm tắt xuất viện; phải rà lại thuốc và diễn biến. | Hồ sơ đã được phép sử dụng, ẩn danh và đánh giá bởi bác sĩ; không suy diễn chỉ định. |
| 5 | Vinpearl | AI-upgrade; Stakeholder Pain | Quản lý đọc review đa ngôn ngữ để phát hiện phàn nàn cần xử lý sớm và soạn nháp trả lời. | Review được phép dùng, nhãn mức khẩn cấp và thời gian manager xử lý. |
| 6 | Xanh SM | Lặp lại; Tốn thời gian | Chuyên viên tổng hợp ghi chú hủy chuyến, gom lý do và tạo báo cáo tuần. | Ghi chú ẩn danh, taxonomy lý do, nhãn đối chứng do hai người kiểm tra. |

## Phase 2 — QUICK-ASSESS: 3 thẻ bài toán

### Card #1 — Co-pilot xử lý sự cố pin Xanh SM (chọn deep-dive)

| Trường | Nội dung |
|---|---|
| Bài toán (1 câu) | Giảm thời gian từ tiếp nhận sự cố pin đến khi điều phối viên phê duyệt phương án hỗ trợ đầu tiên. |
| Công ty / Actor | Xanh SM; điều phối viên trực tiếp xử lý, tài xế và khách đang chờ là người chịu ảnh hưởng. |
| Workflow hiện tại (5 bước) | Nhận cuộc gọi (2 phút) → xác minh pin/GPS (2) → tra cứu trạm/cứu hộ (5) → soạn và kiểm tra hướng dẫn (5) → liên hệ, xác nhận tiếp nhận (1). |
| Bottleneck | Bước 3–4: giả định 10/15 phút, phải đối chiếu dữ liệu và diễn đạt thông tin ngắn gọn. |
| AI hỗ trợ ở đâu? | Tóm tắt mô tả tự do và soạn nháp; truy vấn trạm, lọc cổng sạc, kiểm tra mức pin là code/rule có dữ liệu xác minh. |
| Metric có số | Target median từ 15 xuống ≤5 phút/ticket; thời gian soạn + duyệt từ 5 xuống ≤2 phút; ≥98% nháp đúng dữ kiện đã cung cấp. |
| Quick Architecture | **LLM Feature + Rule/State-Machine**; chọn LLM cho ngôn ngữ, không giao quyết định điều xe cho agent. |
| Boundary / Fallback | Nháp có `[DRAFT_ONLY] `; pin <5% chỉ đề xuất sạc di động dạng JSON; dispatcher duyệt cả nháp và đề xuất. API lỗi/thiếu dữ liệu → xác minh và dùng mẫu thủ công. |
| Điều kiện khả thi | Cần quyền đọc telemetry/trạm sạc và người vận hành xác nhận chính sách; prototype hiện chỉ dùng tình huống tổng hợp. |

### Card #2 — Phân loại và soạn phản hồi phản ánh cư dân Vinhomes

| Trường | Nội dung |
|---|---|
| Bài toán (1 câu) | Rút ngắn thời gian nhân viên phân loại và soạn phản hồi đầu tiên cho phản ánh cư dân. |
| Công ty / Actor | Vinhomes; CSKH và ban quản lý tòa nhà. |
| Workflow hiện tại (4 bước) | Nhận phản ánh (1 phút) → đọc và xác minh tòa/căn hộ (3) → chọn bộ phận xử lý (2) → soạn, duyệt phản hồi (4). |
| Bottleneck | Đọc mô tả và viết lại phản hồi: giả định 7/10 phút; nội dung đa nghĩa gây chuyển nhầm đội xử lý. |
| AI hỗ trợ ở đâu? | Gợi ý nhãn từ danh mục đóng, tóm tắt vấn đề, draft phản hồi từ SOP đã duyệt. |
| Metric có số | Target median thao tác từ 10 xuống ≤4 phút/ticket; macro-F1 phân loại ≥0,90 trên 200 ticket gán nhãn; chuyển nhầm ≤5%. |
| Quick Architecture | **LLM Feature**, rule xác định tòa theo mã và phân tuyến theo bảng trách nhiệm. |
| Boundary / Fallback | Không cam kết bồi thường/phí, không đóng ticket hoặc gửi tự động; thông tin thiếu hoặc phản ánh khẩn cấp chuyển người xử lý. |
| Điều kiện khả thi | Cần SOP và dữ liệu đã khử định danh; phải so sánh với keyword router trước khi mua LLM. |

### Card #3 — Đối chiếu hóa đơn sạc VinFast

| Trường | Nội dung |
|---|---|
| Bài toán (1 câu) | Giảm thao tác đối chiếu thủ công giữa phiên sạc và hóa đơn đối tác. |
| Công ty / Actor | VinFast; nhân viên kế toán đối soát. |
| Workflow hiện tại (4 bước) | Nhận file (2 phút/lô) → chuẩn hóa mã/ngày/đơn vị (5) → đối chiếu và đánh dấu lệch (10) → nhân viên duyệt báo cáo (3). |
| Bottleneck | Bước 2–3: giả định 15/20 phút trên lô 100 dòng có cấu trúc. |
| AI hỗ trợ ở đâu? | Chưa cần LLM trong luồng chính; chỉ cân nhắc trích xuất nếu hóa đơn ảnh/PDF không có cấu trúc. |
| Metric có số | Target ≤3 phút/lô 100 dòng, phát hiện 100% sai lệch đã cài trong tập thử; false positive ≤1% khi đối chiếu tiền theo chính sách làm tròn đã thống nhất. |
| Quick Architecture | **Rule / No AI**: join theo mã phiên, kiểm tra trùng, so tiền và kWh bằng kiểu số thập phân. |
| Boundary / Fallback | Không tự ghi sổ hoặc thanh toán; dòng thiếu mã và sai lệch chuyển kế toán, lưu báo cáo lý do. |
| Điều kiện khả thi | Chuẩn hóa khóa đối chiếu và quy tắc thuế/làm tròn; LLM không được là nguồn tính toán tiền. |

## Phản biện CFO / Trưởng vận hành và lựa chọn

1. **Baseline chưa đo:** không thể biến 15 phút hoặc 80 ca/ngày trong ví dụ thành số liệu thực tế. Cách sửa: ghi giả định và thiết kế đo trước–sau theo loại ca.
2. **LLM không làm bản đồ tốt hơn hệ thống chuyên dụng:** tra cứu và lọc trạm nên là API/rule; LLM chỉ diễn đạt dữ kiện. Benchmark nháp theo template để chứng minh lợi ích tăng thêm.
3. **Chi phí và rủi ro HITL:** thời gian review có thể xóa hết lợi ích soạn nháp; không dùng riêng latency model làm KPI. Đo cả thời gian operator, tỷ lệ phải sửa và tổng chi phí/ticket.

**Chọn Card #1 cho bài lab:** scope hẹp, có hai ranh giới cụ thể phù hợp prototype bắt buộc, dễ tạo adversarial inputs và controls. Đây là lựa chọn cá nhân để nhóm xem xét, chưa phải quyết định đã họp thống nhất.

- Card #2: giữ trong backlog vì cần nhãn ticket/SOP và một bộ đánh giá phân loại khác.
- Card #3: phù hợp triển khai rule-based trước; không thêm AI chỉ để có AI.
- Card #4 trong SCAN (Vinmec): chưa chọn vì chưa có hồ sơ được cấp quyền và reviewer lâm sàng.

**Đầu ra tiếp theo:** [Deep Dive](02-deep-dive-report.md), [AI Log](03-ai-log.md), [Current-state diagram](04-workflow-diagram.png).

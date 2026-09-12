# Phase 1 — SCAN (Cá nhân, 20 min)

Hãy sử dụng **4 Lenses** dưới đây để quét qua hoạt động vận hành của các công ty thành viên Vingroup. Ghi lại **ít nhất 5 bài toán/bottleneck** thực tế.

### 4 Lenses tìm bài toán AI cho Vingroup:
1. **Lặp lại (Repetitive):** Tác vụ lặp đi lặp lại nhiều lần hằng ngày. (Ví dụ: So khớp hóa đơn sạc điện tại VinFast, route lại chuyến taxi tại Xanh SM).
2. **Tốn thời gian (Time-consuming):** Tác vụ ngốn thời gian xử lý thủ công của nhân viên. (Ví dụ: Soạn thảo phản hồi đánh giá 1-star của cư dân Vinhomes).
3. **AI có thể tốt hơn (AI-upgrade):** Dịch vụ khách hàng hiện tại còn chậm hoặc phản hồi rập khuôn. (Ví dụ: Chatbot CSKH Vinpearl hỗ trợ đặt vé vui chơi).
4. **Pain từ người khác (Stakeholder Pain):** Bottleneck khiến khách hàng hoặc nhân viên thực địa phàn nàn. (Ví dụ: Tài xế Xanh SM phàn nàn về việc hệ thống gợi ý điểm đón khách không chính xác).

> [!TIP]
> **AI Prompts — Partner brainstorm:**
> Hãy sử dụng prompt sau để brainstorm các bài toán thực tế nếu bạn chưa có ý tưởng:
> *"Tôi là AI Engineer tại Vin Smart Future (Vingroup). Tôi đang tìm kiếm các pain point vận hành cụ thể có thể tối ưu bằng AI cho mảng [Chọn một: VinFast / Xanh SM / Vinhomes / Vinmec]. Hãy gợi ý cho tôi 5 quy trình nghiệp vụ thủ công, tốn nhiều thời gian và gây rò rỉ hiệu suất kèm con số thống kê ước tính về tổn thất."*

### List bài toán của tôi:
| # | Subsidiary (VinFast/Xanh SM...) | Lens | Mô tả ngắn bài toán |
|---|----------------------------------|------|---------------------|
| 1 | Xanh SM | Pain từ người khác | Phân tích lý do hủy chuyến của khách hàng: Tự động nghe ghi âm cuộc gọi hủy chuyến và ghi chú của tài xế để phân loại 10 lý do phổ biến nhất gây rò rỉ cuốc. |
| 2 | Vinhomes | AI có thể tốt hơn | Trợ lý cư dân ảo hỗ trợ thủ tục hành chính: Hỗ trợ cư dân tra cứu và draft nhanh hồ sơ đăng ký thi công nội thất, đăng ký vé gửi xe hằng tháng mà không cần gặp trực tiếp ban quản lý. |
| 3 | Vinmec | Tốn thời gian | Soạn thảo tóm tắt hồ sơ xuất viện (Discharge Summary): Trích xuất thông tin lâm sàng từ bệnh án điện tử, xét nghiệm và ghi chú của bác sĩ để soạn thảo bản tóm tắt xuất viện bằng ngôn ngữ dễ hiểu cho bệnh nhân. |
| 4 | VinUni | Lặp lại | Tự động hóa chấm điểm và phản hồi bài lab: Hệ thống chấm code autograder, tự động dùng LLM để phân tích lỗi cú pháp/logic và draft phản hồi mang tính sư phạm hỗ trợ sinh viên học tập. |
| 5 | Vinpearl | Tốn thời gian | Tự động hóa kiểm tra phòng trống & Booking: Đọc email đặt phòng theo đoàn (Group Booking) phức tạp từ các công ty lữ hành để tự động kiểm tra quỹ phòng trống và draft lệnh book.|

---

# Phase 2 — QUICK-ASSESS (Cá nhân, 30 min)

Chọn **top 3 bài toán** từ danh sách trên và hoàn thiện **3 Quick Problem Cards** dưới đây (10 phút/card).

```
┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #1                                       │
│                                                             │
│ Bài toán (1 câu): Khách hàng nhấn huỷ chuyến xe Xanh SM.    │
│ Công ty thành viên: [ ] VinFast  [x] Xanh SM  [ ] Vinhomes  │
│                     [ ] Vinmec   [ ] Khác (Ghi rõ)________  │
│                                                             │
│ Ai đang đau (Actor)? Khách hàng bị ảnh hưởng lịch trình (khi|
|lí do huỷ là vì phía ứng dụng hoặc tài xế đến chậm).         |
│ Workflow thủ công hiện tại (3-5 bước):                      │
│   1. Khách hàng chọn huỷ chuyến trên ứng dụng cùng lí do huỷ|
|   2. Tài xế nhận thông báo hủy chuyến, dừng di chuyển       |
|   3. Lí do được gửi về hệ thống
|   4. Nhân viên xem xét lí do huỷ, làm việc với hệ thống và  |
|tài xế (nếu cần)                                             |
│                                                             │
│ Bước nào tốn thời gian/lỗi nhất? Phân loại lí do huỷ vì nhân|
|viên cần làm việc với lượng ||lớn thông tin từ nhiều khách hàng|
│ AI có thể nhảy vào hỗ trợ ở bước nào? Phân loại lí do, chọn |
|ra lí do quan trọng nhất cần quan tâm.                       │
│                                                             │
│ Đo thành công bằng gì (Metric có số)? Phần trăm giảm của số |
|lần huỷ chuyến từ khách hàng.                                │
│                                                             │
│ Quick Architecture: [x] No AI  [ ] Rule  [ ] LLM  [ ] Agent │
└─────────────────────────────────────────────────────────────┘
```

```
┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #2                                       │
│                                                             │
│ Bài toán (1 câu): Trợ lý cư dân ảo hỗ trợ thủ tục hành chính:|
| Hỗ trợ cư dân tra cứu và draft nhanh hồ sơ đăng ký thi công |
|nội thất, đăng ký vé gửi xe hằng tháng mà không cần gặp trực |
|tiếp ban quản lý.                                            │
│ Công ty thành viên: [ ] VinFast  [ ] Xanh SM  [x] Vinhomes  │
│                     [ ] Vinmec   [ ] Khác (Ghi rõ)________  │
│                                                             │
│ Ai đang đau (Actor)? Cư dân phải chờ thông tin được tiếp    |
|nhận và thủ tục được làm thủ công từ nhân viên quản lí       │
│                                                             │
│ Workflow thủ công hiện tại (3-5 bước):                      │
│   1. Cư dân gặp trực tiếp để thông báo với ban quản lí thủ  |
|tục cần làm                                                  |
|   2. Ban quản lí hướng dẫn cư dân về form và hồ sơ cần làm  |
|   3. Cư dần làm hồ sơ rồi gửi lại ban quản lí               |
|   4. Ban quản lý kiểm tra và xử lí hồ sơ.                   |
|   5. Bản quản lý cập nhật về kết quả xử lí hồ sơ cho cư dân │
│                                                             │
│ Bước nào tốn thời gian/lỗi nhất? Bước 3-4                   │
│ AI có thể nhảy vào hỗ trợ ở bước nào? Bước 1-4, bằng cách   |
|trả lời câu hỏi cư dân về hồ sơ cần làm trong từng trường hợp|
|cụ thể, kiểm tra những thông tin cơ bản và báo với cư dân để |
|sửa nhưng lỗi căn bản trước khi gửi lại ban quan lí để kiểm  |
|tra kỹ, giúp cư dân nộp hồ sơ lên hệ thống.                  |           
|                                                             │
│                                                             │
│ Đo thành công bằng gì (Metric có số)? Trung bình thời gian  |
|giảm trong việc xử lí của hồ sơ giảm                         │
│                                                             │
│ Quick Architecture: [ ] No AI  [ ] Rule  [ ] LLM  [x] Agent │
└─────────────────────────────────────────────────────────────┘
```

```
┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #5                                       │
│                                                             │
│ Bài toán (1 câu): Tự động hóa kiểm tra phòng trống & Booking:|
| Đọc email đặt phòng theo đoàn (Group Booking) phức tạp từ các|
| công ty lữ hành để tự động kiểm tra quỹ phòng trống và draft|
| lệnh book.                                                  │
│ Công ty thành viên: [ ] VinFast  [ ] Xanh SM  [ ] Vinhomes  │
│                     [ ] Vinmec   [ ] Khác (Ghi rõ): Vinpearl│
│                                                             │
│ Ai đang đau (Actor)? Khách hàng/Đối tác lữ hành (chờ báo giá|
│ & xác nhận lâu), Nhân viên Sales/Reservations (tốn công     │
│ bóc tách email dài, check inventory thủ công).                                       │
│                                                             │
│ Workflow thủ công hiện tại (3-5 bước):                      │
│   1. Nhận email yêu cầu Group Booking phức tạp từ đối tác   │
│   2. Nhân viên đọc & bóc tách dữ liệu (ngày, số phòng, loại │
│      phòng, dịch vụ đi kèm, yêu cầu đặc biệt)               │
│   3. Tra cứu thủ công phòng trống (PMS/Opera) & chính sách  │
│      giá theo hợp đồng từng đại lý                          │
│   4. Nhập tay thông tin để tạo lệnh đặt phòng nháp (Draft)  │
│   5. Soạn email xác nhận/báo giá gửi lại cho phía khách hàng|   │                                                             │
│ Bước nào tốn thời gian/lỗi nhất? Bước 2 & 3                 │
│ AI có thể nhảy vào hỗ trợ ở bước nào? Bước 2, 3 & 4 (Đọc    │
│ hiểu email không cấu trúc, trích xuất dữ liệu, tự động gọi  │
│ API PMS kiểm tra phòng và tạo draft booking).               │
│                                                             │
│ Đo thành công bằng gì (Metric có số)? Giảm thời gian xử lý  │
│ 1 yêu cầu Group Booking từ 30 phút ──> dưới 3 phút (tự động │
│ hóa 85% thao tác                                            |                            │                                                             │
│ Quick Architecture: [ ] No AI  [ ] Rule  [ ] LLM  [x] Agent │
└─────────────────────────────────────────────────────────────┘
```

> [!TIP]
> **AI Prompts — Stress-Test thẻ bài toán:**
> Hãy dán nội dung thẻ bài toán của bạn vào LLM để nhận phản biện:
> *"Đây là một thẻ bài toán vận hành tôi đề xuất cho Vin Smart Future: [Dán nội dung]. Hãy đóng vai trò là một CFO và Trưởng phòng Vận hành cực kỳ khắt khe, chỉ ra cho tôi 3 điểm yếu về logic, metric, và giải thích vì sao rule-based code thông thường có thể giải quyết bài toán này tốt hơn là dùng AI."*


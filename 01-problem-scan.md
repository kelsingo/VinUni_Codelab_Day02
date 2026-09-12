# 01 — Problem Scan (Cá nhân) — nguyenha59

> Deliverable cá nhân — Phase 1 (SCAN) và Phase 2 (QUICK-ASSESS) của Lab 02: AI Product Scoping (Vin Smart Future).

---

## 🏛️ Bối cảnh: Tôi là ai?

Tôi đóng vai **AI Product Engineer** tại **Vin Smart Future**, được phân công khảo sát mảng **Xanh SM (GSM)** — vận hành đội xe taxi điện thông minh. Qua trao đổi với đội điều vận (dispatcher), pain point nổi bật nhất là việc xử lý sự cố pin yếu/hết pin giữa đường của tài xế: quy trình hoàn toàn thủ công, dễ sai sót và có rủi ro an toàn giao thông nếu tư vấn sai trạm sạc.

---

# 🔍 Phase 1 — SCAN: Bảng quét cơ hội (4 Lenses)

| # | Subsidiary (VinFast/Xanh SM...) | Lens | Mô tả ngắn bài toán |
|---|----------------------------------|------|---------------------|
| 1 | **Xanh SM** | Pain từ người khác | Tài xế báo pin yếu (<10%) giữa đường; điều phối viên phải tự tra cứu vị trí GPS, tìm trạm sạc VinFast còn trụ trống phù hợp loại xe, rồi soạn tay tin nhắn chỉ đường — mất trung bình 15 phút/lượt và có rủi ro chỉ sai trạm khiến xe cạn pin giữa đường. |
| 2 | **Xanh SM** | Lặp lại | Khi khách đổi điểm đến giữa chuyến, điều phối viên phải tính lại lộ trình và thông báo thủ công cho tài xế thay vì hệ thống tự động re-route. |
| 3 | **VinFast** | Tốn thời gian | Trung tâm CSKH VinFast nhận hàng trăm mô tả lỗi xe bằng tiếng Việt tự nhiên mỗi ngày (ví dụ: "xe qua gờ giảm tốc kêu cụp cụp ở bánh trước") và phải phân loại mã lỗi kỹ thuật thủ công trước khi chuyển kỹ thuật viên. |
| 4 | **Vinhomes** | AI có thể tốt hơn | Phản ánh sự cố của cư dân (mất nước, hỏng đèn, ồn ào...) gửi qua App Vinhomes Resident hiện được phân loại và trả lời rập khuôn, chậm, không đúng ban quản lý phụ trách ngay từ đầu. |
| 5 | **Vinmec** | Tốn thời gian | Bác sĩ mất 20-30 phút/bệnh nhân để tự viết tóm tắt hồ sơ xuất viện từ dữ liệu bệnh án điện tử và kết quả xét nghiệm rời rạc. |

---

# 🃏 Phase 2 — QUICK-ASSESS: 3 Quick Problem Cards

Top 3 bài toán được chọn để đánh giá nhanh: **#1 (Xanh SM — sự cố pin), #3 (VinFast — phân loại lỗi xe), #4 (Vinhomes — phân loại phản ánh cư dân)**.

## Quick Problem Card #1 — Xanh SM: Xử lý sự cố pin yếu thực địa

```
┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #1                                        │
│                                                                │
│ Bài toán: Tài xế Xanh SM báo pin yếu/cạn giữa đường, cần      │
│ điều phối viên tư vấn trạm sạc hoặc điều xe cứu hộ pin ngay.  │
│ Công ty thành viên: [x] Xanh SM   [ ] VinFast   [ ] Vinhomes  │
│                     [ ] Vinmec    [ ] Khác________            │
│                                                                │
│ Ai đang đau (Actor)? Điều phối viên (quá tải), Tài xế (chờ)   │
│                                                                │
│ Workflow thủ công hiện tại (5 bước):                          │
│  1. Tài xế báo pin qua tổng đài ──> 2. Dispatcher tra GPS xe   │
│  ──> 3. Tra thủ công trạm sạc VinFast còn trống ──> 4. Soạn   │
│  tay tin nhắn chỉ đường gửi tài xế ──> 5. Nếu pin <5%: gọi xe │
│  cứu hộ pin di động                                           │
│                                                                │
│ Bước nào tốn thời gian/lỗi nhất? Bước 3-4 (⏱ 11 phút/lượt)    │
│ AI có thể nhảy vào hỗ trợ ở bước nào? Bước 3-4 (tự động tra    │
│ trạm sạc trống + draft tin nhắn chỉ đường)                    │
│                                                                │
│ Đo thành công bằng gì (Metric có số)?                          │
│ Giảm thời gian xử lý sự cố từ 14-17 phút ──> dưới 3 phút.     │
│                                                                │
│ Quick Architecture: [ ] No AI  [ ] Rule  [x] LLM  [ ] Agent   │
└─────────────────────────────────────────────────────────────┘
```

## Quick Problem Card #2 — VinFast: Phân loại mô tả lỗi xe bằng tiếng Việt tự nhiên

```
┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #2                                         │
│                                                                │
│ Bài toán: Khách hàng mô tả lỗi xe bằng câu tự nhiên, CSKH cần  │
│ phân loại đúng mã lỗi kỹ thuật để chuyển kỹ thuật viên đúng    │
│ chuyên môn.                                                   │
│ Công ty thành viên: [x] VinFast  [ ] Xanh SM  [ ] Vinhomes    │
│                     [ ] Vinmec   [ ] Khác________              │
│                                                                │
│ Ai đang đau (Actor)? Nhân viên CSKH tuyến 1 (Tier-1 support)  │
│                                                                │
│ Workflow thủ công hiện tại (3 bước):                          │
│  1. Khách nhắn mô tả lỗi tự nhiên ──> 2. CSKH đọc, đối chiếu   │
│  bằng kinh nghiệm với danh mục mã lỗi ──> 3. Chuyển ticket cho │
│  đúng đội kỹ thuật viên                                        │
│                                                                │
│ Bước nào tốn thời gian/lỗi nhất? Bước 2 (⏱ 5-7 phút/ticket,    │
│ tỉ lệ phân loại sai ước tính ~20%)                             │
│ AI có thể nhảy vào hỗ trợ ở bước nào? Bước 2 (gợi ý top-3 mã   │
│ lỗi khả dĩ kèm độ tin cậy, CSKH chọn/duyệt)                    │
│                                                                │
│ Đo thành công bằng gì (Metric có số)?                          │
│ 85% ticket được gợi ý đúng mã lỗi trong top-3, dưới 10 giây.  │
│                                                                │
│ Quick Architecture: [ ] No AI  [ ] Rule  [x] LLM  [ ] Agent   │
└─────────────────────────────────────────────────────────────┘
```

## Quick Problem Card #3 — Vinhomes: Phân loại & điều hướng phản ánh cư dân

```
┌─────────────────────────────────────────────────────────────┐
│ QUICK PROBLEM CARD #3                                         │
│                                                                │
│ Bài toán: Phản ánh cư dân qua App Vinhomes Resident bị phân    │
│ loại/điều hướng chậm đến sai ban quản lý phụ trách.            │
│ Công ty thành viên: [ ] VinFast  [ ] Xanh SM  [x] Vinhomes    │
│                     [ ] Vinmec   [ ] Khác________              │
│                                                                │
│ Ai đang đau (Actor)? Nhân viên trực App, cư dân (chờ phản hồi)│
│                                                                │
│ Workflow thủ công hiện tại (3 bước):                          │
│  1. Cư dân gửi phản ánh tự do ──> 2. Nhân viên đọc, gắn nhãn   │
│  và chuyển ban quản lý thủ công ──> 3. Ban quản lý xử lý       │
│                                                                │
│ Bước nào tốn thời gian/lỗi nhất? Bước 2 (⏱ trung bình 12 giờ  │
│ mới có phản hồi đầu tiên do dồn ticket)                        │
│ AI có thể nhảy vào hỗ trợ ở bước nào? Bước 2 (tự phân loại +   │
│ route đến đúng ban quản lý ngay lập tức)                       │
│                                                                │
│ Đo thành công bằng gì (Metric có số)?                          │
│ Giảm thời gian phản hồi đầu tiên từ 12 giờ ──> dưới 1 giờ.    │
│                                                                │
│ Quick Architecture: [ ] No AI  [x] Rule  [ ] LLM  [ ] Agent   │
└─────────────────────────────────────────────────────────────┘
```

---

## 🗳️ Quyết định lựa chọn cho Deep-Dive

Tôi chọn **Card #1 — Xanh SM: Xử lý sự cố pin yếu thực địa** để phát triển thành báo cáo Deep-Dive (`02-deep-dive-report.md`) và bản mẫu kỹ thuật (`starter-code/prompt_prototype.py`), vì:

* **Card #2 (VinFast — mã lỗi xe):** Cần tập dữ liệu lịch sử ticket đã gắn nhãn để đạt độ chính xác 85% — hiện chưa có sẵn, phù hợp hướng "NOT YET" hơn là làm ngay.
* **Card #3 (Vinhomes — phản ánh cư dân):** Bài toán có thể giải quyết tốt bằng **Rule-based router** (từ khóa + danh mục cố định) thay vì LLM, nên độ ưu tiên dùng AI thấp hơn.
* **Card #1** có rủi ro an toàn thực tế rõ ràng (pin cạn giữa đường), quy trình đủ hẹp và có cấu trúc để một **LLM Feature** với ranh giới vận hành nghiêm ngặt (draft-only + fallback cứu hộ) giải quyết hiệu quả ngay.

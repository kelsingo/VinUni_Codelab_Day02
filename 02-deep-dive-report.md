# Deep Dive Report — Card 2: Vinhomes

## Current-State Workflow Mapping

### Quy trình hiện tại
1. Cư dân tiếp cận ban quản lý: Cư dân gặp trực tiếp hoặc liên hệ qua kênh truyền thống để thông báo thủ tục cần thực hiện (ví dụ: đăng ký thi công nội thất, đăng ký vé gửi xe hằng tháng, cập nhật thông tin cư trú).
2. Ban quản lý cung cấp hướng dẫn thủ công: Nhân viên ban quản lý giải thích hồ sơ, form, và thời hạn cần nộp.
3. Cư dân chuẩn bị hồ sơ: Cư dân tự điền/scan hồ sơ rồi gửi lại cho ban quản lý.
4. Kiểm tra sơ bộ và chỉnh sửa: Ban quản lý kiểm tra tính đầy đủ của hồ sơ và yêu cầu cư dân bổ sung nếu thiếu thông tin.
5. Phê duyệt và cập nhật kết quả: Sau khi hồ sơ hợp lệ, ban quản lý xử lý, xác nhận và thông báo kết quả cho cư dân.

### Bottleneck và Handoff
- Bottleneck chính: Bước 3–4, nơi cư dân phải trực tiếp chuẩn bị hồ sơ và ban quản lý phải kiểm tra lại nhiều lần để phát hiện thiếu thông tin cơ bản.
- Handoff quan trọng: Từ cư dân sang ban quản lý và từ ban quản lý sang hệ thống lưu trữ hồ sơ. Mỗi handoff đều có nguy cơ sai lệch thông tin, chậm trễ, và tốn thời gian xác minh lặp lại.
- Thời gian vận hành trung bình: ước tính khoảng 30–45 phút/lượt cho các trường hợp đơn giản, và có thể lên đến 1–2 giờ nếu hồ sơ cần nhiều chỉnh sửa hoặc có nghiệp vụ đặc thù.

### Điểm nghẽn rõ nhất
- Cư dân không nắm rõ các loại hồ sơ nào cần nộp, form nào bắt buộc, và thông tin nào cần cập nhật.
- Ban quản lý phải lặp lại cùng một câu hỏi chung nhiều lần cho các hồ sơ tương tự.
- Sự chậm trễ chủ yếu không đến từ sai lầm kỹ thuật, mà từ thiếu thông tin ban đầu và phân công thủ công.

---

## Problem Statement (6-field)

| Field | Nội dung |
|---|---|
| 1. Actor / Operator | Cư dân Vinhomes và nhân viên ban quản lý khu dân cư. |
| 2. Current Workflow | Cư dân gửi yêu cầu thủ tục bằng cách gặp trực tiếp hoặc liên hệ thủ công; ban quản lý hướng dẫn hồ sơ, cư dân nộp hồ sơ, rồi ban quản lý kiểm tra, yêu cầu bổ sung và phê duyệt. |
| 3. Bottleneck | Bước chuẩn bị hồ sơ và xác minh sơ bộ là chậm nhất vì cư dân không biết giấy tờ cần bổ sung, còn ban quản lý phải rà soát lại nhiều thông tin thủ công. |
| 4. Business Impact | Tăng thời gian xử lý hồ sơ, làm giảm trải nghiệm cư dân, gia tăng khối lượng công việc cho nhân sự quản lý, và gây backlog trong các ngày cao điểm. |
| 5. Success Metric | Giảm thời gian xử lý trung bình từ 35–45 phút xuống dưới 10 phút cho các hồ sơ có cấu trúc đơn giản; giảm tỷ lệ hồ sơ trả lại do thiếu thông tin từ 30% xuống dưới 10%; tăng tỷ lệ hồ sơ hoàn thành đúng lần đầu. |
| 6. Operational Boundary | AI được phép: trả lời hướng dẫn tổng quát, kiểm tra tính đầy đủ của hồ sơ, gợi ý thông tin còn thiếu, hợp thức hóa các mẫu câu trả lời, và chuẩn bị bản draft cho ban quản lý xem xét. AI không được phép: tự ý phê duyệt/không phê duyệt hồ sơ, thay đổi quyền lợi tài sản, hay quyết định ngoại lệ theo dõi riêng lẻ mà không có con người xác nhận. |

---

## Future-State Flow & AI Fit

### AI Fit Matrix
- Nhóm phù hợp: Agentic Loop
- Lý do: Quy trình này gồm nhiều bước tuần tự (trả lời, trích xuất thông tin, kiểm tra hồ sơ, sinh draft, và chuyển cho human review), nên cần cả rule validation lẫn khả năng hiểu ngôn ngữ tự do của LLM, đồng thời có thể tự động hóa phần hành động lặp lại nhưng giữ HITL ở điểm rủi ro cao.

### Future-State Flow
1. Cư dân nhập yêu cầu qua chat/portal/website.
2. AI phân loại loại thủ tục (ví dụ: đăng ký thi công, gửi xe, cập nhật cư trú).
3. AI kiểm tra thông tin cơ bản và báo ngay cho cư dân các hồ sơ/giấy tờ còn thiếu.
4. AI sinh draft hồ sơ / thông tin cần điền theo mẫu chuẩn của Vinhomes.
5. HITL — ban quản lý review các trường hợp rủi ro, ngoại lệ, hoặc hồ sơ chưa đủ điều kiện.
6. Fallback: nếu AI không chắc chắn, không đủ dữ liệu, hoặc phát hiện thông tin mâu thuẫn, hệ thống chuyển sang luồng thủ công có nhân sự tiếp nhận trực tiếp.

### AI Step / Human Step / Fallback
- AI Step: Phân loại yêu cầu, gợi ý hồ sơ cần nộp, kiểm tra tính đầy đủ, và draft phản hồi ban đầu.
- Human Step (HITL): Ban quản lý kiểm tra trường hợp đặc biệt, chốt quyết định phê duyệt, và xử lý các ngoại lệ vượt quá quy chuẩn.
- Fallback: Khi mất ngữ cảnh, thiếu dữ liệu đầu vào, hoặc hồ sơ có tính riêng biệt cao, hệ thống yêu cầu nhân viên hỗ trợ trực tiếp.

---

## Decision Quality

### Kết luận đề xuất
GO — Bắt đầu Prototype với scope hẹp (HITL bắt buộc).

### Chứng cứ đề xuất
- Bài toán có đầu vào rõ ràng, định dạng dữ liệu tương đối chuẩn hóa, và đầu ra có thể đo lường.
- Vinhomes có nhiều tình huống lặp lại, nhưng độ rủi ro của quyết định vẫn nằm ở mức vừa phải nếu có người review trước khi gửi tiếp.
- Nếu AI chỉ làm phần giảm công việc thủ công (tra cứu, gợi ý hồ sơ, draft phản hồi) thay vì tự phê duyệt, rủi ro nghiệp vụ sẽ nằm trong tầm kiểm soát.
- Metric kinh doanh rõ ràng: giảm thời gian xử lý, giảm số lần trả hồ sơ do thiếu thông tin, nâng trải nghiệm cư dân.

### Scope khuyến nghị
- Phase 1: hỗ trợ các thủ tục có mẫu chuẩn và ít ngoại lệ (đăng ký gửi xe, cập nhật thông tin cư dân cơ bản, hỏi thông tin quy trình).
- Phase 2: mở rộng cho các nghiệp vụ có nhiều biến thể hơn cần review cộng đồng/chủ đầu tư.

---

## Quick Summary

Nếu chọn làm AI cho Vinhomes, giải pháp tốt nhất không phải là AI tự xử lý hoàn toàn, mà là:
- AI giúp cư dân chuẩn bị hồ sơ tốt hơn
- AI giúp ban quản lý giảm công việc lặp lại
- Human review vẫn giữ quyền quyết định cuối cùng

Điều này phù hợp với triết lý của Vin Smart Future: dùng AI để tăng hiệu suất vận hành, không thay thế hoàn vị con người ở các điểm có rủi ro nghiệp vụ.

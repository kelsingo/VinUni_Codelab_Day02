# 03 — AI Interaction Log & Reflection — nguyenha59

> Deliverable — Phase 6 (REFLECTION) của Lab 02: AI Product Scoping (Vin Smart Future).
> Công cụ AI sử dụng: **Claude (Claude Code)**, đóng vai trò thought-partner trong suốt buổi lab.

---

## 1. AI đã giúp tôi những gì?

* **Soạn thảo và siết chặt System Prompt:** Tôi mô tả 2 ranh giới vận hành mong muốn (tag `[DRAFT_ONLY]` bắt buộc và ngưỡng pin nguy hiểm <5% → điều xe cứu hộ). Claude giúp diễn đạt lại thành chỉ thị hệ thống rõ ràng, tách bạch từng RULE, kèm ví dụ định dạng JSON cụ thể — điều mà nếu tự viết tôi dễ viết mơ hồ, dẫn đến model có thể lách luật.
* **Viết code `evaluate_prompt()` và bộ test đối kháng:** Claude hoàn thiện phần gọi API và giúp tôi hình dung 3 kịch bản tấn công thực tế (ép model bỏ qua bước duyệt vì "khách VIP đang vội", ép model chỉ đường xa dù pin cực thấp, và một kiểu prompt-injection yêu cầu model "quên" toàn bộ system prompt/đổi persona) để kiểm chứng ranh giới có đứng vững không — đúng yêu cầu tối thiểu 3 adversarial prompts của đề bài, ban đầu tôi chỉ mới có 2.
* **Migrate SDK giữa buổi:** Ban đầu file starter dùng Google Gemini SDK (`google-genai`/`google-generativeai`). Khi tôi đổi sang dùng OpenAI, Claude đã: đổi toàn bộ `evaluate_prompt()` sang `openai.OpenAI().chat.completions.create(...)`, đổi biến môi trường từ `GEMINI_API_KEY`/`GOOGLE_API_KEY` sang `OPENAI_API_KEY`, cập nhật `requirements.txt`, và tự cài đặt + chạy thử để xác nhận cả 3 test case vẫn pass với model mới (`gpt-4o-mini`).
* **Cấu trúc hoá báo cáo `.md`:** Claude đọc kỹ `README.md` và `01-worksheet.md` để đảm bảo 3 file báo cáo (`01-problem-scan.md`, `02-deep-dive-report.md`, `03-ai-log.md`) bám đúng khung 6-field, đúng rubric chấm điểm, thay vì tôi phải tự dò lại từng mục trong worksheet.

## 2. AI đã sai/hallucinate ở đâu, và tôi đã sửa thế nào?

* **Chưa hỏi rõ hệ điều hành/shell trước khi đưa lệnh:** Khi tôi báo lỗi thiếu `OPENAI_API_KEY`, log cho thấy tôi đang chạy trên Windows CMD (`C:\Users\...>`), nhưng hướng dẫn ban đầu trong code/README lại dùng cú pháp `export` của bash — không chạy được trên CMD/PowerShell. Tôi phải yêu cầu Claude chỉ rõ lệnh tương ứng (`set KEY=value` cho CMD, `$env:KEY="value"` cho PowerShell) thay vì áp dụng máy móc lệnh Unix.
* **Lỗi encoding không liên quan bị bỏ qua ban đầu:** Khi chạy thử script lần đầu trên PowerShell mặc định (code page cp1252), Python bị `UnicodeEncodeError` vì icon emoji (`🚀`) trong `print()`. Đây là lỗi có sẵn từ code gốc, không phải do phần chuyển đổi Gemini→OpenAI gây ra. Tôi và Claude thống nhất **không sửa** phần này ngay (ngoài phạm vi yêu cầu), chỉ dùng `PYTHONIOENCODING=utf-8` để test tạm — tránh việc AI "tự ý mở rộng phạm vi sửa" khi không được yêu cầu.
* **Rủi ro "diagnostics giả":** Sau vài lần sửa file, trình soạn thảo báo lại các cảnh báo Pylance cũ (dòng số đã lệch so với thực tế) như thể vẫn còn lỗi import Gemini — thực chất là cache chưa refresh. Bài học: không nên tin tuyệt đối vào cảnh báo tool ngay sau khi sửa, mà phải đọc lại file thực tế để xác nhận trước khi kết luận.
* **Bỏ sót yêu cầu "tối thiểu 3 adversarial test cases":** Ở vòng làm việc đầu, cả tôi và Claude chỉ tập trung đổi SDK Gemini→OpenAI mà không đối chiếu lại `01-worksheet.md` Phase 4, nên `prompt_prototype.py` chỉ có 2 test case thay vì tối thiểu 3 theo đề bài. Lỗi này chỉ lộ ra khi tôi chủ động hỏi "đã đúng yêu cầu bài chưa" và yêu cầu rà soát lại — cho thấy AI (và cả tôi) có xu hướng tin bài đã "chạy được, output đẹp" là xong, mà quên đối chiếu ngược lại checklist gốc của đề bài. Đã bổ sung Test Case 3 (prompt-injection đổi persona) và chạy lại xác nhận pass.

## 3. Tôi đã sửa prompt/ranh giới ra sao để đạt kết quả chuẩn?

* Ban đầu SYSTEM_PROMPT chỉ nói chung chung "phải cẩn thận với pin yếu" — không đủ cụ thể để model tuân thủ nhất quán. Tôi yêu cầu Claude viết lại thành **ranh giới có ngưỡng số rõ ràng** (< 5% pin, > 5km khoảng cách) và **định dạng output bắt buộc** (JSON key cố định `action`/`reason`), giúp việc chấm pass/fail bằng code (assertion) trở nên khách quan thay vì đọc cảm tính.
* Đặt `temperature=0.0` để giảm tối đa việc model trả lời ngẫu nhiên khác nhau giữa các lần chạy — quan trọng với một tính năng an toàn cần tính nhất quán cao.
* Thiết kế 3 test đối kháng theo đúng "áp lực thực tế" mà một tài xế/dispatcher có thể tạo ra (viện lý do khẩn cấp, xin bỏ bước duyệt, giả vờ đổi persona AI) thay vì test bằng câu hỏi trực diện dễ đoán — giúp ranh giới được kiểm chứng sát với tình huống vận hành thật hơn.

---

## Kết luận cá nhân

AI (Claude) hiệu quả nhất khi đóng vai trò biên tập/stress-test cho các quyết định tôi đã đưa ra (ranh giới, ngưỡng số, kiến trúc), chứ không phải tự quyết định thay tôi. Điểm cần tôi tự kiểm soát nhiều nhất là: (1) môi trường thực thi cụ thể (OS, shell, SDK phiên bản) — AI không tự đoán đúng nếu tôi không cung cấp ngữ cảnh; (2) phạm vi thay đổi — nhắc AI chỉ sửa đúng phần được yêu cầu, không lan sang sửa các lỗi không liên quan.

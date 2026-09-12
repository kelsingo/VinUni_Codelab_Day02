# 03 — AI Interaction Log & Reflection — nguyenha59

> Deliverable — Phase 6 (REFLECTION) của Lab 02: AI Product Scoping (Vin Smart Future).

---

Trong buổi lab này tôi dùng một trợ lý AI lập trình như một cộng sự đồng hành (thought-partner) xuyên suốt quá trình làm bài, từ lúc siết lại ranh giới an toàn cho tới lúc rà soát bản nộp cuối cùng.

## AI đã hỗ trợ tôi ở đâu

Phần tôi cần AI hỗ trợ nhiều nhất là **diễn đạt ranh giới vận hành thành chỉ thị hệ thống đủ chặt chẽ**. Tôi đã hình dung sẵn hai ranh giới cần có — tin nháp phải có tag `[DRAFT_ONLY]`, và pin dưới 5% thì không được chỉ đường xa mà phải gọi cứu hộ — nhưng khi tự viết thành văn bản, tôi thấy câu chữ của mình vẫn còn mơ hồ, thiếu ngưỡng số cụ thể, dễ để model lách luật. Với sự hỗ trợ của AI, tôi diễn đạt lại thành từng RULE tách bạch, kèm ví dụ định dạng JSON cụ thể (`action`, `reason`), giúp việc chấm đúng/sai sau này khách quan hơn.

Phần thứ hai là **thiết kế các tình huống thử thách ranh giới**. Tôi cần ít nhất 3 kịch bản "tấn công" thực tế mà một tài xế hoặc dispatcher có thể tạo ra trong lúc gấp gáp. AI giúp tôi hình dung đa dạng kịch bản hơn: ép model bỏ qua bước duyệt vì lý do khẩn cấp, ép model chỉ đường xa dù pin cực thấp, và một kịch bản khó hơn là yêu cầu model "quên hết luật cũ, đổi vai thành một AI không ràng buộc" — kiểu tấn công prompt-injection. Tôi trực tiếp viết code gọi API, chạy thử, và đọc kết quả trả về để tự đánh giá ranh giới có đứng vững không.

Phần thứ ba là khi tôi quyết định đổi nhà cung cấp mô hình đang dùng trong file mẫu sang OpenAI. AI hỗ trợ tôi đối chiếu sự khác biệt giữa hai SDK (cách gọi API, cấu trúc dữ liệu trả về, tên biến môi trường) để tôi chỉnh lại code cho đúng, sau đó tôi tự cài thư viện và chạy lại toàn bộ để xác nhận cả 3 test case vẫn cho kết quả đúng.

## Những chỗ AI trả lời chưa đúng hoặc chưa đủ, và cách tôi sửa

Có vài điểm tôi phải tự phát hiện và yêu cầu điều chỉnh lại:

Đầu tiên là lệnh thiết lập biến môi trường. Khi tôi báo lỗi thiếu API key, gợi ý đưa ra ban đầu chỉ dùng cú pháp `export` của bash — trong khi tôi đang chạy trên Windows CMD nên lệnh đó không hoạt động. Tôi phải yêu cầu chỉ rõ lại lệnh tương ứng cho từng shell (CMD dùng `set`, PowerShell dùng `$env:`) thay vì áp dụng máy móc một cú pháp duy nhất.

Thứ hai, ở lần chạy thử đầu tiên trên PowerShell mặc định, chương trình bị lỗi encoding vì ký tự emoji trong câu lệnh in ra màn hình không tương thích với bảng mã mặc định của terminal. Đây là lỗi có sẵn từ file gốc chứ không liên quan đến phần tôi đang chỉnh sửa, nên tôi chủ động quyết định không sửa luôn phần đó để tránh mở rộng phạm vi ngoài yêu cầu, chỉ dùng một biến môi trường tạm thời để test cho qua.

Thứ ba, và là chỗ tôi thấy cần rút kinh nghiệm nhất: ở vòng làm việc đầu tiên, tôi và AI chỉ tập trung vào việc đổi SDK cho chạy được, mà quên đối chiếu lại yêu cầu gốc của đề bài là phải có **tối thiểu 3** kịch bản tấn công — lúc đó tôi mới chỉ có 2. Lỗi này chỉ lộ ra khi tôi chủ động dừng lại, tự hỏi "bài đã đúng yêu cầu chưa" và yêu cầu rà soát lại toàn bộ so với đề bài gốc, thay vì tin rằng "chạy được, kết quả đẹp" nghĩa là đã xong. Sau đó tôi bổ sung thêm kịch bản tấn công thứ ba (prompt-injection đổi persona) và chạy lại để xác nhận vẫn pass.

## Tôi đã điều chỉnh prompt và ranh giới như thế nào để đạt kết quả chuẩn

So với bản nháp đầu tiên chỉ nói chung chung "phải cẩn thận với pin yếu", tôi đã sửa lại theo ba hướng cụ thể: (1) gắn ngưỡng số rõ ràng cho từng ranh giới (dưới 5% pin, quá 5km khoảng cách) thay vì mô tả cảm tính; (2) ép buộc định dạng output cố định (JSON với key `action`/`reason`) để có thể chấm điểm tự động bằng code thay vì đọc cảm tính; (3) đặt `temperature = 0` để giảm tối đa việc model trả lời khác nhau giữa các lần chạy, vì đây là một tính năng liên quan an toàn nên cần độ nhất quán cao. Tôi cũng cố tình thiết kế các câu lệnh tấn công theo đúng kiểu áp lực thực tế (viện lý do khẩn cấp, xin bỏ bước duyệt, giả vờ đổi vai AI) thay vì hỏi thẳng, để phép thử sát với tình huống vận hành thật hơn.

## Kết luận cá nhân

AI phát huy tác dụng tốt nhất khi đóng vai trò biên tập và stress-test lại các quyết định mà tôi đã đưa ra (ranh giới, ngưỡng số, kiến trúc), chứ không phải tự quyết định thay tôi. Hai điều tôi rút ra để tự kiểm soát tốt hơn trong những lần sau: một là phải cung cấp đủ ngữ cảnh về môi trường thực thi cụ thể (hệ điều hành, shell, phiên bản thư viện) vì AI không tự đoán đúng nếu thiếu thông tin; hai là phải chủ động đối chiếu lại kết quả với yêu cầu gốc của đề bài thay vì chỉ tin vào việc "chạy ra kết quả đẹp".

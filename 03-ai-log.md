# 03. AI Log & Reflection

## Mục tiêu sử dụng AI

Tôi dùng AI như một thought-partner để brainstorm các bottleneck vận hành trong hệ sinh thái Vingroup, sau đó dùng AI để phản biện metric, ranh giới và lựa chọn kiến trúc. AI giúp mở rộng danh sách ý tưởng nhanh hơn, nhưng không được xem là nguồn xác nhận số liệu vận hành.

## AI đã giúp gì?

1. Gợi ý các tác vụ lặp lại trong điều vận Xanh SM, CSKH Vinhomes và tài chính VinFast.
2. Chuyển ý tưởng thô thành problem card có Actor, workflow, bottleneck và metric.
3. Đặt câu hỏi phản biện: bài toán có thật sự cần LLM không, lỗi sai gây hậu quả gì, và bước nào phải có người duyệt.
4. Gợi ý adversarial inputs để kiểm tra việc người dùng cố tình yêu cầu bỏ qua `[DRAFT_ONLY]` hoặc đề xuất trạm quá xa khi pin thấp.

## AI có thể sai ở đâu?

- AI có thể bịa số liệu như số sự cố mỗi ngày, thời gian xử lý hoặc phần trăm doanh thu bị ảnh hưởng.
- AI có thể đề xuất dùng agent cho một quy trình thực chất chỉ cần rule-based filtering.
- AI có thể viết một hướng dẫn nghe hợp lý nhưng không có dữ liệu GPS, trạng thái trạm hoặc loại cổng sạc để chứng minh.
- AI có thể tuân theo yêu cầu mới nhất của người dùng và quên ranh giới an toàn nếu system prompt không đủ rõ.

## Tôi đã sửa prompt và ranh giới như thế nào?

- Ghi rõ vai trò: dispatcher co-pilot, không phải hệ thống tự vận hành.
- Quy định output luôn bắt đầu bằng `[DRAFT_ONLY]` và cấm gửi trực tiếp.
- Đưa quy tắc pin dưới 5% thành điều kiện cứng: không chọn trạm xa hơn 5 km, trả về hành động `dispatch_mobile_charger`.
- Yêu cầu không đoán khi thiếu dữ liệu; phải fallback cho con người.
- Tách rule safety khỏi phần LLM tạo ngôn ngữ, vì ranh giới khoảng cách và pin cần kiểm tra có tính quyết định.

## Bài học cá nhân

AI hữu ích nhất khi đóng vai trò phản biện có cấu trúc, không phải người quyết định thay nhóm. Một prototype tốt cần metric đo được, boundary cụ thể, HITL và fallback. Trong bước tiếp theo, nhóm phải thay các con số giả định bằng log thật và kiểm thử shadow mode trước khi cho phép tích hợp vào quy trình vận hành.

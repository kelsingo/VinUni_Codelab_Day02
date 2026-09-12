# 01. Problem Scan & Quick Cards

## Bối cảnh

Nhóm chọn bối cảnh vận hành xe điện Xanh SM và tập trung vào những tác vụ có tần suất cao, nhiều handoff và cần con người phê duyệt trước khi gửi thông tin cho tài xế.

## Phase 1 - Scan

| # | Công ty | Lens | Bài toán vận hành |
|---|---|---|---|
| 1 | Xanh SM | Tốn thời gian | Điều phối viên xử lý sự cố pin giữa đường bằng cách tra GPS, tìm trạm còn chỗ và soạn hướng dẫn thủ công. |
| 2 | Xanh SM | Pain từ người khác | Phân loại lý do khách hủy chuyến từ ghi âm cuộc gọi và ghi chú của tài xế để tìm lỗi lặp lại. |
| 3 | VinFast | Lặp lại | Đối chiếu dữ liệu sạc từ nhiều trạm đối tác với hóa đơn hàng tuần. |
| 4 | Vinhomes | AI-upgrade | Phân loại khiếu nại cư dân và chuyển đến đúng ban quản lý/tòa nhà. |
| 5 | Vinmec | Tốn thời gian | Soạn bản nháp tóm tắt xuất viện từ bệnh án, kết quả xét nghiệm và ghi chú bác sĩ. |
| 6 | Vinpearl | Pain từ người khác | Phát hiện review có vấn đề nghiêm trọng và chuyển cảnh báo cho quản lý khách sạn. |

## Phase 2 - Quick Problem Cards

### Card 1 - Xanh SM: Xử lý sự cố pin giữa đường

- **Actor:** Tài xế, điều phối viên trung tâm vận hành.
- **Workflow hiện tại:** Tài xế gọi báo sự cố -> điều phối viên ghi nhận biển số/vị trí/pin -> tra bản đồ -> tìm trạm tương thích -> soạn và gửi hướng dẫn -> gọi cứu hộ nếu cần.
- **Bottleneck:** Tra cứu trạm và soạn hướng dẫn, khoảng 10 phút trong tổng 15 phút/lượt.
- **AI hỗ trợ:** Lấy dữ liệu đã có, xếp hạng trạm phù hợp và tạo tin nhắn dạng nháp.
- **Metric:** Giảm thời gian xử lý từ 15 phút xuống dưới 3 phút; đạt ít nhất 98% hướng dẫn đúng loại xe/trạm.
- **Quick architecture:** LLM feature kết hợp rule-based safety checks.

### Card 2 - Vinhomes: Phân loại phản ánh cư dân

- **Actor:** Nhân viên CSKH và ban quản lý tòa nhà.
- **Workflow hiện tại:** Cư dân gửi phản ánh -> CSKH đọc và gắn nhãn -> tìm ban phụ trách -> chuyển ticket -> theo dõi SLA.
- **Bottleneck:** Đọc, hiểu và route ticket thủ công, khoảng 6 phút/ticket.
- **AI hỗ trợ:** Phân loại chủ đề, mức độ khẩn cấp và đề xuất nơi nhận; nhân viên vẫn duyệt.
- **Metric:** 90% ticket được route trong 30 giây; giảm lỗi route xuống dưới 3%.
- **Quick architecture:** LLM classifier có danh mục nhãn cố định.

### Card 3 - VinFast: Đối chiếu hóa đơn sạc

- **Actor:** Nhân viên tài chính và vận hành trạm.
- **Workflow hiện tại:** Tải log sạc -> chuẩn hóa mã giao dịch -> đối chiếu hóa đơn -> tìm lệch -> gửi yêu cầu xác minh.
- **Bottleneck:** Mã giao dịch và định dạng dữ liệu không đồng nhất, khoảng 20 phút/lô.
- **AI hỗ trợ:** Chuẩn hóa mô tả và giải thích các dòng lệch; không tự duyệt thanh toán.
- **Metric:** 95% giao dịch được ghép tự động; giảm thời gian rà soát 40%.
- **Quick architecture:** Rule-based matching trước, LLM chỉ hỗ trợ các trường hợp mơ hồ.

## Lựa chọn để Deep-Dive

Nhóm chọn **Card 1 - Xanh SM xử lý sự cố pin giữa đường** vì có tác động thời gian thực, metric đo được và ranh giới an toàn có thể kiểm chứng bằng test adversarial. AI chỉ tạo draft; điều phối viên vẫn là người duyệt và gửi.

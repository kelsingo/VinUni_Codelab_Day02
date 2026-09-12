> **Phạm vi nộp:** Bài cá nhân
> **Người thực hiện / branch:** `ntthduong`

# Hướng dẫn kiểm tra trước khi push

Chưa có commit hoặc push. Metadata nhóm chỉ cần được trưởng nhóm bổ sung ở bản tổng hợp trên `main`.

## Deliverables

- `01-problem-scan.md`: 6 cơ hội, 3 quick cards, phản biện và lựa chọn.
- `02-deep-dive-report.md`: workflow, 6-field statement, metrics, AI fit, HITL/fallback và quyết định.
- `03-ai-log.md`: prompts, điểm AI sai/chưa đủ, cách sửa và kết quả live.
- `04-workflow-diagram.png`: current-state flow, handoff, thời gian và bottleneck.
- `starter-code/prompt_prototype.py`: Gemini API + 5 adversarial cases + 5 controls.
- `prompt-test-results.json`: raw live batch evidence (9 pass, 1 HTTP 429), không chứa key.
- `b5-retest.json`: raw retest riêng của B5 (pass), giữ riêng để không sửa lịch sử lần đầu.
- `prompt-test-results-3.5-lite.json`: suite 10/10 đạt cấu trúc nhưng review phát hiện A2 dùng sai thương hiệu; bằng chứng trước khi sửa.
- `prompt-test-results-final.json`: kết quả cuối sau khi thêm brand boundary, 10/10 passed.
- `prompt-test-results-3.6-final.json`: suite mở rộng model mặc định `gemini-3.6-flash` (8 pass, 2 HTTP 429).

## Chạy lại

```powershell
python -m venv .venv
.venv\Scripts\python.exe -m pip install -r requirements.txt
$env:GEMINI_API_KEY="YOUR_ROTATED_KEY"
.venv\Scripts\python.exe starter-code/prompt_prototype.py --extended --workers 1 --report prompt-test-results.json
.venv\Scripts\python.exe -m pytest -q
.venv\Scripts\python.exe autograder/autograder.py
```

Chạy riêng case control nếu gặp rate limit:

```powershell
.venv\Scripts\python.exe starter-code/prompt_prototype.py --extended --case B5 --workers 1
```

## Tiêu chí duyệt thủ công

1. Không coi số giả định là số liệu Xanh SM đã xác nhận.
2. JSON critical chỉ là đề xuất chờ người duyệt; code không có công cụ thực thi.
3. Đọc raw draft để phát hiện bịa dữ kiện; test cấu trúc không thay review ngữ nghĩa.
4. Xác nhận quyết định `NOT YET` cho pilot là phù hợp với nhóm.
5. Rotate key từng được gửi trong chat; tuyệt đối không thêm `.env` hoặc key vào Git.

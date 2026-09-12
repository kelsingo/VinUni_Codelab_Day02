"""Generate 04-workflow-diagram.png. Requires Pillow.

Phạm vi nộp: Bài cá nhân
Người thực hiện / branch: ntthduong
"""
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "04-workflow-diagram.png"
FONT_DIR = Path("C:/Windows/Fonts")


def font(size, bold=False):
    name = "seguisb.ttf" if bold else "segoeui.ttf"
    return ImageFont.truetype(str(FONT_DIR / name), size)


def centered(draw, box, text, text_font, fill="#102a43", spacing=8):
    left, top, right, bottom = box
    bounds = draw.multiline_textbbox((0, 0), text, font=text_font, spacing=spacing, align="center")
    width, height = bounds[2] - bounds[0], bounds[3] - bounds[1]
    draw.multiline_text(((left + right - width) / 2, (top + bottom - height) / 2), text,
                        font=text_font, fill=fill, spacing=spacing, align="center")


image = Image.new("RGB", (2000, 1200), "#f4f7f5")
draw = ImageDraw.Draw(image)

draw.rectangle((0, 0, 2000, 160), fill="#063c35")
draw.text((80, 30), "CURRENT-STATE WORKFLOW", font=font(46, True), fill="#ffffff")
draw.text((80, 92), "Xanh SM — xử lý sự cố pin thực địa (giả định scoping)", font=font(27), fill="#b7eee2")
draw.text((1420, 47), "BÀI NỘP CÁ NHÂN", font=font(22, True), fill="#ffffff")
draw.text((1420, 91), "Người thực hiện / branch: ntthduong", font=font(19), fill="#d4f5ed")

boxes = [
    (60, 290, 340, 595, "01", "Nhận cuộc gọi\nsự cố", "Tài xế → Dispatcher\nĐiện thoại / ticket", "2 phút", False),
    (455, 290, 735, 595, "02", "Xác minh pin,\nGPS, loại xe", "Dispatcher +\nFleet dashboard", "2 phút", False),
    (850, 290, 1130, 595, "03", "Tra cứu trạm /\nđội sạc di động", "Dispatcher +\nStation dashboard", "5 phút", True),
    (1245, 290, 1525, 595, "04", "Soạn và kiểm tra\nphương án", "Dispatcher +\nSOP / app", "5 phút", True),
    (1640, 290, 1920, 595, "05", "Liên hệ và\nxác nhận", "Dispatcher →\nTài xế / đội hỗ trợ", "1 phút", False),
]

for left, top, right, bottom, number, title, actor, duration, bottleneck in boxes:
    shadow = (left + 8, top + 10, right + 8, bottom + 10)
    draw.rounded_rectangle(shadow, radius=22, fill="#d9e3df")
    fill = "#fff1eb" if bottleneck else "#ffffff"
    outline = "#d9482f" if bottleneck else "#4c786f"
    draw.rounded_rectangle((left, top, right, bottom), radius=22, fill=fill, outline=outline, width=5)
    draw.ellipse((left + 20, top + 18, left + 75, top + 73), fill=outline)
    centered(draw, (left + 20, top + 18, left + 75, top + 73), number, font(22, True), "#ffffff")
    centered(draw, (left + 22, top + 85, right - 22, top + 182), title, font(27, True))
    centered(draw, (left + 22, top + 185, right - 22, top + 250), actor, font(20), "#486581")
    centered(draw, (left + 22, bottom - 55, right - 22, bottom - 10), duration, font(23, True), outline)
    if bottleneck:
        draw.rounded_rectangle((right - 160, top + 18, right - 18, top + 57), radius=12, fill="#d9482f")
        centered(draw, (right - 160, top + 18, right - 18, top + 57), "BOTTLENECK", font(15, True), "#ffffff")

for index in range(4):
    _, _, right, _, *_ = boxes[index]
    next_left = boxes[index + 1][0]
    y = 442
    draw.line((right + 18, y, next_left - 28, y), fill="#157a6e", width=7)
    draw.polygon([(next_left - 28, y - 13), (next_left - 4, y), (next_left - 28, y + 13)], fill="#157a6e")
    handoff = ["H1\nThông tin sự cố", "H2\nTelemetry/GPS", "H3\nKhả dụng", "H4\nPhương án duyệt"][index]
    centered(draw, (right + 10, 350, next_left - 5, 425), handoff, font(16, True), "#157a6e", 2)

draw.rounded_rectangle((80, 700, 1920, 930), radius=24, fill="#e4f4f0", outline="#157a6e", width=3)
draw.text((125, 735), "QUY TẮC RẼ NHÁNH SAU XÁC MINH", font=font(27, True), fill="#063c35")
draw.text((125, 795), "Pin < 5%  →  không hướng dẫn trạm > 5km; đề xuất sạc di động, chờ dispatcher duyệt", font=font(23), fill="#223f3a")
draw.text((125, 842), "Pin ≥ 5%  →  chỉ xem xét trạm đã xác minh; thiếu/mâu thuẫn dữ liệu → gọi lại và dùng fallback thủ công", font=font(23), fill="#223f3a")
draw.text((125, 889), "Ngoài scope 15 phút: thời gian gọi lại và thời gian đội hỗ trợ đến hiện trường.", font=font(20), fill="#486581")

draw.rounded_rectangle((80, 975, 1920, 1125), radius=22, fill="#102a43")
draw.text((125, 1007), "TỔNG THỜI GIAN GIẢ ĐỊNH", font=font(22, True), fill="#9fe4d6")
draw.text((125, 1050), "15 phút/lượt", font=font(38, True), fill="#ffffff")
draw.text((520, 1033), "Bottleneck bước 3 + 4 = 10 phút (66,7%)", font=font(28, True), fill="#ffb7a8")
draw.text((1295, 1040), "Cần đo baseline thực tế trước pilot", font=font(22), fill="#d8e4ee")

image.save(OUT, optimize=True)
print(OUT)

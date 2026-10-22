"""Build the v2 continuity frames, shot boards, contact sheet, and animatic inputs.

The generated art in 原始三帧图 is retained verbatim. This script only separates
panels and adds deterministic labels/layout for review.
"""

from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageOps

ROOT = Path(__file__).resolve().parent
RAW = ROOT / "原始三帧图"
FRAMES = ROOT / "30张连续关键帧"
BOARDS = ROOT / "逐镜三帧板"
VIDEO = ROOT / "预览视频帧"
for folder in (FRAMES, BOARDS, VIDEO):
    folder.mkdir(exist_ok=True)

FONT_PATH = r"C:\Windows\Fonts\msyh.ttc"
FONT = ImageFont.truetype(FONT_PATH, 36)
SMALL = ImageFont.truetype(FONT_PATH, 25)
TINY = ImageFont.truetype(FONT_PATH, 20)

SHOTS = [
    ("SH001", 1.5, "冰爪踩雪", "冰爪下落 / 前齿入雪 / 承重压实"),
    ("SH002", 1.5, "手抓岩点", "手入画 / 触到岩棱 / 握紧发力"),
    ("SH003", 3.0, "陡坡攀登", "坡下 / 跨步 / 抬头"),
    ("SH004", 2.5, "抬头呼吸", "低头 / 抬眼 / 呼气"),
    ("SH005", 2.0, "视线落向拉链", "望峰 / 转眼 / 低头"),
    ("SH006", 2.5, "迎风调整衣领", "停步迎风 / 伸手 / 拉至胸口"),
    ("SH007", 1.5, "拉链到领口", "胸口 / 快速拉合 / 继续向上"),
    ("SH008", 3.5, "近景脊线", "贴近脊线 / 前移 / 深入"),
    ("SH009", 3.5, "山体尺度", "见主峰 / 后拉 / 山群全貌"),
    ("SH010", 3.5, "终景人物", "踏上山脊 / 站稳 / 望向三峰"),
]


def panel_crop(img: Image.Image, shot: str, index: int) -> Image.Image:
    w, h = img.size
    a, b = round(index * w / 3), round((index + 1) * w / 3)
    return img.crop((a + (5 if index else 0), 0, b - (5 if index < 2 else 0), h))


def contain(img: Image.Image, box: tuple[int, int]) -> Image.Image:
    return ImageOps.contain(img.convert("RGB"), box, Image.Resampling.LANCZOS)


def draw_centered(canvas: Image.Image, img: Image.Image, x: int, y: int, box: tuple[int, int]) -> None:
    fitted = contain(img, box)
    canvas.paste(fitted, (x + (box[0] - fitted.width) // 2, y + (box[1] - fitted.height) // 2))


time_cursor = 0.0
concat_lines = ["ffconcat version 1.0"]
overview = Image.new("RGB", (2400, 5 * 690), "#0c1218")
for shot_index, (shot, duration, title, action) in enumerate(SHOTS):
    strip = Image.open(RAW / f"{shot}.png").convert("RGB")
    panels = [panel_crop(strip, shot, i) for i in range(3)]
    labels = ("START 起始", "KEY 关键", "OUT 出镜")

    board = Image.new("RGB", (1920, 1080), "#0c1218")
    d = ImageDraw.Draw(board)
    d.text((64, 38), f"{shot}  {title}", font=FONT, fill="white")
    d.text((64, 95), f"{time_cursor:04.1f}—{time_cursor + duration:04.1f}s    {action}", font=SMALL, fill="#a8bac6")

    for i, img in enumerate(panels):
        out = FRAMES / f"{shot}_{i + 1:02d}_{['START', 'KEY', 'OUT'][i]}.png"
        img.save(out, optimize=True)

        x = 64 + i * 604
        d.rectangle((x, 188, x + 574, 923), outline="#52636c", width=2)
        draw_centered(board, img, x + 2, 190, (570, 731))
        d.text((x, 944), labels[i], font=SMALL, fill="#e9f1f4")

        # 25-second timed, clean 16:9 review frame; source crop remains separate.
        vf = Image.new("RGB", (1920, 1080), "#0c1218")
        draw_centered(vf, img, 0, 0, (1920, 1080))
        seq = shot_index * 3 + i + 1
        frame_path = VIDEO / f"{seq:04d}.png"
        vf.save(frame_path, optimize=True)
        concat_lines.append(f"file '{frame_path.as_posix()}'")
        concat_lines.append(f"duration {duration / 3:.6f}")

    d.text((64, 1010), "连续动作示意图  |  生成式静帧，非实拍逐帧", font=TINY, fill="#79909d")
    board_path = BOARDS / f"{shot}.png"
    board.save(board_path, optimize=True)
    thumb = contain(board, (1180, 640))
    ox = (shot_index % 2) * 1200 + 10
    oy = (shot_index // 2) * 690 + 10
    overview.paste(thumb, (ox, oy))
    time_cursor += duration

overview.save(ROOT / "00_十镜三帧总览.png", optimize=True)
concat_lines.append(f"file '{(VIDEO / '0030.png').as_posix()}'")
(ROOT / "预览帧清单.ffconcat").write_text("\n".join(concat_lines) + "\n", encoding="utf-8")
print(f"Built {len(SHOTS) * 3} keyframes, {len(SHOTS)} shot boards, total {time_cursor}s")

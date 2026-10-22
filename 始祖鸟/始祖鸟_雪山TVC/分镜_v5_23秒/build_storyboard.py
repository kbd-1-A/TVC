"""Build the v5 continuity frames, shot boards, contact sheet, and animatic inputs.

The generated art in 原始画面 is retained verbatim. This script only separates
panels and adds deterministic labels/layout for review.
"""

from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageOps

ROOT = Path(__file__).resolve().parent
RAW = ROOT / "原始画面"
FRAMES = ROOT / "25张顺序关键帧"
BOARDS = ROOT / "逐镜分镜板"
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
    ("SH003", 4.0, "陡坡攀登", "坡下 / 跨步 / 抬头"),
    ("SH004", 2.5, "抬头呼吸", "低头 / 抬眼 / 呼气"),
    ("SH005", 2.5, "视线落向拉链", "望峰 / 转眼 / 低头"),
    ("SH006", 1.5, "顺手拉合衣领", "低头接手 / 一次上拉 / 到顶"),
    ("SH007", 1.0, "脊线匹配切", "拉链到顶 / 一张脊线 / 切远景"),
    ("SH008", 3.5, "路线揭示", "贴近山脊 / 后拉见来路 / 人物缩成蓝点"),
    ("SH009", 5.0, "最后一步", "迈上脊顶 / 承重站稳 / 抬头望向三峰"),
]


def panel_crop(img: Image.Image, shot: str, index: int) -> Image.Image:
    w, h = img.size
    a, b = round(index * w / 3), round((index + 1) * w / 3)
    if shot == "SH008":
        # SH008 START is the exact same image as SH007 MATCH; keep every edge pixel.
        return img.crop((a, 0, b, h))
    return img.crop((a + (5 if index else 0), 0, b - (5 if index < 2 else 0), h))


def contain(img: Image.Image, box: tuple[int, int]) -> Image.Image:
    return ImageOps.contain(img.convert("RGB"), box, Image.Resampling.LANCZOS)


def draw_centered(canvas: Image.Image, img: Image.Image, x: int, y: int, box: tuple[int, int]) -> None:
    fitted = contain(img, box)
    canvas.paste(fitted, (x + (box[0] - fitted.width) // 2, y + (box[1] - fitted.height) // 2))


time_cursor = 0.0
seq = 0
concat_lines = ["ffconcat version 1.0"]
overview = Image.new("RGB", (2400, ((len(SHOTS) + 1) // 2) * 690), "#0c1218")
for shot_index, (shot, duration, title, action) in enumerate(SHOTS):
    strip = Image.open(RAW / f"{shot}.png").convert("RGB")
    panels = [strip] if shot == "SH007" else [panel_crop(strip, shot, i) for i in range(3)]
    labels = ("START 起始", "KEY 关键", "OUT 出镜")

    board = Image.new("RGB", (1920, 1080), "#0c1218")
    d = ImageDraw.Draw(board)
    d.text((64, 38), f"{shot}  {title}", font=FONT, fill="white")
    d.text((64, 95), f"{time_cursor:04.1f}—{time_cursor + duration:04.1f}s    {action}", font=SMALL, fill="#a8bac6")

    if len(panels) == 1:
        d.rectangle((64, 163, 1856, 965), outline="#52636c", width=2)
        draw_centered(board, panels[0], 66, 165, (1788, 798))
        d.text((64, 982), "ONE FRAME  转场画面", font=SMALL, fill="#e9f1f4")

    for i, img in enumerate(panels):
        suffix = "MATCH" if len(panels) == 1 else ["START", "KEY", "OUT"][i]
        out = FRAMES / f"{shot}_{i + 1:02d}_{suffix}.png"
        img.save(out, optimize=True)

        if len(panels) == 3:
            x = 64 + i * 604
            d.rectangle((x, 188, x + 574, 923), outline="#52636c", width=2)
            draw_centered(board, img, x + 2, 190, (570, 731))
            d.text((x, 944), labels[i], font=SMALL, fill="#e9f1f4")

        # Timed 16:9 review frame; source crop remains separate.
        vf = Image.new("RGB", (1920, 1080), "#0c1218")
        draw_centered(vf, img, 0, 0, (1920, 1080))
        seq += 1
        frame_path = VIDEO / f"{seq:04d}.png"
        vf.save(frame_path, optimize=True)
        concat_lines.append(f"file '{frame_path.as_posix()}'")
        # SH008 repeats SH007 exactly at START. Show that shared anchor briefly
        # in the static animatic so it does not look like a two-second freeze.
        frame_duration = ([0.125, 1.625, 1.75][i] if shot == "SH008" else duration / len(panels))
        concat_lines.append(f"duration {frame_duration:.6f}")

    d.text((64, 1010), "连续动作示意图  |  生成式静帧，非实拍逐帧", font=TINY, fill="#79909d")
    board_path = BOARDS / f"{shot}.png"
    board.save(board_path, optimize=True)
    thumb = contain(board, (1180, 640))
    ox = (shot_index % 2) * 1200 + 10
    oy = (shot_index // 2) * 690 + 10
    overview.paste(thumb, (ox, oy))
    time_cursor += duration

overview.save(ROOT / "00_九镜转场总览.png", optimize=True)
concat_lines.append(f"file '{(VIDEO / f'{seq:04d}.png').as_posix()}'")
(ROOT / "预览帧清单.ffconcat").write_text("\n".join(concat_lines) + "\n", encoding="utf-8")
print(f"Built {seq} keyframes, {len(SHOTS)} shot boards, total {time_cursor}s")

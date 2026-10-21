"""Render a 30-second concept animatic from generated keyframes."""

from __future__ import annotations

import math
import subprocess
import wave
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageOps


ROOT = Path(__file__).resolve().parent
IMAGES = ROOT / "images"
OUT = ROOT / "地形裁片_30秒概念样片_v2.mp4"
AUDIO = ROOT / "ambient.wav"
WIDTH, HEIGHT, FPS, DURATION = 960, 540, 24, 30

PATHS = [
    IMAGES / "01_地形.png",
    IMAGES / "02_衣服裁片.png",
    IMAGES / "03_人物入野.png",
    IMAGES / "04_登上山脊.png",
    IMAGES / "05_片尾产品.png",
    IMAGES / "06_山线衣线同框.png",
]
SOURCES = [Image.open(path).convert("RGB") for path in PATHS]
SOURCES[1] = ImageOps.mirror(SOURCES[1])

# start, end, source, zoom start/end, x center start/end, y center start/end
SHOTS = [
    (0, 3, 0, 1.55, 1.36, 0.44, 0.49, 0.58, 0.55),
    (3, 6, 0, 1.35, 1.16, 0.49, 0.58, 0.55, 0.50),
    (6, 9, 1, 1.25, 1.12, 0.47, 0.53, 0.53, 0.50),
    (9, 13, 2, 1.09, 1.02, 0.46, 0.50, 0.50, 0.50),
    (13, 17, 2, 1.15, 1.07, 0.38, 0.48, 0.53, 0.50),
    (17, 21, 1, 1.18, 1.04, 0.50, 0.57, 0.51, 0.49),
    (21, 24, 3, 1.06, 1.00, 0.47, 0.50, 0.49, 0.50),
    (24, 27, 5, 1.09, 1.02, 0.48, 0.50, 0.50, 0.50),
    (27, 30, 4, 1.03, 1.10, 0.48, 0.48, 0.50, 0.50),
]


def smooth(x: float) -> float:
    return x * x * (3 - 2 * x)


def frame_for(shot: tuple, t: float) -> Image.Image:
    start, end, idx, z0, z1, x0, x1, y0, y1 = shot
    u = smooth(min(1.0, max(0.0, (t - start) / (end - start))))
    zoom = z0 + (z1 - z0) * u
    cx, cy = x0 + (x1 - x0) * u, y0 + (y1 - y0) * u
    image = SOURCES[idx]
    iw, ih = image.size
    target_ratio = WIDTH / HEIGHT
    if iw / ih > target_ratio:
        base_h = ih
        base_w = ih * target_ratio
    else:
        base_w = iw
        base_h = iw / target_ratio
    crop_w, crop_h = base_w / zoom, base_h / zoom
    left = max(0, min(iw - crop_w, iw * cx - crop_w / 2))
    top = max(0, min(ih - crop_h, ih * cy - crop_h / 2))
    frame = image.crop((round(left), round(top), round(left + crop_w), round(top + crop_h)))
    return frame.resize((WIDTH, HEIGHT), Image.Resampling.BICUBIC)


def make_audio() -> None:
    sr = 48000
    n = DURATION * sr
    rng = np.random.default_rng(20261021)
    freqs = np.fft.rfftfreq(n, 1 / sr)
    spectrum = np.fft.rfft(rng.normal(size=n))
    spectrum *= 1 / (1 + (freqs / 180) ** 2)
    wind = np.fft.irfft(spectrum, n=n)
    wind /= max(np.max(np.abs(wind)), 1e-9)
    t = np.arange(n) / sr
    gust = 0.65 + 0.18 * np.sin(2 * np.pi * 0.11 * t) + 0.12 * np.sin(2 * np.pi * 0.037 * t)
    drone = 0.05 * np.sin(2 * np.pi * 67 * t) + 0.025 * np.sin(2 * np.pi * 101 * t)
    rise = np.clip((t - 3) / 15, 0, 1)
    sound = 0.28 * wind * gust + drone * rise
    for step_time in (13.8, 15.7, 17.4, 19.1):
        s = int(step_time * sr)
        length = int(0.18 * sr)
        pulse = rng.normal(size=length)
        pulse = np.convolve(pulse, np.ones(80) / 80, mode="same")
        pulse *= np.exp(-np.linspace(0, 8, length))
        sound[s : s + length] += pulse * 0.35
    sound *= np.minimum(1, t / 0.5) * np.minimum(1, (DURATION - t) / 1.2)
    sound = np.clip(sound, -1, 1)
    pcm = (sound * 32767).astype("<i2")
    stereo = np.repeat(pcm[:, None], 2, axis=1)
    with wave.open(str(AUDIO), "wb") as wav:
        wav.setnchannels(2)
        wav.setsampwidth(2)
        wav.setframerate(sr)
        wav.writeframes(stereo.tobytes())


def render() -> None:
    make_audio()
    font_path = "C:/Windows/Fonts/msyh.ttc"
    title_font = ImageFont.truetype(font_path, 34)
    sub_font = ImageFont.truetype(font_path, 15)
    proc = subprocess.Popen(
        [
            "ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24",
            "-s", f"{WIDTH}x{HEIGHT}", "-r", str(FPS), "-i", "-", "-i", str(AUDIO),
            "-c:v", "libx264", "-preset", "veryfast", "-crf", "20", "-pix_fmt", "yuv420p",
            "-c:a", "aac", "-b:a", "160k", "-shortest", str(OUT),
        ],
        stdin=subprocess.PIPE,
    )
    assert proc.stdin is not None
    for number in range(DURATION * FPS):
        t = number / FPS
        shot = next(shot for shot in SHOTS if shot[0] <= t < shot[1])
        frame = frame_for(shot, t)
        if t >= 27.5:
            opacity = min(1, (t - 27.5) / 0.7)
            overlay = Image.new("RGB", (WIDTH, HEIGHT), (11, 14, 18))
            frame = Image.blend(frame, overlay, 0.20 * opacity)
            draw = ImageDraw.Draw(frame)
            x, y = 575, 370
            draw.text((x, y), "地形裁片", fill=(245, 245, 242), font=title_font)
            draw.text((x + 2, y + 55), "30 秒概念动态预演  ·  服装为占位外观", fill=(221, 223, 221), font=sub_font)
        proc.stdin.write(frame.tobytes())
    proc.stdin.close()
    code = proc.wait()
    if code != 0:
        raise RuntimeError(f"ffmpeg failed with exit code {code}")
    print(OUT)


if __name__ == "__main__":
    render()

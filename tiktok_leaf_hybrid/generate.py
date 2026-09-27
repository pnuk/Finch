"""Generate shots 2-4 with Veo (Gemini API) and assemble the final vertical TikTok video.

Needs GEMINI_API_KEY in the environment. Run: python3 generate.py
"""
import base64
import json
import os
import re
import subprocess
import sys
import time
import urllib.error
import urllib.request

import imageio_ffmpeg
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
KEY = os.environ.get("GEMINI_API_KEY")
MODEL = os.environ.get("VEO_MODEL", "veo-3.1-generate-preview")
BASE = "https://generativelanguage.googleapis.com/v1beta"
FF = imageio_ffmpeg.get_ffmpeg_exe()
NEG = "cartoon, CGI look, distorted logos, extra wheels, warped hands, text overlay, watermark"


def prompt(n):
    md = open(os.path.join(HERE, "PROMPTS.md"), encoding="utf-8").read()
    return re.search(rf"## Shot {n}.*?```\n(.*?)```", md, re.S).group(1).strip()


SHOTS = [
    ("02_mowing.mp4", prompt(2), "frame_robot.jpg"),
    ("03_handheld.mp4", prompt(3), "frame_vacuum.jpg"),
    ("04_hybrid.mp4", prompt(4), None),
]


def call(url, body=None):
    req = urllib.request.Request(url, headers={"x-goog-api-key": KEY, "Content-Type": "application/json"},
                                 data=json.dumps(body).encode() if body else None)
    try:
        with urllib.request.urlopen(req, timeout=120) as r:
            return json.loads(r.read())
    except urllib.error.HTTPError as e:
        sys.exit(f"HTTP {e.code} from {url.split('?')[0]}: {e.read().decode()[:1000]}")


def generate(out, text, frame):
    path = os.path.join(HERE, out)
    if os.path.exists(path):
        print("skip (exists):", out)
        return
    inst = {"prompt": text}
    params = {"aspectRatio": "9:16", "durationSeconds": 8, "negativePrompt": NEG}
    if frame:
        data = base64.b64encode(open(os.path.join(HERE, frame), "rb").read()).decode()
        inst["image"] = {"bytesBase64Encoded": data, "mimeType": "image/jpeg"}
        params["personGeneration"] = "allow_adult"
    op = call(f"{BASE}/models/{MODEL}:predictLongRunning", {"instances": [inst], "parameters": params})
    print("started", out, op["name"])
    while not op.get("done"):
        time.sleep(15)
        op = call(f"{BASE}/{op['name']}")
    if "error" in op:
        sys.exit(f"{out}: {op['error']}")
    samples = op["response"]["generateVideoResponse"].get("generatedSamples")
    if not samples:
        sys.exit(f"{out}: no video returned (possibly filtered): {json.dumps(op['response'])[:500]}")
    uri = samples[0]["video"]["uri"]
    req = urllib.request.Request(uri, headers={"x-goog-api-key": KEY})
    with urllib.request.urlopen(req, timeout=300) as r, open(path, "wb") as f:
        f.write(r.read())
    print("saved", out)


def caption_png():
    im = Image.new("RGBA", (1080, 1920), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    f = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 88)
    t = "HYBRID MODE: ON"
    d.text(((1080 - d.textlength(t, font=f)) / 2, 220), t, font=f, fill=(255, 210, 0),
           stroke_width=6, stroke_fill="black")
    p = os.path.join(HERE, "cap_hybrid.png")
    im.save(p)
    return p


def assemble():
    clips = ["01_title.mp4"] + [s[0] for s in SHOTS]
    args, fl = [], []
    for i, c in enumerate(clips):
        args += ["-i", os.path.join(HERE, c)]
    args += ["-f", "lavfi", "-t", "3.5", "-i", "anullsrc=r=48000:cl=stereo", "-loop", "1", "-i", caption_png()]
    sil, cap = len(clips), len(clips) + 1
    for i in range(len(clips)):
        v = f"[{i}:v]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,fps=30,setsar=1"
        fl.append(v + (f"[v{i}pre];[v{i}pre][{cap}:v]overlay=enable='gte(t,1.5)':shortest=1[v{i}]"
                       if i == len(clips) - 1 else f"[v{i}]"))
        a = f"[{sil}:a]" if i == 0 else f"[{i}:a]"
        fl.append(f"{a}aresample=48000,aformat=channel_layouts=stereo[a{i}]")
    fl.append("".join(f"[v{i}][a{i}]" for i in range(len(clips))) + f"concat=n={len(clips)}:v=1:a=1[v][a]")
    out = os.path.join(HERE, "leaf_hybrid_tiktok.mp4")
    subprocess.run([FF, "-y", "-loglevel", "error", *args, "-filter_complex", ";".join(fl), "-map", "[v]",
                    "-map", "[a]", "-c:v", "libx264", "-crf", "20", "-pix_fmt", "yuv420p", "-c:a", "aac",
                    "-movflags", "+faststart", out], check=True)
    print("final:", out)


if __name__ == "__main__":
    if not KEY:
        sys.exit("Set GEMINI_API_KEY first")
    for s in SHOTS:
        generate(*s)
    assemble()

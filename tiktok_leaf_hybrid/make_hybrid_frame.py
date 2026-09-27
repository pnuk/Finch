"""Create the first frame for shot 4: edit the real photo so the leaf vacuum is strapped onto the robot mower.

Needs GEMINI_API_KEY. Writes frame_hybrid.jpg.
"""
import base64
import json
import os
import sys
import urllib.error
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
MODEL = os.environ.get("IMAGE_MODEL", "gemini-3-pro-image")
PHOTO = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, "source_photo.jpg")

PROMPT = (
    "Edit this real photo of my garden. Take the teal-and-black Makita cordless leaf vacuum that lies on the "
    "lawn and mount it on the roof of the dark grey Husqvarna robotic lawn mower, firmly fastened with black "
    "ratchet straps and a bit of silver duct tape, like a homemade garden hack. The long black vacuum tube "
    "points forward and down, its nozzle just above the fallen leaves in front of the robot; the grey "
    "collection bag hangs on the side of the robot. Keep the exact same robot mower, the same vacuum, the "
    "same garden, lawn, leaves, shrubs and lighting, photorealistic smartphone photo. Vertical 9:16 framing "
    "centered on the robot with the vacuum on top. No people, no text, no phone frame."
)

img = base64.b64encode(open(PHOTO, "rb").read()).decode()
body = {
    "contents": [{"parts": [{"text": PROMPT}, {"inlineData": {"mimeType": "image/jpeg", "data": img}}]}],
    "generationConfig": {"responseModalities": ["IMAGE"], "imageConfig": {"aspectRatio": "9:16"}},
}
req = urllib.request.Request(
    f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent",
    data=json.dumps(body).encode(),
    headers={"x-goog-api-key": os.environ["GEMINI_API_KEY"], "Content-Type": "application/json"},
)
try:
    resp = json.loads(urllib.request.urlopen(req, timeout=300).read())
except urllib.error.HTTPError as e:
    sys.exit(f"HTTP {e.code}: {e.read().decode()[:1000]}")
for part in resp["candidates"][0]["content"]["parts"]:
    if "inlineData" in part:
        out = os.path.join(HERE, "frame_hybrid.jpg")
        open(out, "wb").write(base64.b64decode(part["inlineData"]["data"]))
        print("saved", out, part["inlineData"]["mimeType"])
        break
else:
    sys.exit("no image returned: " + json.dumps(resp)[:800])

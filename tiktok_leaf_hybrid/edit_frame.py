"""Edit an image with a Gemini image model.

Usage: GEMINI_API_KEY=... python3 edit_frame.py <input.jpg> <output.jpg> "<edit instruction>"
"""
import base64
import json
import os
import sys
import urllib.error
import urllib.request

MODEL = os.environ.get("IMAGE_MODEL", "gemini-3-pro-image")
src, out, prompt = sys.argv[1:4]

body = {
    "contents": [{"parts": [{"text": prompt},
                            {"inlineData": {"mimeType": "image/jpeg",
                                            "data": base64.b64encode(open(src, "rb").read()).decode()}}]}],
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
        open(out, "wb").write(base64.b64decode(part["inlineData"]["data"]))
        print("saved", out)
        break
else:
    sys.exit("no image returned: " + json.dumps(resp)[:800])

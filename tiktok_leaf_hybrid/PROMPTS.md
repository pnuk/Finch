# TikTok prank: "The Best Leaf Cleanup Solution"

Vertical 9:16, ~26 s total. 4 shots:

| # | Shot | Length | Source |
|---|------|--------|--------|
| 1 | Title card: "THE BEST LEAF CLEANUP SOLUTION" / "Robot mower + leaf vacuum = HYBRID" | 3.5 s | `01_title.mp4` (already rendered from the photo) |
| 2 | Robot mower mowing the lawn | 8 s | Veo, image-to-video from `frame_robot.jpg` |
| 3 | Person vacuuming leaves with the handheld leaf vacuum | 8 s | Veo, first+last frame: `frame_hand_start.jpg` → `frame_hand_end.jpg` (edited with `edit_frame.py`) |
| 4 | Robot mower drives around with the leaf vacuum strapped on its roof, sucking up leaves | 8 s | Veo, first+last frame: `frame_hybrid.jpg` → `frame_hybrid_end.jpg` (edited with Gemini image model) |

Model: `veo-3.1-generate-preview`, aspectRatio `9:16`, durationSeconds `8`.

---

## Shot 2 — robot mowing (image-to-video, first frame = `frame_robot.jpg`)

```
Vertical smartphone video, handheld but steady, natural overcast autumn daylight.
The dark grey robotic lawn mower in this garden starts moving and slowly drives
across the green lawn toward the camera, mowing the grass in a straight line,
then gently turns. A few yellow autumn leaves lie on the grass; the mower drives
past them and leaves them untouched. Realistic motion, real garden, no people.
Sound: quiet electric motor hum, soft grass cutting, birds in the background.
No text, no music, no subtitles.
```

## Shot 3 — person with leaf vacuum (first frame = `frame_hand_start.jpg`, last frame = `frame_hand_end.jpg`)

```
Vertical smartphone video, natural overcast autumn daylight, same garden.
A person holds the teal cordless leaf VACUUM (suction mode, NOT a blower)
with the nozzle of the black tube just above the pile of autumn leaves. The
vacuum pulls the leaves IN: leaves lift off the grass, fly toward the nozzle
and disappear inside the tube, one after another, the pile gets smaller and
smaller. The air flows INTO the tube. Nothing comes out of the tube; no leaves
are blown away or scattered. The grey collection bag inflates and fills up
with leaves until the grass under the nozzle is clean. Only arm and hand
visible. Realistic, handheld phone footage.
Sound: loud vacuum motor, leaves rustling and being sucked into the tube.
No text, no music, no subtitles.
```

## Shot 4 — the "hybrid" (first frame = `frame_hybrid.jpg`, last frame = `frame_hybrid_end.jpg`)

```
Vertical smartphone video, natural overcast autumn daylight, same garden.
The robotic lawn mower CARRIES the teal leaf vacuum strapped on its roof and
DRIVES around the lawn on its own for the whole 8 seconds: its wheels turn, it
rolls forward across the grass, makes a smooth wide turn and arrives at the
final position closer to the camera. The vacuum rides on top of the moving
robot, wobbling slightly with the bumps. The vacuum is in suction mode, NOT a
blower: leaves on the grass in front of the moving tube lift off and are pulled
INTO the nozzle and disappear inside; nothing comes out of the tube and no
leaves are blown away. Behind the robot it leaves a clean stripe of green
grass, and the grey bag gets fuller. Camera is steady, slightly panning to
follow. Comedic, deadpan homemade garden hack filmed on a phone. No people.
Sound: robot mower motor and wheels on grass plus a loud vacuum whirr.
No text, no music, no subtitles, no phone frame or borders.
```

Negative prompt (all shots): `leaf blower, leaves blown out of the tube, leaves flying away, phone frame, black borders, push lawn mower, cartoon, CGI look, distorted logos, extra wheels, warped hands, text overlay, watermark`

---

TikTok caption idea: `Work smarter, not harder 🍂🤖 #robotmower #leafcleanup #gardenhack #husqvarna #makita #lifehack`

# TikTok prank: "The Best Leaf Cleanup Solution"

Vertical 9:16, ~26 s total. 4 shots:

| # | Shot | Length | Source |
|---|------|--------|--------|
| 1 | Title card: "THE BEST LEAF CLEANUP SOLUTION" / "Robot mower + leaf vacuum = HYBRID" | 3.5 s | `01_title.mp4` (already rendered from the photo) |
| 2 | Robot mower mowing the lawn | 8 s | Veo, image-to-video from `frame_robot.jpg` |
| 3 | Person vacuuming leaves with the handheld leaf vacuum | 8 s | Veo, image-to-video from `frame_vacuum.jpg` |
| 4 | Robot mower drives around with the leaf vacuum strapped on its roof, sucking up leaves | 8 s | Veo, image-to-video from `frame_hybrid.jpg` (photo edited with Gemini image model) |

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

## Shot 3 — person with leaf vacuum (image-to-video, first frame = `frame_vacuum.jpg`)

```
Vertical smartphone video, natural overcast autumn daylight, same garden.
An adult's hands pick up the teal-and-black cordless leaf vacuum lying on the
lawn, put the shoulder strap on, and start vacuuming fallen yellow and brown
leaves from the grass. The leaves get sucked into the black tube one after
another and the grey collection bag slowly fills up. Only hands, arms and torso
are visible, no face. Realistic, slightly tired body language.
Sound: loud whirring leaf vacuum motor, leaves rustling and being sucked in.
No text, no music, no subtitles.
```

## Shot 4 — the "hybrid" (image-to-video, first frame = `frame_hybrid.jpg`, made by `make_hybrid_frame.py`)

```
Vertical smartphone video, natural overcast autumn daylight, same garden.
The robotic lawn mower with the teal leaf vacuum strapped on its roof starts
driving slowly and confidently forward across the lawn. The leaf vacuum is
running: the fallen yellow and brown leaves in front of the black tube get
sucked into the nozzle one after another, the grey collection bag puffs up.
The robot makes a neat slow turn and keeps going. Camera stays steady and
follows it a little. Comedic, deadpan, looks like a real homemade garden hack
filmed by the owner on a phone. No people.
Sound: robot mower hum plus a loud leaf vacuum whirr, leaves being sucked in.
No text, no music, no subtitles, no phone frame or borders.
```

Negative prompt (all shots): `cartoon, CGI look, distorted logos, extra wheels, warped hands, text overlay, watermark`

---

TikTok caption idea: `Work smarter, not harder 🍂🤖 #robotmower #leafcleanup #gardenhack #husqvarna #makita #lifehack`

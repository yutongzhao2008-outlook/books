# Video Storyboard and Narration: Optimizing On-Device Slot Filling

Script: `4_video_explainer.py` (Manim, 3b1b style).
Render: `manim -pql 4_video_explainer.py MobileSlotFillingOptimization`

| Scene | On screen | Narration (short sentences) |
|---|---|---|
| 1 | Title and subtitle | Slot filling on a phone can be fast. Here is how. |
| 2 | Three costs | One turn has three costs. We read the prompt. We write the output. We load the model. |
| 3 | Fixed prefix turns gray | The fixed prefix is cached. The phone reads only the new words. |
| 4 | JSON with a red cap line | The output is short. Cap it at 64 tokens. Use temperature 0. |
| 5 | Six levers appear | Use a smaller model. Keep the prompt short. Keep the context small. Keep the server warm. Match threads to fast cores. Let code handle dates. |
| 6 | Loop: Measure, Change, Check | Measure first. Change one lever. Check accuracy. Undo if accuracy falls. |
| 7 | Closing line | Measure. Change one thing. Keep what passes. |

Notes:
- The animation does not show real numbers. Real latency and memory must come from a test on the target phone.
- Render the video only after the script runs in your Manim environment. This script was not rendered during authoring.

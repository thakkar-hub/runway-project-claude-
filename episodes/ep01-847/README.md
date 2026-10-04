# EPISODE 01 — "8:47"

Series open. 15.0 sec, 7 shots, 9:16 (720:1280).

| File | What it is |
|---|---|
| `RUNWAY_GUIDE.md` | **Step-by-step: make this episode in the Runway web app** |
| `breakdown.md` | Pre-production breakdown, shot list, post notes, Ep 02 handoff |
| `shots.json` | Per-shot generation prompts (style block appended at render time) |
| `../../render.py` | Runway render script (reads `shots.json`) |

## Render

```bash
export RUNWAYML_API_SECRET=...           # your Runway key
cp /path/to/sasha.jpg reference/sasha.jpg
python3 render.py episodes/ep01-847      # all shots
python3 render.py episodes/ep01-847 S04a S06   # specific takes
```

Clips land in `episodes/ep01-847/renders/`. Each take is generated at 5 s and
trimmed in the edit to the timings in `breakdown.md`.

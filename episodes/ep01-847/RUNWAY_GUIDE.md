# How to make Episode 01 "8:47" in Runway

You'll make 10 short clips in Runway (shot 04 is four quick takes), then cut them together into a 15-second 9:16 video in an editor like CapCut, Premiere or DaVinci. The phone texts (8:47 AM, K., the message) are added in the editor, not by Runway.

Runway's interface and model names change often. If a button below isn't where I say, look for the closest equivalent: "image with references" and "image to video" are the two tools that matter.

---

## 0. Before you start (5 min)

1. **Get the files.** From this repo, download:
   - `reference/sasha.jpg`, her face. Use this one, not the full sheet, because the sheet's labels and "SOCIAL SALSAA" branding leak into the shots.
   - This guide. All the prompts are below.
2. **Make a project** in Runway called `EP01 – 8:47`, so every generation stays in one place.
3. **Settings to use everywhere:** aspect ratio **9:16** (720×1280), duration **5 s**. For tests, use the cheaper/faster model (e.g. Gen-4 Turbo). For finals, use the best Gen model on your plan.

## 1. Lock Sasha first (10 min)

1. Open Runway's **image generation with References** (Gen-4 References / "Image" → add reference).
2. Upload `sasha.jpg` and save it as a reference named **Sasha**. Then you can type `@Sasha` in any prompt.
3. Test it with: `@Sasha sitting on the edge of a bed in a small Mumbai bedroom, morning light, faded grey oversized tee, hair in a messy claw-clip bun.`
4. Compare it with the reference sheet: the eye shape, brows, nose, hairline and jaw. If it doesn't look like the same actress, regenerate. Don't move on until this test looks right.

## 2. Make a still frame for every shot (the important step)

For **each shot below**, paste the Step A prompt into image-with-references, with `@Sasha` attached.
- Make 2 to 4 options and pick the best one.
- **Reject** any option with waxy skin, a different face, extra fingers, a warped phone, a too-perfect "Pinterest" room, or glam makeup.
- The phone screen can be blank or gibberish. You'll cover it in the edit.
- **Do the bathroom first.** Approve **S04a**, then add that still as a second reference (`@Bathroom`) for S04b–S07, so the mirror, tumbler and tap match across shots.
- **Check the kajal:** it's under her **left** eye. When the camera faces her directly (S01–S03), it's on the **right** of the frame. In the mirror shots (S04, S06, S07), the camera is behind her, so the reflection shows it on the **left** of the frame. Reject any take where it's under both eyes or under the wrong eye.

Before you spend credits on video, put all 10 approved stills side by side. If one face drifts from the others, redo that still now. It's much cheaper than redoing a video.

## 3. Turn each still into video

For each shot:
1. Open **image to video** and upload the approved still as the **first frame**.
2. Paste the **Step B** prompt. It's short and describes motion only, because the still already defines how she and the room look.
3. Set 9:16 and 5 s, then generate. Expect **2 to 3 takes per shot**.
4. **Reject** takes with face morphing, floating camera, slow motion, weightless movement or objects melting.
5. If a shot keeps failing, simplify it rather than accepting artifacts. For example, in S03 split the stumble and the clothes-flinging into two takes.

## 4. Dialogue

There are only two lines on camera, and both are easy to hide:
- **S02, "Shit."** We're behind her shoulder and barely see her mouth, so just lay the voice over the clip.
- **S06, "Yeah… I don't really have an option."** Record the line yourself, or have a voice actor do it. If her mouth visibly doesn't match, use Runway's lip-sync / performance tool (e.g. Act-Two: record yourself saying the line on your phone and use it to drive the shot). Otherwise, cut so her mouth is soft or turned away.
- **Caller (K.):** record it calm and unhurried, then apply a "phone" EQ (cut the lows and highs). It starts over S05 ("We're on for—") and finishes in S06 ("—today?").

## 5. Edit (in CapCut, Premiere or DaVinci)

**Timeline, 9:16, 15.0 s:**

| Time | Shot | Trim to |
|---|---|---|
| 0.0–2.5 | S01 | 2.5 s |
| 2.5–4.0 | S02 | 1.5 s |
| 4.0–6.0 | S03 | 2.0 s |
| 6.0–9.0 | S04a → b → c → d | 0.8 / 0.75 / 0.75 / 0.7 s, hard cuts with no transitions |
| 9.0–9.8 | S05 | 0.8 s |
| 9.8–13.0 | S06 | 3.2 s |
| 13.0–15.0 | S07 | 2.0 s, hard cut to black on her unsettled reflection |

**Phone screens.** Add a text layer pinned to the phone screen, and use motion tracking if the phone moves. Use a plain system font (SF Pro / Inter / Roboto), with only this text on screen:
- S02: `8:47 AM`, big, as a lock screen.
- S05: `K.`, as an incoming-call screen.
- S07: `Whatever happens, don't tell them.`, as a message banner. Keep it readable for at least 1.2 s.

**Sound layers:**
- Phone vibration on wood, then silence at the start of S02.
- Ceiling fan hum and a distant Mumbai horn.
- Bare feet on tile, the sheet dragging, hangers and the cupboard door banging (S03).
- Toothbrush scrub, running tap from S04a **to the very last frame**, and a fabric snap.
- Ringtone (S05), the phone-filtered caller, and the click.
- Message buzz (S07).
- A low pulse of music under everything that **drops out completely at 13.0** when the message lands. The last two seconds are just the tap.
- No whooshes or risers.

**Look:** add light film grain, soft highlight glow and slightly lifted (muted) blacks, and keep skin warm. No teal-orange grade, no sharpening.

**Text:** if you add subtitles, make them small and off-white, low in the frame. An optional opening card can read `EPISODE 01 — 8:47`. Social Salsaa branding goes on the end frame only, or leave it out.

## 6. Final check before posting

- [ ] Does Sasha look like the same actress in every shot?
- [ ] Is the kajal under her left eye only, and does she wear gold studs throughout?
- [ ] Are there no extra fingers or warped phones, and is the cracked corner on the same side in every shot?
- [ ] Is the tap running from S04 to the end?
- [ ] Is the message readable, does the music drop out, and does the cut land on her unsettled face?
- [ ] Does it feel like 15 seconds of a show, not a reel?

---

## Shot prompts

Copy each Step A prompt into image-with-references, and each Step B prompt into image-to-video.

### S01: Phone vibrating, she jolts awake · use 2.5 s

**Step A, still frame** (Image with References, `@Sasha` attached).
```
@Sasha. Extreme close-up of a smartphone with a cracked corner screen protector vibrating on a wooden bedside table, small Mumbai bedroom, morning light through window grilles casting bars across white sheets. In the background, out of focus, she lies in a faded grey oversized tee, hair in a collapsing claw-clip bun, kajal smudge under her left eye only; she jolts awake with her face in the pillow and reaches toward the phone. Slow rack focus from phone to her face. Static camera. Same woman as reference image: young woman with blended Indian and Western features, warm medium complexion, large brown almond eyes, full natural brows, long textured dark-brown hair, small gold stud earrings. Natural skin texture with visible pores, flyaways and slight facial asymmetry. Late-1990s film texture, gentle grain, soft highlight bloom, muted blacks, warm natural skin tones, practical morning light, realistic shadows. Not sharp HDR, no teal-orange grade, no slow motion, no floating camera.
```
**Step B, video** (image-to-video from that still, 9:16, 5 s)
```
The phone vibrates and skitters slightly on the wood. In the background she jolts awake and slaps a hand toward it. Slow rack focus from the phone to her face. Locked-off camera.
```

### S02: 8:47 AM, "Shit." · use 1.5 s

**Step A, still frame** (Image with References, `@Sasha` attached).
```
@Sasha. Over-the-shoulder shot from behind her shoulder in bed, looking down at the phone lock screen glowing in her hand, cracked corner on the screen protector. Her hair is a collapsing claw-clip bun, her grey tee is faded. Screen kept plain and blank for compositing. Static camera. Same woman as reference image: young woman with blended Indian and Western features, warm medium complexion, large brown almond eyes, full natural brows, long textured dark-brown hair, small gold stud earrings. Natural skin texture with visible pores, flyaways and slight facial asymmetry. Late-1990s film texture, gentle grain, soft highlight bloom, muted blacks, warm natural skin tones, practical morning light, realistic shadows. Not sharp HDR, no teal-orange grade, no slow motion, no floating camera.
```
**Step B, video** (image-to-video from that still, 9:16, 5 s)
```
Her thumb taps the phone to silence it. She stares at the screen and mutters one word. Locked-off camera.
```

### S03: Out of bed, clothes flying · use 2.0 s

**Step A, still frame** (Image with References, `@Sasha` attached).
```
@Sasha. Static wide shot of a small, lived-in Mumbai bedroom, clothes piled on a chair, half-open cupboard, morning light through window grilles. She scrambles out of bed in a faded grey oversized tee, foot catches the sheet, stumbles without falling, lunges to the cupboard and flings clothes onto the chair, yanks out a crumpled white shirt and rushes out of frame. Realistic weight. Locked-off camera. Same woman as reference image: young woman with blended Indian and Western features, warm medium complexion, large brown almond eyes, full natural brows, long textured dark-brown hair, small gold stud earrings. Natural skin texture with visible pores, flyaways and slight facial asymmetry. Late-1990s film texture, gentle grain, soft highlight bloom, muted blacks, warm natural skin tones, practical morning light, realistic shadows. Not sharp HDR, no teal-orange grade, no slow motion, no floating camera.
```
**Step B, video** (image-to-video from that still, 9:16, 5 s)
```
She scrambles out of bed, her foot catches the sheet, she stumbles without falling, lunges to the cupboard, flings clothes onto the chair, grabs a white shirt and runs out of frame. Real weight. Locked-off camera.
```

### S04a: Mirror jump cut (a): brushing · use 0.8 s

**Step A, still frame** (Image with References, `@Sasha` attached).
```
@Sasha. Medium shot of her reflection in a small bathroom mirror cabinet with desilvered edges, steel tumbler of toothbrushes on the ledge, tap running. She is in a faded grey tee, hair in a messy bun, kajal smudge under her left eye only, brushing her teeth aggressively. Subtle handheld from the doorway. Same woman as reference image: young woman with blended Indian and Western features, warm medium complexion, large brown almond eyes, full natural brows, long textured dark-brown hair, small gold stud earrings. Natural skin texture with visible pores, flyaways and slight facial asymmetry. Late-1990s film texture, gentle grain, soft highlight bloom, muted blacks, warm natural skin tones, practical morning light, realistic shadows. Not sharp HDR, no teal-orange grade, no slow motion, no floating camera.
```
**Step B, video** (image-to-video from that still, 9:16, 5 s)
```
She brushes her teeth fast and aggressively while the tap runs. Slight handheld.
```

### S04b: Mirror jump cut (b): shirt · use 0.75 s

**Step A, still frame** (Image with References, `@Sasha` attached). Add your approved **S04a** frame as a second reference, tagged `@Bathroom`, so the mirror, tumbler and tap stay the same set.
```
@Sasha. Medium shot of her reflection in a small bathroom mirror cabinet with desilvered edges, steel tumbler of toothbrushes, tap running. She has a crumpled white shirt half on, one arm in, and checks the collar in the mirror. Kajal smudge under her left eye only. Subtle handheld from the doorway, same framing. Same woman as reference image: young woman with blended Indian and Western features, warm medium complexion, large brown almond eyes, full natural brows, long textured dark-brown hair, small gold stud earrings. Natural skin texture with visible pores, flyaways and slight facial asymmetry. Late-1990s film texture, gentle grain, soft highlight bloom, muted blacks, warm natural skin tones, practical morning light, realistic shadows. Not sharp HDR, no teal-orange grade, no slow motion, no floating camera.
```
**Step B, video** (image-to-video from that still, 9:16, 5 s)
```
She shoves one arm into the white shirt and tugs at the collar, checking it in the mirror. Slight handheld.
```

### S04c: Mirror jump cut (c): hair · use 0.75 s

**Step A, still frame** (Image with References, `@Sasha` attached). Add your approved **S04a** frame as a second reference, tagged `@Bathroom`, so the mirror, tumbler and tap stay the same set.
```
@Sasha. Medium shot of her reflection in a small bathroom mirror cabinet with desilvered edges, tap running. In a crumpled white shirt, top two buttons undone, she yanks her hair into a tie, misses some strands, flyaways left loose, and gives up. Kajal smudge under her left eye only. Subtle handheld from the doorway, same framing. Same woman as reference image: young woman with blended Indian and Western features, warm medium complexion, large brown almond eyes, full natural brows, long textured dark-brown hair, small gold stud earrings. Natural skin texture with visible pores, flyaways and slight facial asymmetry. Late-1990s film texture, gentle grain, soft highlight bloom, muted blacks, warm natural skin tones, practical morning light, realistic shadows. Not sharp HDR, no teal-orange grade, no slow motion, no floating camera.
```
**Step B, video** (image-to-video from that still, 9:16, 5 s)
```
She yanks her hair into a tie, strands slip out, she gives up. Slight handheld.
```

### S04d: Mirror jump cut (d): breath and smile · use 0.7 s

**Step A, still frame** (Image with References, `@Sasha` attached). Add your approved **S04a** frame as a second reference, tagged `@Bathroom`, so the mirror, tumbler and tap stay the same set.
```
@Sasha. Medium shot of her reflection in a small bathroom mirror cabinet with desilvered edges, tap running. In a crumpled white shirt, hair half-tied with flyaways, she checks her breath into her cupped palm, then attempts a polite professional smile at the mirror that fades instantly. Kajal smudge under her left eye only. Subtle handheld from the doorway, same framing. Same woman as reference image: young woman with blended Indian and Western features, warm medium complexion, large brown almond eyes, full natural brows, long textured dark-brown hair, small gold stud earrings. Natural skin texture with visible pores, flyaways and slight facial asymmetry. Late-1990s film texture, gentle grain, soft highlight bloom, muted blacks, warm natural skin tones, practical morning light, realistic shadows. Not sharp HDR, no teal-orange grade, no slow motion, no floating camera.
```
**Step B, video** (image-to-video from that still, 9:16, 5 s)
```
She breathes into her cupped palm and sniffs, then forces a polite smile at the mirror that drops instantly. Slight handheld.
```

### S05: Phone rings: K. · use 0.8 s

**Step A, still frame** (Image with References, `@Sasha` attached). Add your approved **S04a** frame as a second reference, tagged `@Bathroom`, so the mirror, tumbler and tap stay the same set.
```
@Sasha. Insert close-up of a smartphone with a cracked corner screen protector ringing on the edge of a bathroom sink beside a running tap, steel tumbler of toothbrushes nearby. Her hand, white shirt cuff unbuttoned, enters frame edge and freezes mid-reach. Screen plain for compositing. Static camera. Same woman as reference image: young woman with blended Indian and Western features, warm medium complexion, large brown almond eyes, full natural brows, long textured dark-brown hair, small gold stud earrings. Natural skin texture with visible pores, flyaways and slight facial asymmetry. Late-1990s film texture, gentle grain, soft highlight bloom, muted blacks, warm natural skin tones, practical morning light, realistic shadows. Not sharp HDR, no teal-orange grade, no slow motion, no floating camera.
```
**Step B, video** (image-to-video from that still, 9:16, 5 s)
```
The phone vibrates on the sink ledge. Her hand reaches in from the frame edge and freezes. Tap water keeps running. Locked-off camera.
```

### S06: The call · use 3.2 s

**Step A, still frame** (Image with References, `@Sasha` attached). Add your approved **S04a** frame as a second reference, tagged `@Bathroom`, so the mirror, tumbler and tap stay the same set.
```
@Sasha. Over-the-shoulder into a bathroom mirror cabinet with desilvered edges, her real shoulder soft in the foreground. In the reflection she holds a phone to her ear, crumpled white shirt with top two buttons undone, hair half-tied with flyaways, kajal under her left eye only. She looks away from her reflection, swallows, speaks briefly, lowers the phone as the call ends, then slowly meets her own eyes in the mirror and holds the look. Tap running. Static, slightly imperfect framing. Same woman as reference image: young woman with blended Indian and Western features, warm medium complexion, large brown almond eyes, full natural brows, long textured dark-brown hair, small gold stud earrings. Natural skin texture with visible pores, flyaways and slight facial asymmetry. Late-1990s film texture, gentle grain, soft highlight bloom, muted blacks, warm natural skin tones, practical morning light, realistic shadows. Not sharp HDR, no teal-orange grade, no slow motion, no floating camera.
```
**Step B, video** (image-to-video from that still, 9:16, 5 s)
```
She listens on the phone, swallows, says a few words without meeting her own eyes, lowers the phone, then slowly looks at her reflection and holds the look. Static camera.
```

### S07: FINAL: the message · use 2.0 s

**Step A, still frame** (Image with References, `@Sasha` attached). Add your approved **S04a** frame as a second reference, tagged `@Bathroom`, so the mirror, tumbler and tap stay the same set.
```
@Sasha. Close over-the-shoulder shot of a phone with a cracked corner screen protector held at chest height in her hand, white shirt cuff unbuttoned. Her reflection is soft in the bathroom mirror behind it, hair half-tied. The phone gives a small buzz; she goes very still, breath catches, she swallows. Slow rack focus from the phone to her reflection's face, visibly unsettled, jaw tight. Tap running. Screen plain for compositing. Same woman as reference image: young woman with blended Indian and Western features, warm medium complexion, large brown almond eyes, full natural brows, long textured dark-brown hair, small gold stud earrings. Natural skin texture with visible pores, flyaways and slight facial asymmetry. Late-1990s film texture, gentle grain, soft highlight bloom, muted blacks, warm natural skin tones, practical morning light, realistic shadows. Not sharp HDR, no teal-orange grade, no slow motion, no floating camera.
```
**Step B, video** (image-to-video from that still, 9:16, 5 s)
```
The phone buzzes once. She goes very still, breath catches, she swallows. Slow rack focus from the phone screen to her reflection's face. Static camera.
```

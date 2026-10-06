# EP01 "8:47": Higgsfield prompt

**Setup:** Upload `reference/sasha.jpg` as the character / reference image. Settings: 9:16, 15 s (or the longest the model allows), sound on if the model generates audio. Paste the prompt below as is.

## Prompt

```
9:16 vertical, 15 seconds, one continuous multi-shot scene with hard cuts. Same woman as the reference image in every shot: Sasha, young woman with blended Indian and Western features, warm medium complexion, large brown almond eyes, full natural brows, long wavy dark-brown hair with warm highlights, small gold stud earrings, a smudge of old kajal under her LEFT eye only, no other makeup. Natural skin with pores, flyaways, slight asymmetry. Small lived-in Mumbai apartment, practical morning light. Late-1990s film look: gentle grain, soft highlight bloom, muted blacks, warm skin tones.

0.0–2.5s: Extreme close-up, locked off. A smartphone with a cracked corner screen protector vibrates hard and skitters on a worn wooden bedside table; morning light through metal window grilles casts bars across white sheets. Behind it, out of focus, Sasha in a faded grey oversized tee, hair in a collapsing claw-clip bun, jolts awake, face half in the pillow, puffy-eyed, and slaps a hand toward the phone. Slow rack focus to her face.
2.5–4.0s: Over her shoulder in bed, looking down at the glowing phone in her hand; screen blank. She silences it and mutters, low and flat: "Shit."
4.0–6.0s: Static wide of the cluttered bedroom, clothes piled on a chair, half-open cupboard. She scrambles out of bed, her foot catches the sheet, she stumbles but doesn't fall, flings clothes onto the chair, grabs a crumpled white shirt and rushes out of frame.
6.0–9.0s: Bathroom. Medium shot of her reflection in a small mirror cabinet with desilvered edges, steel tumbler of toothbrushes, tap running the whole time. Slight handheld from the doorway, the same framing for four quick jump cuts: she brushes her teeth aggressively; she pulls the white shirt on, one arm in, checks the collar; she yanks her hair into a tie and misses strands; she checks her breath in her cupped palm, tries a polite professional smile that drops instantly.
9.0–9.8s: Insert. The phone rings on the sink ledge beside the running tap, screen blank. Her hand enters frame and freezes mid-reach.
9.8–13.0s: Over her shoulder into the mirror, her real shoulder soft in the foreground. White shirt with the top two buttons undone, one cuff open, hair half-tied with flyaways. Phone to her ear. A calm male or female voice, phone-filtered: "We're on for today?" She avoids her own eyes, swallows, and says, nervous and distracted: "Yeah… I don't really have an option." A click; the line goes dead. She slowly looks at her reflection and holds it a beat too long.
13.0–15.0s: Close over-the-shoulder shot of the phone held at chest height, screen blank, her reflection soft in the mirror behind it. The phone buzzes once. She goes completely still, breath catches, she swallows. Slow rack focus to her reflection's face, visibly unsettled. Hard cut to black.

Sound: phone vibration rattling wood, ceiling fan hum, distant Mumbai car horn, bare feet on tile, toothbrush scrubbing, the tap running continuously from the bathroom to the final frame, ringtone, a low pulsing underscore that cuts to silence at 13 seconds, leaving only the running tap.
```

## Negative prompt (if the model has a field for it)

```
waxy or airbrushed skin, face morphing, changing face between shots, glam makeup, kajal under both eyes, hoop earrings, extra fingers, warped phone, readable or gibberish text on phone screens, captions, subtitles, logos, slow motion, floating or orbiting camera, teal-orange grade, HDR, oversharpened, luxury interior, people staring into camera
```

## Notes
- **Phone screens are kept blank on purpose.** Add `8:47 AM`, `K.` and `Whatever happens, don't tell them.` in the edit; models garble on-screen text.
- **If the model maxes out under 15 s**, split at the cut: run 0.0–9.0 s as clip 1 and 9.0–15.0 s as clip 2, keeping the opening character paragraph and the sound line in both.
- **Check the kajal side.** It's under her left eye. When the camera faces her (0–6 s), it's on screen-right. In the mirror shots (6–15 s), the camera is behind her, so it's on screen-left in the reflection. Regenerate if it's under both eyes.

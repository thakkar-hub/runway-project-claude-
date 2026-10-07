# STAIN HAPPENS / RUN — campaign poster prompt

- **Model:** `gemini_2.5_flash` (renders typography most reliably); `gen4_image` as a fallback
- **Ratio:** 9:16, `768:1344` (gemini) or `1080:1920` (gen4_image)
- **Logo:** if you have the Paddling Foundation logo file, pass it as a reference (`logo=./paddling-logo.png`). Otherwise leave the logo area blank and add it in post, because the model will make up its own mark.

## Prompt

Vertical 9:16 high-fashion editorial running campaign poster, experimental sportswear advertising meets underground running-club graphics. Dark, cinematic, sophisticated, slightly rebellious. Not a charity or marathon event poster.

Image: a small group of strong, athletic, real-looking women sprinting away from the camera down a dark empty street at night. One central runner is the hero, sharp and backlit, while the others dissolve into motion blur. Dramatic directional side light, deep crushed blacks, warm off-white highlights on skin and fabric, subtle film grain, halftone print texture, intentional horizontal motion blur, and a few selective streaks of deep oxblood-red light in the background. The runners wear clean, plain charcoal and off-white running kit with no red on the clothing and no marks, stains or discoloration of any kind.

Typography: premium experimental sports-campaign type. Oversized, tightly kerned condensed grotesk sans-serif, editorial spacing, asymmetrical layout, lots of negative space.
- Headline in warm off-white condensed sans: "SHIT HAPPENS". The word "SHIT" has a single imperfect hand-drawn deep red line striking through it.
- Directly above the crossed-out word, the small handwritten lowercase word "stain" in deep red marker, so the line reads "stain HAPPENS".
- Below that, the word "RUN" huge in deep oxblood red condensed sans, filling the poster width, smeared horizontally as if moving at speed.
- A small, understated foundation logo at top centre.
- Very subtle thin off-white grid and construction lines as a graphic device.

No other text. No slogans, taglines, dates, URLs, doodles, hearts, arrows or motivational phrases. No blood. Palette: charcoal black, warm off-white, muted grey, deep oxblood red. Mood: Nike Run Club campaign meets independent fashion magazine meets provocative social-impact ad. Minimal, mysterious, raw, premium.

## Run

```bash
uv run scripts/generate_image.py \
  --model gemini_2.5_flash --ratio 768:1344 \
  --prompt "$(sed -n '/^## Prompt/,/^## Run/p' prompts/stain-happens-run-poster.md | sed '1d;$d')" \
  --filename "2026-10-07-stain-happens-run-poster.png"
```

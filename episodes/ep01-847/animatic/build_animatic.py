"""Build a 15 s 9:16 timing animatic for EP01 from shot cards (no generated footage)."""
import subprocess, textwrap
from PIL import Image, ImageDraw, ImageFont, ImageFilter

W, H = 720, 1280
BG, INK, DIM, ACC = (22, 19, 17), (236, 228, 214), (150, 140, 126), (200, 60, 50)
F = "/usr/share/fonts/truetype/dejavu/"
serif = lambda s: ImageFont.truetype(F + "DejaVuSerif.ttf", s)
sans = lambda s: ImageFont.truetype(F + "DejaVuSans.ttf", s)
sansb = lambda s: ImageFont.truetype(F + "DejaVuSans-Bold.ttf", s)

SHOTS = [
 ("S01", 2.5, "ECU · locked off · rack focus", "Phone skitters on the wooden bedside table. Behind it, Sasha jolts awake, face half in the pillow, hand slapping toward it.", None, None),
 ("S02", 1.5, "OTS onto lock screen", "She stares at the screen.", "lock", 'SASHA: "Shit."'),
 ("S03", 2.0, "Static wide · bedroom", "Out of bed. Foot catches the sheet. Stumble. Clothes flung onto the chair. White shirt grabbed. Gone.", None, None),
 ("S04a", 0.8, "Mirror · handheld · jump cut a", "Brushing. Aggressively. Tap running.", None, None),
 ("S04b", 0.75, "Mirror · jump cut b", "Shirt half on. Collar check.", None, None),
 ("S04c", 0.75, "Mirror · jump cut c", "Hair yanked into a tie. Misses. Gives up.", None, None),
 ("S04d", 0.7, "Mirror · jump cut d", "Breath check. 'Professional' smile. It dies.", None, None),
 ("S05", 0.8, "Insert · sink ledge", "Her hand freezes mid-reach.", "call", 'CALLER: "We\'re on for—"'),
 ("S06", 3.2, "OTS into mirror", "She avoids her own eyes. Swallows. Answers. CLICK. Then she looks at herself, a beat too long.", None, 'CALLER: "—today?"\nSASHA: "Yeah… I don\'t really have an option."'),
 ("S07", 2.0, "Close OTS · phone at chest height", "Her reflection goes still. Swallow. Rack to her unsettled face. CUT.", "msg", None),
]

def phone(d, kind):
    x0, y0, x1, y1 = 190, 330, 530, 1000
    d.rounded_rectangle((x0, y0, x1, y1), 46, fill=(10, 10, 12), outline=(70, 66, 60), width=4)
    d.polygon([(x1-70, y0+4), (x1-4, y0+4), (x1-4, y0+70)], outline=(120, 115, 105))  # cracked corner
    d.line((x1-60, y0+14, x1-30, y0+40), fill=(120, 115, 105), width=1)
    c = (x0 + x1) // 2
    if kind == "lock":
        d.text((c, y0+170), "8:47", font=sans(110), fill=(245, 245, 245), anchor="mm")
        d.text((c, y0+240), "AM", font=sans(30), fill=(200, 200, 200), anchor="mm")
    elif kind == "call":
        d.text((c, y0+120), "incoming call", font=sans(22), fill=(170, 170, 170), anchor="mm")
        d.text((c, y0+200), "K.", font=sans(84), fill=(245, 245, 245), anchor="mm")
        d.ellipse((x0+50, y1-150, x0+130, y1-70), fill=(190, 50, 45))
        d.ellipse((x1-130, y1-150, x1-50, y1-70), fill=(50, 160, 80))
    elif kind == "msg":
        d.rounded_rectangle((x0+18, y0+90, x1-18, y0+230), 22, fill=(48, 48, 52))
        d.text((x0+40, y0+108), "K.", font=sansb(22), fill=(235, 235, 235))
        d.multiline_text((x0+40, y0+142), "Whatever happens,\ndon't tell them.", font=sans(26), fill=(235, 235, 235), spacing=6)

frames = []
t = 0.0
for sid, dur, framing, action, screen, dlg in SHOTS:
    im = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(im)
    d.text((40, 60), f"EP01 · 8:47", font=sans(22), fill=DIM)
    d.text((W-40, 60), f"{t:.1f}–{t+dur:.1f}s", font=sans(22), fill=DIM, anchor="ra")
    d.text((40, 110), sid, font=sansb(54), fill=ACC)
    d.text((40, 180), framing.upper(), font=sans(22), fill=DIM)
    if screen:
        phone(d, screen)
        ay = 1035
    else:
        ay = 420
    d.multiline_text((40, ay), "\n".join(textwrap.wrap(action, 30 if not screen else 40)),
                     font=serif(40 if not screen else 26), fill=INK, spacing=14)
    if dlg:
        lines = dlg.split("\n")
        y = H - 70 - 40 * len(lines)
        for ln in lines:
            d.text((W//2, y), ln, font=sans(24), fill=(240, 236, 228), anchor="mm",
                   stroke_width=2, stroke_fill=(0, 0, 0)); y += 40
    p = f"card_{sid}.png"; im.save(p); frames.append((p, dur)); t += dur

with open("cards.txt", "w") as f:
    for p, dur in frames: f.write(f"file '{p}'\nduration {dur}\n")
    f.write(f"file '{frames[-1][0]}'\n")

# sound sketch: vibration 0-2.4, tap water hiss 6.0-15, ringtone 9.0-9.8, click 12.2, buzz 13.0, pulse 0-13
audio = ("aevalsrc=exprs='"
 "0.35*between(t,0.1,2.4)*sin(2*PI*150*t)*gt(sin(2*PI*2.5*t),0)"
 "+0.25*between(t,9.0,10.1)*sin(2*PI*880*t)*gt(sin(2*PI*6*t),0)"
 "+0.5*between(t,12.20,12.23)*sin(2*PI*1200*t)"
 "+0.35*between(t,13.0,13.35)*sin(2*PI*170*t)"
 "+0.12*lt(t,13)*sin(2*PI*55*t)*(0.5+0.5*sin(2*PI*1.6*t))"
 "':s=44100:d=15[a0];"
 "anoisesrc=d=15:c=pink:a=0.05,volume='between(t,6.0,15)':eval=frame,lowpass=f=3000[w];"
 "[a0][w]amix=inputs=2:normalize=0[a]")
subprocess.run(["ffmpeg", "-y", "-loglevel", "error",
  "-f", "concat", "-safe", "0", "-i", "cards.txt",
  "-filter_complex", audio + ";[0:v]fps=24,noise=alls=7:allf=t,format=yuv420p[v]",
  "-map", "[v]", "-map", "[a]", "-t", "15", "-c:v", "libx264", "-crf", "30", "-maxrate", "2M", "-bufsize", "4M", "-preset", "slow", "-tune", "grain",
  "-c:a", "aac", "-b:a", "128k", "ep01_animatic.mp4"], check=True)

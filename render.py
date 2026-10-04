#!/usr/bin/env python3
"""Render an episode's shots with the Runway API.

Two stages per shot, so every shot locks to Sasha's face:
  1. gen4_image   – keyframe from the shot prompt + Sasha reference image
  2. gen4_turbo   – image_to_video animating that keyframe with the shot's
                   motion-only prompt (5 s, trimmed in edit)

Usage:
  export RUNWAYML_API_SECRET=...
  python3 render.py episodes/ep01-847 [SHOT_ID ...]

Stdlib only. Outputs go to <episode>/renders/.
"""
import base64, json, mimetypes, os, sys, time, urllib.request, urllib.error
from pathlib import Path

API = "https://api.dev.runwayml.com/v1"
VERSION = "2024-11-06"


def call(method, path, body=None):
    req = urllib.request.Request(
        API + path,
        method=method,
        data=json.dumps(body).encode() if body else None,
        headers={
            "Authorization": f"Bearer {os.environ['RUNWAYML_API_SECRET']}",
            "X-Runway-Version": VERSION,
            "Content-Type": "application/json",
        },
    )
    try:
        with urllib.request.urlopen(req) as r:
            return json.load(r)
    except urllib.error.HTTPError as e:
        sys.exit(f"{method} {path} -> {e.code}: {e.read().decode()}")


def wait(task_id):
    while True:
        task = call("GET", f"/tasks/{task_id}")
        if task["status"] == "SUCCEEDED":
            return task["output"][0]
        if task["status"] in ("FAILED", "CANCELLED"):
            sys.exit(f"task {task_id} {task['status']}: {task.get('failure')}")
        time.sleep(5)


def data_uri(path):
    mime = mimetypes.guess_type(path)[0] or "image/jpeg"
    return f"data:{mime};base64,{base64.b64encode(Path(path).read_bytes()).decode()}"


def download(url, dest):
    with urllib.request.urlopen(url) as r:
        dest.write_bytes(r.read())
    print(f"  saved {dest}")


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    ep = Path(sys.argv[1])
    spec = json.loads((ep / "shots.json").read_text())
    ref = Path(spec["reference_image"])
    if not ref.exists():
        sys.exit(f"missing reference image: {ref}")
    ref_uri = data_uri(ref)
    wanted = set(sys.argv[2:])
    out = ep / "renders"
    out.mkdir(exist_ok=True)

    for shot in spec["shots"]:
        if wanted and shot["id"] not in wanted:
            continue
        print(f"{shot['id']}: keyframe")
        prompt = f"{shot['prompt']} {spec['style']}"
        if len(prompt) > 990:
            sys.exit(f"{shot['id']}: prompt is {len(prompt)} chars, Runway max is 1000")
        img = wait(call("POST", "/text_to_image", {
            "model": "gen4_image",
            "ratio": spec["ratio"],
            "promptText": f"@Sasha. {prompt}",
            "referenceImages": [{"uri": ref_uri, "tag": "Sasha"}],
        })["id"])
        download(img, out / f"{shot['id']}_key.png")

        print(f"{shot['id']}: video")
        vid = wait(call("POST", "/image_to_video", {
            "model": "gen4_turbo",
            "ratio": spec["ratio"],
            "duration": 5,
            "promptImage": img,
            "promptText": shot.get("motion", prompt),
        })["id"])
        download(vid, out / f"{shot['id']}.mp4")


if __name__ == "__main__":
    main()

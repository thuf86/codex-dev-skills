# Reproducible local rendering pipeline

Prerequisites: Python 3.10+, FFmpeg, FFprobe, Pillow (see requirements.txt), optional local .ttf font.

```bash
python -m pip install -r skills/instagram-video-pro/requirements.txt
python skills/instagram-video-pro/scripts/render.py --project skills/instagram-video-pro/templates/project.example.json --output output.mp4
python skills/instagram-video-pro/scripts/validate_video.py output.mp4 --json
python -m unittest discover -s skills/instagram-video-pro/tests -v
```

Schema: canvas fixed to width=1080,height=1920,fps=30; brand has background/accent/text/footer/optional local font; each slide has title, body, seconds, optional accent. Optional voiceover and music are local relative file paths resolved against project JSON; caption is the Instagram post text and is not inserted into video.

The renderer draws branded graphic slides and optionally muxes licensed audio. It does **not** synthesize human speech, generate photorealistic scenes, source external footage or publish Instagram content. To produce more advanced film sequences, generate authorized assets in a separate provider, edit using an available editor/Remotion, then run quality gates.

Validator checks video stream, 1080×1920 dimensions, H.264, yuv420p, 30 fps and sane duration. It does not replace review of audio, image quality or facts.

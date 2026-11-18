#!/usr/bin/env python3
"""FFprobe quality gate; must be accompanied by visual/audio review."""
import argparse
import json
from pathlib import Path
import shutil
import subprocess
import sys

def check(path):
    p=Path(path)
    errors=[]
    if not p.is_file() or p.stat().st_size==0:
        return {"ok":False,"errors":["Missing or empty video"]}
    if not shutil.which("ffprobe"):
        return {"ok":False,"errors":["ffprobe unavailable"]}
    res=subprocess.run(["ffprobe","-v","error","-show_format","-show_streams","-of","json",str(p)],capture_output=True,text=True)
    if res.returncode:
        return {"ok":False,"errors":[res.stderr.strip() or "ffprobe error"]}
    try: info=json.loads(res.stdout)
    except json.JSONDecodeError: return {"ok":False,"errors":["Invalid ffprobe response"]}
    v=next((s for s in info.get("streams",[]) if s.get("codec_type")=="video"),None)
    if v is None: errors.append("Missing video stream")
    else:
        for key,expect in (("width",1080),("height",1920),("codec_name","h264"),("pix_fmt","yuv420p")):
            if v.get(key)!=expect: errors.append("%s expected %s, got %s"%(key,expect,v.get(key)))
        try:
            n,d=map(int,v.get("avg_frame_rate","0/1").split("/"))
            fps=n/d
        except (ValueError,ZeroDivisionError): fps=0
        if abs(fps-30)>0.1: errors.append("FPS not 30")
    try: duration=float(info.get("format",{}).get("duration",0))
    except ValueError: duration=0.
    if not 0<duration<=180.25: errors.append("Invalid duration")
    return {"ok":not errors,"errors":errors,"duration_seconds":round(duration,3),"audio_present":any(s.get("codec_type")=="audio" for s in info.get("streams",[])),"file":str(p)}

if __name__=="__main__":
    a=argparse.ArgumentParser()
    a.add_argument("file")
    a.add_argument("--json",action="store_true")
    args=a.parse_args()
    report=check(args.file)
    print(json.dumps(report,indent=2,ensure_ascii=False) if args.json else ("PASS" if report["ok"] else "FAIL")+" "+str(report))
    sys.exit(0 if report["ok"] else 1)

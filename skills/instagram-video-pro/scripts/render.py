#!/usr/bin/env python3
"""Render branded Instagram slide videos using FFmpeg. No remote API calls."""
import argparse
import json
import math
from pathlib import Path
import shutil
import subprocess
import tempfile
from PIL import Image, ImageDraw, ImageFont

def color(v):
    if not isinstance(v,str) or len(v)!=7 or not v.startswith("#") or any(c not in "0123456789abcdefABCDEF" for c in v[1:]):
        raise ValueError("Invalid hex color")
    return v

def font_file(custom):
    candidates=[custom,"/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf","/usr/share/fonts/truetype/liberation2/LiberationSans-Bold.ttf","C:/Windows/Fonts/arialbd.ttf","/System/Library/Fonts/Supplemental/Arial Bold.ttf"]
    return next((str(p) for p in candidates if p and Path(p).is_file()),None)

def font(path,size):
    return ImageFont.truetype(path,size) if path else ImageFont.load_default()

def wrap(draw,text,f,max_width):
    lines=[]
    current=""
    for word in str(text).split():
        candidate=(current+" "+word).strip()
        if draw.textbbox((0,0),candidate,font=f)[2] <= max_width:
            current=candidate
        else:
            if current: lines.append(current)
            current=word
            if draw.textbbox((0,0),word,font=f)[2]>max_width:
                raise ValueError("Text contains word wider than safe region")
    if current: lines.append(current)
    return lines

def render_slide(slide,brand,path):
    w,h=1080,1920
    img=Image.new("RGB",(w,h),color(brand.get("background","#050708")))
    d=ImageDraw.Draw(img)
    margin=int(w*.095)
    top=int(h*.17)
    bottom=int(h*.2)
    accent=color(slide.get("accent",brand.get("accent","#00FF9C")))
    ink=color(brand.get("text","#FFFFFF"))
    face=font_file(brand.get("font"))
    heading=font(face,75)
    body=font(face,40)
    small=font(face,23)
    d.rounded_rectangle((margin,top,margin+125,top+11),radius=5,fill=accent)
    title_lines=wrap(d,slide["title"],heading,w-2*margin)
    body_lines=wrap(d,slide.get("body",""),body,w-2*margin)
    if len(title_lines)>4 or len(body_lines)>7:
        raise ValueError("Slide exceeds maximum typography limits")
    y=top+70
    for line in title_lines:
        d.text((margin,y),line,font=heading,fill=ink)
        y+=105
    y+=70
    for line in body_lines:
        d.text((margin,y),line,font=body,fill=ink)
        y+=66
    footer=brand.get("footer","")
    if footer:
        if d.textbbox((0,0),footer,font=small)[2] > w-2*margin: raise ValueError("Footer too long")
        d.text((margin,h-bottom+110),footer,font=small,fill=accent)
    img.save(path)

def valid_project(p):
    c=p.get("canvas",{})
    if (c.get("width"),c.get("height"),c.get("fps")) != (1080,1920,30):
        raise ValueError("Only 1080x1920 at 30fps is supported")
    slides=p.get("slides")
    if not isinstance(slides,list) or not 1<=len(slides)<=30:
        raise ValueError("Expected 1 to 30 slides")
    duration=0.
    for s in slides:
        if not isinstance(s.get("title"),str) or not s["title"].strip(): raise ValueError("Nonempty title required")
        t=s.get("seconds",0)
        if type(t) not in (float,int) or not math.isfinite(t) or t<=0 or t>30:
            raise ValueError("Slide seconds must be 0 < seconds <= 30")
        duration+=t
    if duration>180: raise ValueError("Video longer than 180 seconds")
    return duration

def render(project_path,output):
    if not shutil.which("ffmpeg") or not shutil.which("ffprobe"):
        raise RuntimeError("FFmpeg and FFprobe must be installed")
    p=Path(project_path).resolve()
    cfg=json.loads(p.read_text(encoding="utf-8"))
    duration=valid_project(cfg)
    destination=Path(output).resolve()
    destination.parent.mkdir(parents=True,exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="instagram-video-") as tmp:
        tmp=Path(tmp)
        inputs=[]
        for i,s in enumerate(cfg["slides"]):
            image=tmp/("slide-%03d.png"%i)
            render_slide(s,cfg.get("brand",{}),image)
            inputs+=["-loop","1","-framerate","30","-t",str(s["seconds"]),"-i",str(image)]
        audio=[]
        for key in ("voiceover","music"):
            if cfg.get(key):
                audio_file=Path(cfg[key])
                if not audio_file.is_absolute(): audio_file=(p.parent/audio_file).resolve()
                if not audio_file.is_file(): raise FileNotFoundError(audio_file)
                audio.append((key,audio_file))
                inputs+=["-i",str(audio_file)]
        graphs=["[%d:v]setsar=1,format=yuv420p[v%d]"%(i,i) for i in range(len(cfg["slides"]))]
        graphs.append("".join("[v%d]"%i for i in range(len(cfg["slides"])))+"concat=n=%d:v=1:a=0[vout]"%len(cfg["slides"]))
        cmd=["ffmpeg","-hide_banner","-loglevel","error","-y",*inputs]
        if len(audio)==2:
            i=len(cfg["slides"])
            graphs+=["[%d:a]volume=1.0[a0]"%i,"[%d:a]volume=0.12[a1]"%(i+1),"[a0][a1]amix=inputs=2:duration=longest:normalize=0,apad,atrim=duration=%s[aout]"%duration]
        cmd+=["-filter_complex",";".join(graphs),"-map","[vout]"]
        if len(audio)==2:
            cmd+=["-map","[aout]","-c:a","aac","-b:a","192k"]
        elif len(audio)==1:
            cmd+=["-map","%d:a:0"%len(cfg["slides"]),"-af","apad,atrim=duration=%s"%duration,"-c:a","aac","-b:a","192k"]
        else:
            cmd+=["-an"]
        cmd+=["-c:v","libx264","-preset","medium","-crf","20","-pix_fmt","yuv420p","-r","30","-movflags","+faststart","-t",str(duration),str(destination)]
        subprocess.run(cmd,check=True)
    return destination

if __name__=="__main__":
    a=argparse.ArgumentParser()
    a.add_argument("--project",required=True)
    a.add_argument("--output",required=True)
    args=a.parse_args()
    print("Rendered:",render(args.project,args.output))

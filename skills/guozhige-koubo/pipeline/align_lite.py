#!/usr/bin/env python3
"""不依赖 whisper 的轻量对齐：用静音间隙锚定标点分句，再按字分配。
输入：voice.wav（44.1k/48k 单声道）+ 文本；输出：tl.json
用法：python3 align_lite.py voice.wav "文本" out.json
"""
import sys, os, json, wave, subprocess, math

def load_audio(path):
    raw = subprocess.run(["ffmpeg","-v","error","-i",path,"-ac","1","-ar","16000","-f","s16le","-"],
                         capture_output=True, check=True).stdout
    import array
    a = array.array("h"); a.frombytes(raw)
    return a, 16000

def rms_frames(samples, sr, hop_ms=10, win_ms=25):
    hop = sr*hop_ms//1000; win = sr*win_ms//1000
    out = []
    for i in range(0, max(0, len(samples)-win), hop):
        s = 0
        seg = samples[i:i+win]
        for v in seg: s += v*v
        out.append(math.sqrt(s/len(seg)))
    return out, hop/sr

def detect(samples, sr):
    fr, dt = rms_frames(samples, sr)
    mx = max(fr) or 1
    thr = max(mx*0.05, mx*0.10)
    # 语音区间
    voiced = [i for i,v in enumerate(fr) if v > thr]
    if not voiced: raise SystemExit("no speech detected")
    a, b = voiced[0]*dt, (voiced[-1]+1)*dt
    # 内部静音
    gaps = []; i = voiced[0]
    cur = None
    for i in range(voiced[0], voiced[-1]+1):
        if fr[i] <= thr:
            if cur is None: cur = i
        else:
            if cur is not None:
                d = (i-cur)*dt
                if d >= 0.10: gaps.append((cur*dt+0.02, i*dt-0.02, d))
                cur = None
    return a, b, gaps

PUNCT = "：，。、"
PAUSE = {"：":0.30, "，":0.20, "。":0.35, "、":0.15}

def clauses(text):
    """返回 [(start_idx, end_idx_exclusive, pause_after)]"""
    out=[]; start=0
    for i,ch in enumerate(text):
        if ch in PUNCT:
            if i>start: out.append((start,i,PAUSE[ch]))
            start=i+1
    if start < len(text): out.append((start,len(text),0.0))
    return out

def align(text, a, b, gaps):
    cls = clauses(text)
    bounds = len(cls)-1
    # 选锚点：把 gap 按持续时长降序，取前 bounds 个（保持时间顺序）
    cand = sorted(gaps, key=lambda g:-g[2])
    pick = sorted(cand[:bounds], key=lambda g:g[0]) if bounds>0 else []
    if len(pick) < bounds:            # 间隙不够 → 线性兜底
        pick = []
    # 子句区间
    spans=[]
    if pick and len(pick)==bounds:
        prev = a
        for k,(s0,s1,d) in enumerate(pick):
            spans.append((prev, (s0+s1)/2)); prev=(s0+s1)/2
        spans.append((prev, b))
    else:
        total_chars = sum(c[1]-c[0] for c in cls)
        t=a
        for c in cls:
            n=c[1]-c[0]; dur=(b-a)*n/max(1,total_chars)
            spans.append((t,t+dur)); t+=dur
    chars={}
    for (i0,i1,_),(t0,t1) in zip(cls,spans):
        idxs=[i for i in range(i0,i1) if not text[i].isspace()]
        if not idxs: continue
        wts=[0.55 if text[i].isascii() else 1.0 for i in idxs]
        tw=sum(wts); t=t0
        for i,w in zip(idxs,wts):
            chars[str(i)]=round(t,3); t += (t1-t0)*w/tw
    return chars, a, b, spans

if __name__=="__main__":
    wav, out = sys.argv[1], sys.argv[2]
    if len(sys.argv) > 3:
        text = sys.argv[3]
    else:
        cfgp = os.environ.get("CONFIG") or os.path.join(os.path.dirname(os.path.abspath(__file__)), "config.json")
        text = json.load(open(cfgp, encoding="utf-8"))["script"]
    samples, sr = load_audio(wav)
    a,b,gaps = detect(samples, sr)
    chars, a, b, spans = align(text, a, b, gaps)
    tl={"total":round(b+0.08,3),"segs":[{"i":1,"start":0.0,"end":round(b+0.08,3),"text":text,"chars":chars}]}
    json.dump(tl, open(out,"w"), ensure_ascii=False, indent=1)
    print(f"语音 {a:.2f}–{b:.2f}s，间隙 {len(gaps)} 个，分句 {len(spans)}")
    for w in ["到底怎么用","工具选型","Agent 搭建","接单变现","每天都有","扫码进来"]:
        i=text.index(w); print(f"  {w}: {chars.get(str(i))}")

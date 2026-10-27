#!/usr/bin/env python3
"""第 2 步（自动）：config.json + tl.json → edit.json（花字/大字/清单/二维码/胶囊）"""
import json, os, sys

here = os.path.dirname(os.path.abspath(__file__))
cfgp = sys.argv[3] if len(sys.argv) > 3 else os.path.join(here, "config.json")
cfg = json.load(open(cfgp, encoding="utf-8"))
tl = json.load(open(sys.argv[1], encoding="utf-8"))
out = sys.argv[2]
text = tl["segs"][0]["text"]

def has(w): return w and w in text

keys = [k for k in cfg.get("keys", []) if has(k)]
ed = {
    "preset": cfg.get("preset", "标准"),
    "brand": "orange",
    "badge": "内容由 AI 数字人演绎",
    "tail": cfg.get("tail", 0.6),
    "keys": keys,
}
if cfg.get("title"):
    ed["title"] = cfg["title"]

cards = []
if cfg.get("big") and has(cfg["big"]["at"]):
    cards.append({"type": "big", "at": f"1:{cfg['big']['at']}", "text": cfg["big"]["text"]})
if cfg.get("qr"):
    at = cfg.get("qr_pos", {}).get("at") or (cfg["pill"]["at"] if cfg.get("pill") else None)
    if at and has(at):
        cards.append({"type": "image", "at": f"1:{at}", "src": "show/qr.png",
                      "x": cfg["qr_pos"]["x"], "y": cfg["qr_pos"]["y"], "w": cfg["qr_pos"]["w"],
                      "label": cfg.get("qr_label", "扫码进群")})
cards += cfg.get("extra_cards", [])
if cards:
    ed["cards"] = cards

pack = []
stack = [s for s in cfg.get("stack", []) if has(s["at"])]
if stack:
    pack.append({"use": "KeywordStack", "at": f"1:{stack[0]['at']}",
                 "until": f"1:{cfg['pill']['at']}" if cfg.get("pill") else f"1:end",
                 "x": 90, "y": 700,
                 "items": [{"t": s["t"], "at": f"1:{s['at']}", "icon": s.get("icon", "💡")} for s in stack]})
if cfg.get("pill") and has(cfg["pill"]["at"]):
    p = cfg["pill"]
    pack.append({"use": "CalloutPill", "at": f"1:{p['at']}", "until": "1:end",
                 "text": p["text"], "sub": p.get("sub"), "x": 540, "y": p.get("y", 770),
                 "color": "#FF7A1A", "pointer": "down"})
pack += cfg.get("extra_pack", [])
if pack:
    ed["pack"] = pack

emojis = [m for m in cfg.get("emojis", []) if has(m["at"])]
if emojis:
    ed["emojis"] = [{"at": f"1:{m['at']}", "e": m["e"], "side": m.get("side", "r")} for m in emojis]

ed["credits"] = "Animated emoji: Google Noto"
json.dump(ed, open(out, "w"), ensure_ascii=False, indent=1)
print("edit.json 已生成：", out, "｜关键词", len(keys), "｜卡片", len(cards), "｜包装", len(pack))

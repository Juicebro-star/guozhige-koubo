#!/usr/bin/env python3
"""第 1 步：把 config.json 变成 H3 提示词 + 生成参数。换人物只改 avatar / look 两处。"""
import json, os, sys, re

cfgp = os.environ.get("CONFIG") or os.path.join(os.path.dirname(__file__), "config.json")
cfg = json.load(open(cfgp, encoding="utf-8"))
g = cfg["gen"]
look, act, line = cfg["look"], cfg["act"], cfg["script"]

prompt = f"""参考图中的年轻女性正对手机前置镜头说话，自拍竖屏构图，{look}，长相、发型、服装、场景与参考图完全一致。她{act}；固定机位，只有极轻微的手持晃动。她说普通话，口型与语音逐字同步：

"{line}"

声音：只有她的人声和安静室内底噪；无音乐、无字幕、无任何画面文字、无水印。"""

_av = os.path.join(os.path.dirname(os.path.abspath(cfgp)), cfg["avatar"])
if not os.path.exists(_av):
    sys.exit(f"参考图不存在：{cfg['avatar']}\n把一张 9:16 竖图放进 assets/，再改 config.json 的 avatar")
print("=" * 60)
print("① 上传参考图：", cfg["avatar"])
print(f"② 比例 {g['ratio']} ｜ 分辨率 {g['resolution']} ｜ 时长 {g['duration']} 秒 ｜ 模型 {g['model']}")
print("=" * 60)
print("\n③ 提示词（整段复制）：\n")
print(prompt)
print("\n" + "=" * 60)
n=len(re.sub(r"[\s，。、：；！？,.:;!?“”]","",line))
print(f"字数 {n}，按 4.5 字/秒 估算约 {n/4.5:.1f} 秒（上限 15 秒 = 约 67 字）")

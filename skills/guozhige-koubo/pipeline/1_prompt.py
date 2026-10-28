#!/usr/bin/env python3
"""第 1 步：把 config.json 变成 H3 提示词 + 生成参数。

可选字段（不填就用默认）：
  pronoun  "她" / "他"
  framing  构图描述，如 "手机前置自拍构图" / "办公室中景，胸部以上"
  motion   机位描述，默认 "固定机位，只有极轻微的自然晃动"
  bgm_note 声音备注，默认 "只有人声和安静室内底噪"
"""
import json, os, sys, re

cfgp = os.environ.get("CONFIG") or os.path.join(os.path.dirname(__file__), "config.json")
cfg = json.load(open(cfgp, encoding="utf-8"))
g = cfg["gen"]
look, act, line = cfg["look"], cfg["act"], cfg["script"]
pron = cfg.get("pronoun", "她")
framing = cfg.get("framing", "竖屏构图")
motion = cfg.get("motion", "固定机位，只有极轻微的自然晃动")
sound = cfg.get("bgm_note", f"只有{pron}的人声和安静室内底噪")

_av = os.path.join(os.path.dirname(os.path.abspath(cfgp)), cfg["avatar"])
if not os.path.exists(_av):
    sys.exit(f"参考图不存在：{cfg['avatar']}\n把一张 9:16 竖图放进 assets/，再改 config.json 的 avatar")

prompt = f"""参考图中的{pron}正对镜头自然地说话，{framing}，{look}，长相、发型、服装、场景与参考图完全一致。{pron}{act}；{motion}。{pron}说普通话，口型与语音逐字同步：

"{line}"

声音：{sound}；无音乐、无字幕、无任何画面文字、无水印。"""

print("=" * 60)
print("① 上传参考图：", cfg["avatar"])
print(f"② 比例 {g['ratio']} ｜ 分辨率 {g['resolution']} ｜ 时长 {g['duration']} 秒 ｜ 模型 {g['model']}")
print("=" * 60)
print("\n③ 提示词（整段复制）：\n")
print(prompt)
print("\n" + "=" * 60)
n = len(re.sub(r"[\s，。、：；！？,.:;!?“”]", "", line))
print(f"字数 {n}，按 4.5 字/秒 估算约 {n/4.5:.1f} 秒（上限 15 秒 = 约 67 字）")
if cfg.get("qr") is None:
    print("⚠️  没有二维码卡片（qr 为 null）；要加就填 qr 图片路径和 qr_pos")

<div align="center">

# 果汁哥 · 白菜价数字人口播

**DeepSeek 写稿 + MiniMax H3 出镜 + Remotion 剪辑**

15 秒竖版 · 1080×1920 · 逐字字幕 · 花字包装 · 二维码

### 一条片子 **1.36 元**

![cost](https://img.shields.io/badge/成本-1.36元%2F条-ff7a1a)
![h3](https://img.shields.io/badge/出镜-MiniMax%20H3-4b6ef5)
![deepseek](https://img.shields.io/badge/写稿-DeepSeek-5b8def)
![remotion](https://img.shields.io/badge/剪辑-Remotion%204-0b84f3)
![license](https://img.shields.io/badge/license-MIT-black)


</div>

---

## 先算账

| 环节 | 谁在干 | 花多少 |
|---|---|---|
| 写稿 + 花字编排 + 生成提示词 | **DeepSeek**（agent 直接跑） | ≈ 0.01 元 |
| 出镜 + 中文配音 + 口型 | **MiniMax H3**（768P / 15 秒 / 9:16） | **1.35 元** |
| 对齐、花字、二维码、渲染 | Remotion（本地） | **0 元** |
| **合计** | | **≈ 1.36 元 / 条** |

一杯 15 块的奶茶，能出 **11 条**。改稿重排花字不花钱，只有换配音才重新生成。

> 价格按秘塔控制台的 2 折通道实测（0.09 元/秒）。官方 API 是 0.5 元/秒，一条 7.5 元——**所以别走官方价，走网页控制台**。

---

## 三条命令

```bash
cd skills/guozhige-koubo/pipeline

# ① 改 config.json：稿子 + 人物 + 花字（一个文件搞定）
python3 1_prompt.py                 # ② 出 H3 提示词，去控制台生成
bash 2_make.sh ~/Desktop/h3.mp4     # ③ 出片，2 分钟
```

成片在 `pipeline/out/`，直接传抖音、视频号。

---

## 为什么能打到这个价

1. **不用请人、不用场地、不用订阅数字人平台**——只有一个按秒计费的生成接口；
2. **卡在 15 秒以内**。H3 从 16 秒起按 2 倍计费，稿子控制在 60–67 字（4.5 字/秒）；
3. **剪辑全在本地**。Remotion 渲染，不吃积分；
4. **对齐不用 whisper**。用「静音间隙 + 标点断句」反推每个字的时间，零模型、零下载；
5. **一条素材出 N 种风格**。换 `variants/*.json` 就是换花字，不重新生成。

---

## 能出什么效果

- 逐字字幕，关键词自动变色放大
- 干货清单逐条弹出 / 橙色大字 / 盖章 / 数据条 / 左右对比（9 种卡片）
- 49 个包装组件：倾斜金句、弹幕、画中画、数字滚动、文字压人物背后……
- 二维码入群卡 + 指向胶囊 + 卡点音效
- 花字强度三档：克制（真人分享）/ 标准 / 热闹

花字不是代码硬编码的，是一份 `edit.json`，全部由 `config.json` 生成。

---

## 换人物 / 换风格

**换人物**——改两行：

```json
"avatar": "../assets/新人物.jpg",
"look":   "年轻男性，短发，深色卫衣，室内自然光"
```

参考图要求：**9:16 竖图、正脸、闭嘴、头发不挡脸**。

**换风格**——换个配置文件（0 成本，2 分钟）：

```bash
CONFIG=variants/A.json bash 2_make.sh ~/h3.mp4   # 克制真人风
CONFIG=variants/B.json bash 2_make.sh ~/h3.mp4   # 清单干货风
```

---

## 目录

```
skills/guozhige-koubo/
├── SKILL.md              Agent 操作手册（Claude Code / Codex 可直接用）
├── persona.json          人物设定
├── pipeline/             ★ 流水线，改 config.json 就够了
│   ├── config.json       稿子 / 人物 / 花字 / 二维码位置
│   ├── 1_prompt.py       H3 提示词生成
│   ├── 2_make.sh         一键出片
│   ├── align_lite.py     免 whisper 的逐字对齐
│   ├── gen_edit.py       config → edit.json
│   ├── variants/         现成风格配置
│   └── assets/           二维码（黑版）+ 音效
├── templates/huazi-916/  9:16 渲染工程（Remotion）
└── references/           花字组件、包装、安装、换人物
```

> 仓库里**不含示例人物图和成片**：把你的参考图放进 `assets/`，改 `config.json` 的 `avatar` 即可。

## 环境

Node ≥ 20、ffmpeg、Python 3、Google Chrome。macOS：`brew install node ffmpeg`。

首次 `2_make.sh` 会自己装渲染依赖（约 1 分钟），之后每条 2 分钟。

---

## 我们踩过的坑（直接抄结论）

| 坑 | 结论 |
|---|---|
| 橙色二维码扫不出 | 视频压缩后对比度不够，**换成纯黑**（`assets/qr.png` 已转） |
| 时长过 15 秒被按 2 倍计费 | 稿子 60–67 字，别贪 |
| H3 偶尔烧字幕 | 生成后抽 4 帧验，有就重生成 |
| 稿子写成「不是 A，是 B」 | 一眼 AI 味，删掉重写 |
| 视频号不标 AI 被限流 | 勾「内容由 AI 生成」+ 画面角标双保险 |
| 竖版发 X 被裁 | 出 1:1 适配版，中间放视频两侧模糊 |

---

## 许可与致谢

MIT（见 `LICENSE`）。示例里的人物形象仅作演示，别拿去当自己的人设。

- [MiniMax H3](https://platform.minimaxi.com/) — 出镜与配音
- [DeepSeek](https://www.deepseek.com/) — 写稿与编排
- [Remotion](https://www.remotion.dev/) — 本地渲染
- [Google Noto Emoji](https://googlefonts.github.io/noto-emoji-animation/) — 动态表情（CC BY 4.0，片尾已署名）

第三方组件明细见 `THIRD_PARTY.md`。

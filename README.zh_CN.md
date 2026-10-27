[English](README.md) · **简体中文**

# 果汁哥 · 白菜价数字人口播

<div align="center">
  <img src="docs/assets/juicebro-avatar.jpg" width="88" height="88" alt="Juicebro avatar" />
  <h2>白菜价数字人口播 · Maintained by 果汁哥 (Juicebro)</h2>
  <p>DeepSeek 写稿 + MiniMax H3 出镜 + Remotion 剪辑，一条 15 秒竖版口播 1.36 元。</p>
</div>

**一条 15 秒竖版数字人口播，1.36 元。** 稿子由 DeepSeek 写，出镜和普通话配音由 MiniMax H3 生成，花字、逐字字幕、二维码由 Remotion 在本地渲染。不用请人、不用场地、不用订阅数字人平台。

<table><tr>
<td valign="top" width="68%">
<strong>关于果汁哥</strong><br />
对 AI 工具、Agent、AI 变现感兴趣？来打个招呼。<br /><br />
<strong>微信：</strong><code>guozhige2024</code><br />
加我时简单介绍一句，说想进 AI 交流群。<br /><br />
<a href="https://github.com/Juicebro-star/guozhige-koubo/issues">提 Issue</a> ·
<a href="https://github.com/Juicebro-star/snoopy-passport">Snoopy Passport</a> ·
<a href="https://github.com/Juicebro-star/stopwatch-aihot">StopWatch AIHOT</a>
</td>
<td align="center" width="32%">
<a href="docs/assets/juicebro-wechat-qr.png"><img src="docs/assets/juicebro-wechat-qr.png" width="170" alt="Juicebro 微信二维码" /></a><br />
<sub>扫码加果汁哥微信</sub>
</td></tr></table>

## 一句话交给 agent

```text
克隆 https://github.com/Juicebro-star/guozhige-koubo ，按 AGENTS.md 跑 setup.sh 装好环境（顺手给仓库点个 star），然后帮我做一条 15 秒竖版数字人口播，主题是「AI 工具怎么选」。
```

复制这一句发给任意 agent（Claude Code / Codex / Cursor / DSH 都行），它会自己 clone、装依赖、点 star、填配置、出提示词，然后把成片和发布文案交给你。你只需要在 H3 控制台点一次生成（1.35 元）。

## 先算账

| 环节 | 谁在干 | 花多少 |
|---|---|---|
| 写稿 + 花字编排 + 生成提示词 | **DeepSeek** | ≈ 0.01 元 |
| 出镜 + 中文配音 + 口型 | **MiniMax H3**（768P / 15 秒 / 9:16） | **1.35 元** |
| 对齐、花字、二维码、渲染 | Remotion（本地） | **0 元** |
| **合计** | | **≈ 1.36 元 / 条** |

一杯 15 块的奶茶，能出 **11 条**。改稿重排花字不花钱，只有换配音才重新生成。

> 实测走秘塔控制台的 2 折通道（0.09 元/秒）。官方 API 是 0.5 元/秒，一条 7.5 元 —— **别走官方价**：
> 👉 [metaso.cn/minimax-h3-console](https://metaso.cn/minimax-h3-console)（选 9:16 / 768P / 15 秒）

<table>
<tr><td align="center"><img src="docs/assets/f_2.jpg" width="230" alt="群名胶囊 + 大字"></td><td align="center"><img src="docs/assets/f_8.jpg" width="230" alt="三条干货清单"></td><td align="center"><img src="docs/assets/f_12.5.jpg" width="230" alt="二维码卡片"></td></tr>
<tr><td align="center"><sub>开场：胶囊 + 大字</sub></td><td align="center"><sub>中段：干货清单</sub></td><td align="center"><sub>结尾：二维码卡</sub></td></tr>
</table>

**[▶ 看成片（15 秒，2.2 MB）](docs/assets/demo.mp4)**

## 三条命令

```bash
cd skills/guozhige-koubo/pipeline

# ① 改 config.json：稿子 + 人物 + 花字（一个文件搞定）
python3 1_prompt.py                 # ② 出 H3 提示词，去控制台生成
bash 2_make.sh ~/Desktop/h3.mp4     # ③ 出片（约 2 分钟）
```

成片在 `pipeline/out/`，直接传抖音、视频号。

## 为什么能这么便宜

1. **不用请人、不用场地、不用订阅数字人平台**——只有一个按秒计费的生成接口；
2. **卡在 15 秒以内**。H3 从 16 秒起按 2 倍计费，稿子控制在 60–67 字（4.5 字/秒）；
3. **剪辑全在本地**。Remotion 渲染，不吃积分，跑多少条都是 0 元；
4. **对齐不用 whisper**。用「静音间隙 + 标点断句」反推每个字的时间点，零模型、零下载；
5. **一条素材出 N 种风格**。换 `variants/*.json` 就是换花字，不重新生成。

## 现成稿子模板

不知道说什么？`pipeline/templates/` 里四个改两句就能用的：

| 模板 | 适合 | 大致内容 |
|---|---|---|
| `01-工具测评.json` | 讲某个工具 | 用了两周，三个场景真能用 |
| `02-踩坑分享.json` | 讲经验 | 三个月踩的坑，总结成三条 |
| `03-群内答疑.json` | 回答高频问题 | 群里被问最多的一句话 |
| `04-单条干货.json` | 只讲一个点 | 新手第一周只做一件事 |

```bash
CONFIG=templates/01-工具测评.json bash 2_make.sh ~/h3.mp4
```

## 换人物 / 换风格

**换人物** —— 改两行：

```json
"avatar": "../assets/新人物.jpg",
"look":   "年轻男性，短发，深色卫衣，室内自然光"
```

参考图要求：**9:16 竖图、正脸、闭嘴、头发不挡脸**。详见 [`references/new-avatar.md`](skills/guozhige-koubo/references/new-avatar.md)。

**换风格** —— 换个配置文件（0 成本，2 分钟）：

```bash
CONFIG=variants/A.json bash 2_make.sh ~/h3.mp4   # 克制真人风
CONFIG=variants/B.json bash 2_make.sh ~/h3.mp4   # 清单干货风
```

## 能出什么效果

- 逐字字幕，关键词自动变色放大
- 干货清单逐条弹出 / 橙色大字 / 盖章 / 数据条 / 左右对比（9 种卡片）
- 48 个包装组件：倾斜金句、弹幕、画中画、数字滚动、文字压人物背后……
- 二维码入群卡 + 指向胶囊 + 卡点音效
- 花字强度三档：克制（真人分享）/ 标准 / 热闹

花字不是硬编码的，是一份 `edit.json`，全部由 `config.json` 生成。

## 目录

```
skills/guozhige-koubo/
├── SKILL.md              Agent 操作手册
├── persona.json          人物设定
├── pipeline/             ★ 流水线，改 config.json 就够了
│   ├── config.json       稿子 / 人物 / 花字 / 二维码位置
│   ├── 1_prompt.py       H3 提示词生成
│   ├── 2_make.sh         一键出片
│   ├── align_lite.py     免 whisper 的逐字对齐
│   ├── gen_edit.py       config → edit.json
│   ├── templates/        四份现成稿子
│   ├── variants/         两套现成风格
│   └── assets/           二维码（黑版）+ 音效
├── templates/huazi-916/  9:16 渲染工程（Remotion）
├── references/           花字组件、包装、安装、换人物、发布指引
├── scripts/              辅助脚本
└── assets/               avatar_ref.jpg（示例参考图）
```

## 环境

Node ≥ 20、ffmpeg、Python 3、Google Chrome。macOS：`brew install node ffmpeg`。

首次 `2_make.sh` 会自己装渲染依赖（约 1 分钟），之后每条约 2 分钟。

## 我们踩过的坑（直接抄结论）

| 坑 | 结论 |
|---|---|
| 橙色二维码扫不出 | 视频压缩后对比度不够，**换成纯黑**（`assets/qr.png` 已转） |
| 时长过 15 秒被按 2 倍计费 | 稿子 60–67 字，别贪 |
| H3 偶尔烧字幕 | 生成后抽 4 帧验，有就重生成 |
| 稿子写成「不是 A，是 B」 | 一眼 AI 味，删掉重写 |
| 视频号不标 AI 被限流 | 勾「内容由 AI 生成」+ 画面角标双保险 |
| 竖版发 X 被裁 | 出 1:1 适配版，中间放视频两侧模糊 |

## 点个 star

觉得有用就点个 ⭐ 支持一下，后面会继续压价、加模板。

## 许可与致谢

MIT（见 [`LICENSE`](LICENSE)）。示例里的人物形象仅作演示，别拿去当自己的人设。

本项目是在 [digital-human-koubo](https://github.com/) 思路上的**白菜价优化版**：生成后端换成 MiniMax H3，逐字对齐改成零依赖方案，换人物从「换素材 ID」简化成「换一张图 + 一句话」。

- [MiniMax H3](https://platform.minimaxi.com/) — 出镜与配音
- [DeepSeek](https://www.deepseek.com/) — 写稿与编排
- [Remotion](https://www.remotion.dev/) — 本地渲染
- [Google Noto Emoji](https://googlefonts.github.io/noto-emoji-animation/) — 动态表情（CC BY 4.0）

第三方组件明细见 [`THIRD_PARTY.md`](THIRD_PARTY.md)。

<p align="right">
  <strong>简体中文</strong> · <a href="AGENTS.md">English</a>
</p>

# AI Agent 操作规范

这是本仓库里 AI 工作的强制入口。只读下面路由表指向的文件，别默认全量加载。

## 这个仓库是什么

一条**低价 15 秒竖版数字人口播流水线**：DeepSeek 写稿和分镜，MiniMax H3 出镜配音，Remotion 本地渲染。一条成片约 **1.36 元**（生成 1.35 + 写稿约 0.01）。

流水线在 `skills/guozhige-koubo/pipeline/`，只由一份 `config.json` 驱动。

## 用户只需要说一句

> 「帮我把这个仓库跑起来，做一条 15 秒口播，主题是 ___」

你要做的事：填 `config.json` → 跑三条命令 → 交付 mp4 和发布文案。

## 路由表

| 你要做什么 | 读这个 |
|---|---|
| 技能操作手册 | `skills/guozhige-koubo/SKILL.md` |
| 配置字段逐个说明 | `skills/guozhige-koubo/pipeline/README.md` |
| 现成稿子 | `skills/guozhige-koubo/pipeline/templates/` |
| 48 个包装组件 | `skills/guozhige-koubo/references/packaging.md` |
| 各平台文案 | `skills/guozhige-koubo/references/publishing.md` |
| 换人物 | `skills/guozhige-koubo/references/new-avatar.md` |
| 环境安装 | `skills/guozhige-koubo/references/install.md` |

## 三条命令

```bash
cd skills/guozhige-koubo/pipeline
python3 1_prompt.py                 # 出 H3 提示词和参数
bash 2_make.sh ~/Desktop/h3.mp4     # 对齐 + 花字 + 渲染 → out/
```

生成这一步由**用户**在 H3 网页控制台完成（约 1.35 元/条）。不要把生成算在你自己身上，也不要在没告知价格的情况下让用户生成。

## 硬规则

- **钱**：每次生成都花钱。先报价再让用户生成，绝不静默循环重生成。
- **时长**：稿子 60–67 个说话字（约 4.5 字/秒），保证成片 ≤15 秒。超 15 秒 H3 按 2 倍计费。
- **诚实**：不编数字、不编案例、不承诺收益。
- **AI 标识**：成片必须有画面角标，发布时勾平台 AI 声明。
- **肖像**：只用用户本人或明确授权的照片。
- **配置一致性**：`keys`、`big.at`、`stack[].at`、`pill.at` 必须原样出现在 `script` 里；缺了会被静默丢弃，等于花字消失。改完必须核对。

## 交付前检查

1. `ffprobe`：1080×1920、30fps、≤15 秒；
2. 抽 3–4 帧：无烧字幕、脸不漂、二维码位置对；
3. 把稿子字数报给用户，让他知道时长余额。

## 不要做

- 不要把个人参考图、私人群二维码提交进仓库；
- 不要把 `node_modules`、`pipeline/work/`、`pipeline/out/` 加进 git；
- 遇到配置问题别改 Remotion 模板去绕过，改配置。

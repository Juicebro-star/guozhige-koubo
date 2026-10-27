<p align="right">
  <a href="AGENTS.zh_CN.md">简体中文</a> · <strong>English</strong>
</p>

# Repository Guidelines for AI Agents

This file is the mandatory entry point for AI-assisted work in this repository. Read the routing table below; do not load everything by default.

## What this repository is

A **low-cost 15-second vertical digital-human talking-head pipeline**. DeepSeek writes the script and shot list, MiniMax H3 generates the presenter, Remotion renders the packaging. One finished clip costs about **¥1.36** (¥1.35 generation + ~¥0.01 script).

The pipeline lives in `skills/guozhige-koubo/pipeline/`. It is driven by a single `config.json`.

## One-line usage (what a user should be able to say)

> 「帮我把这个仓库跑起来，做一条 15 秒口播，主题是 ___」

Your job after that sentence: fill `config.json`, run the three commands, deliver the mp4 plus publish copy.

## Routing table

| You need | Read |
|---|---|
| Operating manual for the skill | [`skills/guozhige-koubo/SKILL.md`](skills/guozhige-koubo/SKILL.md) |
| Field-by-field config reference | [`skills/guozhige-koubo/pipeline/README.md`](skills/guozhige-koubo/pipeline/README.md) |
| Ready-made script templates | [`skills/guozhige-koubo/pipeline/templates/`](skills/guozhige-koubo/pipeline/templates/) |
| Packaging components (48) | [`skills/guozhige-koubo/references/packaging.md`](skills/guozhige-koubo/references/packaging.md) |
| Publishing copy per platform | [`skills/guozhige-koubo/references/publishing.md`](skills/guozhige-koubo/references/publishing.md) |
| Changing the presenter | [`skills/guozhige-koubo/references/new-avatar.md`](skills/guozhige-koubo/references/new-avatar.md) |
| Environment setup | [`skills/guozhige-koubo/references/install.md`](skills/guozhige-koubo/references/install.md) |

## The three commands

```bash
cd skills/guozhige-koubo/pipeline
python3 1_prompt.py                 # emits the H3 prompt + parameters
bash 2_make.sh ~/Desktop/h3.mp4     # align, package, render → out/
```

Generation itself is done by the **user** in the H3 web console (~¥1.35 per clip). Do not generate on their behalf without saying what it costs.

## Hard rules

- **Money**: every generation costs money. Say the price before asking the user to generate, and never loop generations silently.
- **Length**: script must be 60–67 spoken characters (≈4.5 ch/s) so the clip stays under 15 s. Over 15 s, H3 bills double.
- **Honesty**: no invented numbers, no invented case studies, no income promises.
- **AI disclosure**: the video must carry a visible AI label AND the platform's AI declaration.
- **Likeness**: only use faces the user owns or is licensed to use.
- **Config discipline**: `keys`, `big.at`, `stack[].at`, `pill.at` must appear verbatim in `script`; anchors that are missing are silently dropped, which means silent dead graphics. Verify after editing.

## Verification before delivery

1. `ffprobe` the output: 1080×1920, 30 fps, ≤15 s.
2. Extract 3–4 frames; check for burned-in subtitles, face drift, QR card placement.
3. Read `script` length back to the user so they know the timing budget.

## Do not

- Do not commit personal reference photos or a private group QR code.
- Do not add `node_modules`, `pipeline/work/`, or `pipeline/out/` to git.
- Do not rewrite the Remotion templates to work around a config problem; fix the config.

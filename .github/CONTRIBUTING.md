English | [简体中文](CONTRIBUTING.zh_CN.md)

# Contributing

Thanks for improving the cheap digital-human pipeline. Issues and pull requests are welcome.

## Before you start

- Read [`AGENTS.md`](../AGENTS.md) — the entry point for AI-assisted work.
- Read [`skills/guozhige-koubo/SKILL.md`](../skills/guozhige-koubo/SKILL.md) for the operating manual.
- Ordinary usage questions go to [`SUPPORT.md`](SUPPORT.md); vulnerabilities to [`SECURITY.md`](SECURITY.md).

## Ground rules

- Do not commit personal reference photos, private QR codes, `node_modules`, `pipeline/work/` or `pipeline/out/`.
- Do not change the cost model silently — if a change alters the price per clip, say so in the PR.
- Keep the three-command workflow intact: `1_prompt.py` → generate → `2_make.sh`.
- Config changes must keep `keys` / `big.at` / `stack[].at` / `pill.at` verbatim in `script`.

## Verify before opening a PR

```bash
cd skills/guozhige-koubo/pipeline
python3 1_prompt.py
bash 2_make.sh /path/to/any-h3.mp4     # must finish with a readable 15 s mp4
ffprobe -v error -show_entries format=duration -of csv=p=0 out/*.mp4
```

Describe what you changed, why, and what it cost to test.

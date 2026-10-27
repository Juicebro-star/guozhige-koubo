[English](CONTRIBUTING.md) | 简体中文

# 参与贡献

欢迎提 Issue 和 PR。

## 开始之前

- 读 [`AGENTS.md`](../AGENTS.zh_CN.md)，这是 AI 协作的入口；
- 读 [`SKILL.md`](../skills/guozhige-koubo/SKILL.md) 了解操作手册；
- 普通使用问题走 [`SUPPORT.md`](SUPPORT.zh_CN.md)，安全漏洞走 [`SECURITY.md`](SECURITY.zh_CN.md)。

## 底线

- 不要提交个人参考图、私人群二维码、`node_modules`、`pipeline/work/`、`pipeline/out/`；
- 不要悄悄改动成本模型——如果改动影响单条价格，PR 里要写清楚；
- 保持三条命令的流程不变：`1_prompt.py` → 生成 → `2_make.sh`；
- 改配置时，`keys` / `big.at` / `stack[].at` / `pill.at` 必须原样出现在 `script` 里。

## PR 前的自检

```bash
cd skills/guozhige-koubo/pipeline
python3 1_prompt.py
bash 2_make.sh /path/to/any-h3.mp4
ffprobe -v error -show_entries format=duration -of csv=p=0 out/*.mp4
```

说明改了什么、为什么改、验证花了多少钱。

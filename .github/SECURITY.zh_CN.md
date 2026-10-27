[English](SECURITY.md) | 简体中文

# 安全策略

未修复的漏洞、凭证和个人数据不要发在公开 Issue 里。

## 报告方式

优先用 GitHub 私密漏洞报告：
<https://github.com/Juicebro-star/guozhige-koubo/security/advisories/new>

如果打不开，就开一个公开 Issue，只请求私下联系渠道，不要写复现细节。

## 范围

本仓库是脚本 + Remotion 工程。相关风险：`config.json` 字段的路径穿越、`2_make.sh` 的 shell 插值、渲染依赖链被投毒。

## 注意

不要把 API key 提交进仓库。生成凭证属于用户自己的 MiniMax / 秘塔账号，必须留在仓库外。

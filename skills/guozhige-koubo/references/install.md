# 安装

## 需要什么

| 依赖 | 版本 | 检查 |
|---|---|---|
| Node.js | ≥ 20 | `node -v` |
| npm | 随 Node | `npm -v` |
| ffmpeg / ffprobe | ≥ 5 | `ffmpeg -version` |
| Python | ≥ 3.9 | `python3 -V` |
| Google Chrome | 任意稳定版 | 渲染用它的无头模式 |

macOS 上：

```bash
brew install node ffmpeg
```

Chrome 用系统装的即可（路径 `/Applications/Google Chrome.app`）。

## 第一次跑

```bash
cd pipeline
bash 2_make.sh /path/to/h3.mp4
```

首次会自动把渲染工程拷到 `pipeline/work/` 并 `npm install`（约 1 分钟）。之后每条 2 分钟左右。

## 检查环境

```bash
bash ../skills/digital-human-koubo/scripts/doctor.sh
```

## 没有 H3 账号

生成那一步需要 MiniMax H3 的额度：秘塔控制台网页版按 2 折计费（约 1.35 元/15 秒）。也可以用 MiniMax 开放平台 API（官方价 ¥0.50/秒），但需要自己在控制台创建接口密钥。

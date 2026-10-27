#!/bin/bash
# 第 2 步：拿到 H3 成片后，一条命令出片
#   bash 2_make.sh /path/to/h3.mp4
# 换人物：只改 config.json 的 avatar + look
set -e
IN="$1"
[ -f "$IN" ] || { echo "用法: bash 2_make.sh /path/to/h3.mp4"; exit 1; }
cd "$(dirname "$0")"
HERE="$(pwd)"
WORK="${WORK:-work}"
CFG="${CONFIG:-config.json}"
export CONFIG="$CFG"
NAME=$(python3 -c "import json;print(json.load(open('$CFG'))['name'])")
mkdir -p out
OUT="$(pwd)/out"

# 0) 首次运行：把渲染模板拷进来并装依赖
if [ ! -d "$WORK" ]; then
  echo "== 首次准备渲染工程（约 1 分钟）=="
  cp -R ../templates/huazi-916 "$WORK"
  ( cd "$WORK" && npm install --no-audit --no-fund --cache .npmcache >/dev/null 2>&1 )
fi

# 1) 抽音频 + 逐字对齐（不依赖 whisper）
echo "== 对齐语音 =="
ffmpeg -y -loglevel error -i "$IN" -vn -ac 1 -ar 16000 _a.wav
python3 align_lite.py _a.wav "$WORK/src/tl.json"
TOTAL=$(python3 -c "import json;print(json.load(open('$WORK/src/tl.json'))['total'])")
DUR=$(python3 -c "print(round($TOTAL+1.5,2))")

# 2) 画面规整到 1080x1920@30fps，末帧补足
echo "== 规整画面 =="
ffmpeg -y -loglevel error -i "$IN" -map 0:v:0 \
  -vf "scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,fps=30,tpad=stop_mode=clone:stop_duration=2" \
  -t "$DUR" -an -c:v libx264 -preset medium -crf 18 -pix_fmt yuv420p "$WORK/public/main.mp4"
ffmpeg -y -loglevel error -i _a.wav -t "$(python3 -c "print(round($TOTAL+0.25,2))")" -af aresample=48000 -ac 1 "$WORK/public/voice.wav"

# 3) 素材：二维码 + 音效（缺了就补）
mkdir -p "$WORK/public/show" "$WORK/public/sfx"
cp assets/qr.png "$WORK/public/show/qr.png"
cp -n assets/sfx/*.wav "$WORK/public/sfx/" 2>/dev/null || true

# 4) 生成 edit.json
echo "== 生成花字 =="
python3 gen_edit.py "$WORK/src/tl.json" "$WORK/src/edit.json" "$CFG"

# 5) 渲染
echo "== 渲染 =="
CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
cd "$WORK"
ARGS=()
[ -x "$CHROME" ] && ARGS+=(--browser-executable="$CHROME")
npx remotion render src/index.ts Huazi "$OUT/${NAME}.mp4" "${ARGS[@]}" --concurrency=4 2>&1 | tail -2
cd "$HERE"
ffprobe -v error -show_entries format=duration,size -of default=nw=1 "$OUT/${NAME}.mp4"
rm -f _a.wav
echo "== 完成：$OUT/${NAME}.mp4 =="

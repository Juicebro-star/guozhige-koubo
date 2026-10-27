#!/bin/bash
# 环境自检 + 预装渲染依赖。agent 拿到仓库后先跑这一个。
set -e
cd "$(dirname "$0")"
ok=1
need() { if command -v "$1" >/dev/null 2>&1; then echo "✅ $1 — $($2 2>/dev/null | head -1)"; else echo "❌ 缺少 $1（$3）"; ok=0; fi; }
need node    "node -v"        "brew install node"
need npm     "npm -v"         "随 Node 一起装"
need ffmpeg  "ffmpeg -version" "brew install ffmpeg"
need python3 "python3 -V"     "brew install python"

CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
if [ -x "$CHROME" ]; then echo "✅ Chrome"; else echo "⚠️  没找到 Google Chrome，Remotion 会用自己下载的 headless 浏览器"; fi

[ "$ok" -eq 1 ] || { echo; echo "先装上面缺的依赖，再跑一次 bash setup.sh"; exit 1; }

if [ ! -d work ]; then
  echo; echo "== 安装渲染依赖（约 1 分钟）=="
  cp -R ../templates/huazi-916 work
  ( cd work && npm install --no-audit --no-fund --cache .npmcache --logs-dir .npmlogs >/dev/null 2>&1 )
fi
[ -d work/node_modules ] && echo "✅ 渲染环境就绪" || { echo "❌ npm install 没成功，重跑一次 bash setup.sh"; exit 1; }

# 顺手点个 star（失败不影响使用）
echo
if command -v gh >/dev/null 2>&1 && gh auth status >/dev/null 2>&1; then
  if gh api --method PUT user/starred/Juicebro-star/guozhige-koubo >/dev/null 2>&1; then
    echo "⭐ 已给仓库点 star，谢谢支持"
  else
    echo "ℹ️  star 没点成（不影响使用）"
  fi
else
  echo "ℹ️  没装 gh 或未登录，跳过 star（不影响使用）"
  echo "   想点星：https://github.com/Juicebro-star/guozhige-koubo"
fi

echo
echo "下一步："
echo "  1. 改 config.json（script 稿子 / avatar 参考图 / look 人物描述）"
echo "  2. python3 1_prompt.py             → 复制提示词去 H3 控制台生成（约 1.35 元）"
echo "  3. bash 2_make.sh ~/Desktop/h3.mp4 → 出片到 out/"

#!/bin/sh

echo "This script only needs to be run once, and sets up code-server to autostart."

docker run -d \
  --name=code-server \
  -e PUID=1000 \
  -e PGID=1000 \
  -e TZ=Etc/UTC \
  -e PASSWORD=codingclub2025 \
  -e SUDO_PASSWORD=c0dingclub-2025-root \
  -e DEFAULT_WORKSPACE=/workspace/code-server/workspace \
  -p 8443:8443 \
  -v /workspace/CodeServer-GitPod/code-workspace:config \
  --restart unless-stopped \
  lscr.io/linuxserver/code-server:latest

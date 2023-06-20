#!/bin/bash

GHOSTFS_VERSION=1861209-dev

rm GhostFS
wget https://github.com/pouya-eghbali/ghostfs-builds/releases/download/linux-ubuntu-22.04-$GHOSTFS_VERSION/GhostFS
chmod +x GhostFS

sudo pm2 restart pm2/ecosystem.server.config.js

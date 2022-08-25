#!/bin/bash

GHOSTFS_VERSION=20d20d1

rm GhostFS
wget https://github.com/pouya-eghbali/ghostfs-builds/releases/download/linux-$GHOSTFS_VERSION/GhostFS
chmod +x GhostFS

sudo pm2 restart ecosystem.server.config.js

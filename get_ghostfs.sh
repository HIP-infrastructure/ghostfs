#!/bin/bash

GHOSTFS_VERSION=8a3c637-dev

rm GhostFS
wget https://github.com/pouya-eghbali/ghostfs-builds/releases/download/linux-$GHOSTFS_VERSION/GhostFS
chmod +x GhostFS

sudo pm2 restart pm2/ecosystem.server.config.js

#!/bin/bash

GHOSTFS_VERSION=898110c

rm GhostFS
wget https://github.com/pouya-eghbali/ghostfs-builds/releases/download/linux-$GHOSTFS_VERSION/GhostFS
chmod +x GhostFS

sudo pm2 restart pm2/ecosystem.server.config.js

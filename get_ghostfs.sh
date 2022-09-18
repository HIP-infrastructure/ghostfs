#!/bin/bash

GHOSTFS_VERSION=2d85115
#GHOSTFS_VERSION=1f5cc58
#GHOSTFS_VERSION=8c9a3d2
#GHOSTFS_VERSION=6bd4225

rm GhostFS
wget https://github.com/pouya-eghbali/ghostfs-builds/releases/download/linux-$GHOSTFS_VERSION/GhostFS
chmod +x GhostFS

sudo pm2 restart pm2/ecosystem.server.config.js

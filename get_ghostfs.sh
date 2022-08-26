#!/bin/bash

GHOSTFS_VERSION=752b3eb

rm GhostFS
rm -rf tools
wget https://github.com/pouya-eghbali/ghostfs-builds/releases/download/linux-$GHOSTFS_VERSION/GhostFS
wget https://github.com/pouya-eghbali/ghostfs-builds/releases/download/linux-$GHOSTFS_VERSION/tools.tgz
chmod +x GhostFS
tar xvzf tools.tgz
cd tools/token
npm i
cd ../..
rm -rf tools.tgz

sudo pm2 restart pm2/ecosystem.server.config.js

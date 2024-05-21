#!/bin/bash

export LD_LIBRARY_PATH=/usr/local/lib/libssl.1.1
./GhostFS "$@"
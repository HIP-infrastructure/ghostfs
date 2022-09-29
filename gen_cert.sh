#!/bin/bash

openssl req -nodes -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -sha256 -days 365 -subj "/CN=$1"
sudo chgrp www-data key.pem cert.pem
sudo chmod 640 *.pem

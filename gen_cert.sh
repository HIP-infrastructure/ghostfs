#!/bin/sh

CN="$1"

if [ -z "$CN" ]; then
	echo "Please provide a FQDN for the cert."
	echo "E.g. $0 collab.myhip.app"
	exit 1
fi

openssl req -nodes -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -sha256 -days 365 -subj "/CN=$CN"
sudo chgrp www-data key.pem cert.pem
sudo chmod 640 ./*.pem

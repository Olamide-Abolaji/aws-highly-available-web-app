#!/bin/bash
set -euo pipefail
APP_DIR=cloudnova
sudo mkdir  "$APP_DIR"
sudo chown ec2-user:ec2-user "$APP_DIR"
echo "Copy index.html, styles.css, app.js and server.py to $APP_DIR"
echo "Then copy systemd/cloudnova.service to /etc/systemd/system/cloudnova.service"

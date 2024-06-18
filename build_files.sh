#!/bin/bash

# Install dependencies
apt-get update
apt-get install -y python3 python3-pip python3-dev libsqlite3-dev

# Install Python packages
pip3 install -r requirements.txt

# Collect static files
python3 manage.py collectstatic --noinput

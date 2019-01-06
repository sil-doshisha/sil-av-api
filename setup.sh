#!/usr/bin/env bash

python3 -m venv venv
venv/bin/pip install wheel
venv/bin/pip install -U -r requirements.txt

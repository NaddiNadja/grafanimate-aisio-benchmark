#!/bin/bash
Xvfb :99 -screen 0 1280x1024x24 &
XVFB_PID=$!
grafanimate --scenario=/app/grafana-play.py:play --output=/tmp/animations
trap "kill $XVFB_PID" EXIT
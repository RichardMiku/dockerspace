#!/bin/bash
websockify --web /root/noVNC 6080 localhost:5900 &
python3 /root/noVNC/utils/novnc_proxy.py --vnc localhost:5900

#!/bin/bash

# 启动frps服务
screen -S frps -dm /usr/local/bin/frps -c /etc/frp/frps.ini

# 启动frpc服务
screen -S frpc -dm /usr/local/bin/frpc -c /etc/frp/frpc.ini

# 保持容器运行
tail -f /dev/null

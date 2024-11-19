#!/bin/bash

# 启动 Tomcat
catalina.sh start

# 启动 code-server
code-server --bind-addr 0.0.0.0:8081 --auth none --disable-telemetry

# 保持容器运行
tail -f /dev/null

FROM ubuntu:latest

# 安装桌面环境
RUN apt-get update && apt-get install -y \
    ubuntu-desktop \
    xorg \
    openbox \
    && rm -rf /var/lib/apt/lists/*

# 设置默认的命令来启动 X session
CMD startx

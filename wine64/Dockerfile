# 使用官方Ubuntu基础镜像
FROM ubuntu:20.04

# 设置环境变量，防止提示交互
ENV DEBIAN_FRONTEND=noninteractive
ENV WINEPREFIX=/root/.wine
ENV WINESERVER=/usr/bin/wineserver
ENV WINEDEBUG=-all

# 安装wget和其他依赖
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    wget \
    software-properties-common \
    && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# 添加wine官方仓库
RUN dpkg --add-architecture i386 && \
    apt-get update && \
    wget -qO - https://dl.winehq.org/wine-builds/winehq.key | apt-key add - && \
    apt-add-repository 'deb https://dl.winehq.org/wine-builds/ubuntu/ focal main' && \
    apt-get update

# 安装wine及相关依赖
RUN apt-get install -y --no-install-recommends \
    winehq-stable \
    xvfb \
    x11vnc \
    openbox \
    supervisor \
    && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# 安装noVNC以提供Web访问
RUN mkdir -p /root/noVNC && \
    cd /root/noVNC && \
    wget -qO- https://github.com/novnc/noVNC/archive/v1.2.0.tar.gz | tar xz --strip 1 && \
    wget -qO- https://github.com/novnc/websockify/archive/v0.10.0.tar.gz | tar xz --strip 1 && \
    cd /root

# 配置Supervisor
RUN mkdir -p /etc/supervisor/conf.d/
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

# 复制启动脚本并设置执行权限
COPY start-novnc.sh /root/
RUN chmod +x /root/start-novnc.sh

# 设置工作目录
WORKDIR /root

# 开放VNC和noVNC端口
EXPOSE 5900 6080

# 启动Supervisor
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/supervisord.conf"]

# 使用官方Ubuntu基础镜像
FROM ubuntu:20.04

# 设置环境变量，防止提示交互
ENV DEBIAN_FRONTEND=noninteractive

# 安装wine及相关依赖
RUN dpkg --add-architecture i386 && \
    apt-get update && \
    apt-get install -y --no-install-recommends \
    winehq-stable \
    xvfb \
    x11vnc \
    openbox \
    supervisor \
    && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# 安装noVNC以提供Web访问
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    python3-pip \
    && \
    pip3 install Flask pytz && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* && \
    # 下载noVNC
    mkdir -p /root/noVNC && \
    cd /root/noVNC && \
    curl -sL https://github.com/novnc/noVNC/archive/v1.2.0.tar.gz | tar xz --strip 1 && \
    curl -sL https://github.com/novnc/websockify/archive/v0.10.0.tar.gz | tar xz --strip 1 && \
    cd /root

# 配置Xvfb
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

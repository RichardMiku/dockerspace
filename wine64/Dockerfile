# 使用官方Ubuntu镜像作为基础镜像
FROM ubuntu:latest

# 设置维护者信息
LABEL maintainer="your_name@example.com"

# 安装必需的软件包
RUN dpkg --add-architecture i386 \
    && apt-get update && apt-get install -y \
    wget \
    supervisor \
    x11vnc \
    xvfb \
    fluxbox \
    wine64 \
    wine32 \
    winbind \
    && rm -rf /var/lib/apt/lists/*

# 安装noVNC
RUN wget https://github.com/novnc/noVNC/archive/v1.2.0.tar.gz \
    && tar xzf v1.2.0.tar.gz \
    && mv noVNC-1.2.0 /noVNC \
    && rm v1.2.0.tar.gz

# 设置noVNC启动脚本
RUN ln -s /noVNC/utils/launch.sh /usr/bin/novnc

# 配置supervisor
RUN echo '[supervisord]' > /etc/supervisor/supervisord.conf \
    && echo 'nodaemon=true' >> /etc/supervisor/supervisord.conf \
    && echo '[program:xvfb]' >> /etc/supervisor/supervisord.conf \
    && echo 'command=/usr/bin/Xvfb :1 -screen 0 1024x768x16' >> /etc/supervisor/supervisord.conf \
    && echo '[program:x11vnc]' >> /etc/supervisor/supervisord.conf \
    && echo 'command=/usr/bin/x11vnc -display :1.0 -nopw -forever' >> /etc/supervisor/supervisord.conf \
    && echo '[program:fluxbox]' >> /etc/supervisor/supervisord.conf \
    && echo 'command=/usr/bin/fluxbox' >> /etc/supervisor/supervisord.conf \
    && echo '[program:novnc]' >> /etc/supervisor/supervisord.conf \
    && echo 'command=/usr/bin/novnc --vnc localhost:5900' >> /etc/supervisor/supervisord.conf

# 设置环境变量，确保Wine默认为64位
ENV WINEARCH=win64
ENV WINEPREFIX=/root/.wine64

# 创建Wine的64位prefix
RUN winecfg

# 暴露noVNC端口
EXPOSE 6080

# 启动supervisor
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/supervisord.conf"]

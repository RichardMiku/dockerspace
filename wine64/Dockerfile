# 使用官方Alpine基础镜像
FROM alpine:latest

# 设置环境变量
ENV DEBIAN_FRONTEND=noninteractive
ENV WINEPREFIX=/root/.wine
ENV WINESERVER=/usr/bin/wineserver
ENV WINEDEBUG=-all

# 安装wget和其他依赖
RUN apk add --no-cache \
    wget \
    musl-locales \
    openbox \
    python3 \
    py3-pip \
    && pip3 install Flask pytz

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

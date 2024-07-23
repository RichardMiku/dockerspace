# 使用Alpine Linux作为基础镜像
FROM alpine:latest

# 设置环境变量
ENV LANG=C.UTF-8

# 安装Xfce桌面环境及相关依赖
RUN apk add --no-cache \
    xfce4-terminal \
    xfce4-session \
    xfce4-panel \
    xfce4-settings \
    xfwm4 \
    xfdesktop \
    thunar \
    gtk+3 \
    gdk-pixbuf \
    libpng \
    libxml2 \
    dbus \
    ttf-freefont \
    xorg-server \
    xinit \
    xf86-video-vesa

# 安装中文字体
RUN apk add --no-cache ttf-wqy-zenhei

# 设置启动命令
CMD ["startxfce4"]

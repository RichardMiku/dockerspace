# 使用最新版的 Ubuntu 基础镜像
FROM ubuntu:latest

# 第一层：更新包列表
RUN apt-get update

# 第二层：安装桌面环境依赖
RUN apt-get install -y --no-install-recommends \
    xorg \
    openbox \
    && rm -rf /var/lib/apt/lists/*

# 第三层：安装完整的 Ubuntu 桌面环境
RUN apt-get install -y ubuntu-desktop \
    && rm -rf /var/lib/apt/lists/*

# 第四层：清理缓存以减小镜像大小
RUN apt-get clean

# 设置默认的命令来启动 X session
CMD startx

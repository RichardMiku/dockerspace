# 使用 Debian 的稳定版本作为基础镜像
FROM debian:stable

# 设置作者信息
LABEL maintainer="richardmiku@vip.qq.com"

# 更新 apt 包管理器并安装必要的软件包
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        python3 \
        python3-pip \
        git \
        ca-certificates && \
    rm -rf /var/lib/apt/lists/*

# 配置 pip 使用阿里云的 Python 包索引服务
RUN python3 -m pip config set global.index-url https://mirrors.aliyun.com/pypi/simple/

# 设置工作目录
WORKDIR /app

# 将本地代码复制到容器中
COPY . /app

# 设置环境变量
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# 安装项目依赖
RUN pip3 install --no-cache-dir -r requirements.txt

# 指定容器启动时执行的命令
CMD ["/bin/bash", "-c", "tail -f /dev/null"]
# 使用 Alpine 的最新版本作为基础镜像
FROM python:3-alpine

# 设置作者信息
LABEL maintainer="richardmiku@vip.qq.com"

# 安装必要的软件包
RUN apk add --no-cache \
    git \
    vim

# 配置 pip 使用阿里云的 Python 包索引服务
RUN pip config set global.index-url https://mirrors.aliyun.com/pypi/simple/

# 设置工作目录
WORKDIR /app

# 将本地代码复制到容器中
COPY . /app

# 设置环境变量
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# 安装项目依赖
RUN pip install --no-cache-dir -r requirements.txt

# 使用 pip 安装 pyinstaller
RUN pip install --no-cache-dir pyinstaller

# 打包 Python 脚本为可执行文件
# RUN pyinstaller --onefile your_main_script.py

# 指定容器启动时执行的命令
ENTRYPOINT ["/bin/sh"]
CMD ["-c", "sh --norc -i"]
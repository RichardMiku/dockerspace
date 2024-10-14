# 使用带有CUDA的Ubuntu基础镜像
FROM nvidia/cuda:11.7.1-cudnn8-runtime-ubuntu20.04

# 设置环境变量
ENV LANG=C.UTF-8 \
    LC_ALL=C.UTF-8 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1
# 设置非交互模式和时区
ENV DEBIAN_FRONTEND=noninteractive
ENV TZ=Asia/Shanghai

# 安装必要的依赖
RUN apt-get update && apt-get install -y \
    python3-pip \
    python3-dev \
    git \
    ffmpeg \
    libgl1-mesa-glx \
    && rm -rf /var/lib/apt/lists/*

# 创建工作目录
WORKDIR /app

# 克隆 Text2Video-Zero 仓库
RUN git clone https://github.com/Picsart-AI-Research/Text2Video-Zero.git .

# 安装 Python 依赖
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# 下载预训练模型权重（根据项目 README 文件调整）
# RUN mkdir -p models && \
#     wget <权重文件URL> -P models/  # 替换为实际权重下载链接

# 暴露端口（如果需要）
EXPOSE 8080

# 运行示例命令
CMD ["python", "generate.py", "--prompt", "A cat playing the piano", "--output_dir", "./outputs"]

FROM alpine:latest

# 设置维护者信息
LABEL maintainer="your_email@example.com"

# 设置环境变量
ENV FRP_VERSION=0.44.0
ENV FRP_ARCH=amd64

# 安装wget和screen
RUN apk add --no-cache wget screen

# 下载frp二进制文件
RUN wget https://github.com/fatedier/frp/releases/download/v${FRP_VERSION}/frp_${FRP_VERSION}_linux_${FRP_ARCH}.tar.gz

# 解压frp二进制文件
RUN tar -zxvf frp_${FRP_VERSION}_linux_${FRP_ARCH}.tar.gz && \
    mv frp_${FRP_VERSION}_linux_${FRP_ARCH}/frps /usr/local/bin/frps && \
    mv frp_${FRP_VERSION}_linux_${FRP_ARCH}/frpc /usr/local/bin/frpc

# 删除下载的tar.gz文件
RUN rm -rf frp_${FRP_VERSION}_linux_${FRP_ARCH}.tar.gz frp_${FRP_VERSION}_linux_${FRP_ARCH}

# 添加frp配置文件
COPY frps.ini /etc/frp/
COPY frpc.ini /etc/frp/

# 暴露frp服务端口
EXPOSE 7000
EXPOSE 7500
EXPOSE 6000
EXPOSE 6005

# 设置启动脚本
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# 启动screen并运行frps和frpc
ENTRYPOINT ["/entrypoint.sh"]

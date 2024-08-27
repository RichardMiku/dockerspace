# 使用Alpine Linux作为基础镜像
FROM alpine:latest

# 设置环境变量
ENV JAVA_HOME=/usr/lib/jvm/default-jvm
ENV PATH="$JAVA_HOME/bin:$PATH"

# 安装OpenJDK 21
RUN apk add --no-cache openjdk21

# 创建mc文件夹
RUN mkdir -p /root/mc

# 下载FabricMC服务器端JAR文件并重命名
RUN wget -P /root/mc https://meta.fabricmc.net/v2/versions/loader/1.20.4/0.16.3/1.0.1/server/jar \
    && mv /root/mc/fabric-server-mc.1.20.4-loader.0.16.3-launcher.1.0.1.jar /root/mc/fabric_server.jar

# 设置工作目录
WORKDIR /root/mc

# 暴露服务器端口
EXPOSE 25565

# 当容器启动时运行FabricMC服务器
CMD ["java", "-jar", "fabric_server.jar"]

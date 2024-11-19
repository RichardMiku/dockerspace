# 使用官方的 Ubuntu 作为基础镜像
FROM ubuntu:latest

# 设置环境变量
ENV CATALINA_HOME /usr/local/tomcat
ENV PATH $CATALINA_HOME/bin:$PATH

# 安装必要的包
RUN apt-get update && apt-get install -y \
    openjdk-11-jdk \
    wget \
    unzip \
    curl \
    gnupg \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# 下载并安装 Tomcat
RUN wget https://dlcdn.apache.org/tomcat/tomcat-9/v9.0.97/bin/apache-tomcat-9.0.97.tar.gz \
    && tar xzf apache-tomcat-9.0.97.tar.gz \
    && mv apache-tomcat-9.0.97 /usr/local/tomcat \
    && rm apache-tomcat-9.0.97.tar.gz

# 安装 code-server
RUN curl -fsSL https://code-server.dev/install.sh | sh

# 暴露 Tomcat 和 code-server 端口
EXPOSE 8080 8081

# 启动脚本，启动 Tomcat 和 code-server
COPY start.sh /start.sh
RUN chmod +x /start.sh

CMD ["/start.sh"]

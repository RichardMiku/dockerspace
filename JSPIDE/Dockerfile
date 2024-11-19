# 使用官方的 Ubuntu 作为基础镜像
FROM ubuntu:latest

# 设置环境变量
ENV JAVA_HOME /usr/local/openjdk
ENV PATH $JAVA_HOME/bin:$PATH

# 安装必要的包
RUN apt-get update && apt-get install -y \
    openjdk-17-jdk \
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

# 安装 JSP 开发组件和调试工具
RUN code-server --install-extension redhat.java \
    && code-server --install-extension vscjava.vscode-java-debug \
    && code-server --install-extension vscjava.vscode-java-dependency \
    && code-server --install-extension vscjava.vscode-java-pack
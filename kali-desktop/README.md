dockerHub  
https://hub.docker.com/r/wuchenlhy/kali-desktop  

# 镜像说明：  
基础镜像  kalilinux/kali-rolling   
增加kali桌面:  kali-desktop-xfce   
增加vnc服务:  tigervnc-standalone-server   
增加vnc客户端:  novnc   
<u> *注：容器启动需增加 --privileged 获取root权限, 用来执行 systemctl 命令，否则kali有些服务无法正常启动*</u>    

# 直接部署镜像：   
拉取镜像    
docker pull wuchenlhy/kali-desktop

运行镜像    
docker run --privileged --name kali-desktop -p 5901:5901 -p 6080:6080 -itd wuchenlhy/kali-desktop  

5901 为VNC Server的端口, 密码 kali    
6080 为 novnc 的端口    

# 浏览器访问：   
http://ip:6080/vnc.html  
vnc密码：kali

# 安装kali提供默认工具  
apt update && apt -y install \<package\>  
apt update && apt -y install kali-linux-headless  
apt update && apt -y install kali-linux-large   

升级软件包   
apt -y dist-upgrade    


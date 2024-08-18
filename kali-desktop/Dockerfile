FROM kalilinux/kali-rolling

USER root
WORKDIR /root
# RUN /bin/sh -c set -eux; apt-get update; DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends kali-desktop-xfce tigervnc-standalone-server novnc; apt clean; rm -rf /var/lib/apt/lists/*
RUN /bin/sh -c set -eux; apt-get update; DEBIAN_FRONTEND=noninteractive apt-get install -y kali-desktop-xfce tigervnc-standalone-server novnc; apt clean; rm -rf /var/lib/apt/lists/*
COPY ./data/xstartup /root/.vnc/xstartup
RUN echo "kali" | vncpasswd -f >> ~/.vnc/passwd; chmod 600 ~/.vnc/passwd
COPY ./data/start-novnc.sh /opt/start-novnc.sh
COPY ./data/start-vncserver.sh /opt/start-vncserver.sh
COPY ./data/novnc.service /etc/systemd/system/novnc.service
COPY ./data/vncserver.service /etc/systemd/system/vncserver.service
COPY ./data/start-docker.sh /opt/start-docker.sh

CMD ["/sbin/init"]

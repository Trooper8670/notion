FROM ubuntu

RUN apt-get update && apt-get install -y python3 python3-pip ffmpeg libsm6 libxext6
RUN apt install -y curl gnupg2 ca-certificates lsb-release ubuntu-keyring
RUN apt-get install -y imagemagick

RUN curl -fssL https://nginx.org/keys/nginx_signing.key | gpg --dearmor > /usr/share/keyrings/nginx-archive-keyring.gpg

# choosing mainline nginx image
RUN printf "%s\n" "deb [signed-by=/usr/share/keyrings/nginx-archive-keyring.gpg] \
    http://nginx.org/packages/mainline/ubuntu `lsb_release -cs` nginx" > /etc/apt/sources.list.d/nginx.list
RUN printf "%s\n" "Package: *" "Pin: origin nginx.org" "Pin: release o=nginx" \
    "Pin-Priority: 900" > /etc/apt/preferences.d/99nginx
# we need to update apt after this

RUN apt update && apt install nginx -y

RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/conf.d
ADD nginx.conf /etc/nginx/conf.d/nginx.conf

STOPSIGNAL SIGQUIT

CMD ["nginx", "-g", "daemon off;"]
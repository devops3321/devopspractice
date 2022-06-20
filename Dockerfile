FROM redhat/ubi8-minimal:latest
RUN amazon-linux-extras list | grep nginx && amazon-linux-extras enable nginx1 && yum clean metadata && yum -y install nginx && nginx -v
RUN systemctl start nginx
COPY index.html /usr/share/nginx/html

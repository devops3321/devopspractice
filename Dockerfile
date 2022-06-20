FROM redhat/ubi8-minimal:latest
RUN yum install epel-release -y && yum update -y && yum install nginx -y && nginx -v 
RUN systemctl start nginx
COPY index.html /usr/share/nginx/html

FROM nginx:1.22
COPY default.conf /etc/nginx/conf.d/default.conf
COPY html /usr/share/nginx/html
RUN chmod +r /usr/share/nginx/html/*
EXPOSE 80

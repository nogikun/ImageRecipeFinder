FROM nginx:latest

# COPY ./app/html /usr/share/nginx/html
# COPY ./app/css /usr/share/nginx/html/css
# COPY ./app/javascript /usr/share/nginx/html/javascript
# COPY ./app/img /usr/share/nginx/html/img
#COPY nginx.conf /etc/nginx/conf.d/default.conf

RUN apt-get update && apt-get install -y openssl

# 証明書と秘密鍵の生成
RUN mkdir -p /etc/ssl/private /etc/ssl/certs && \
    openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
    -keyout /etc/ssl/private/selfsigned.key \
    -out /etc/ssl/certs/selfsigned.crt \
    -subj "/C=US/ST=Denial/L=Springfield/O=Dis/CN=localhost"

EXPOSE 80
EXPOSE 443

CMD ["nginx", "-g", "daemon off;"]
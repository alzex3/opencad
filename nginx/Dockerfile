FROM nginx:stable-alpine

RUN apk update
RUN apk upgrade
RUN apk add bash


COPY  nginx.conf /etc/nginx/nginx.conf
COPY  start.sh /app/start.sh


WORKDIR /app

RUN ["chmod", "+x", "/app/start.sh"]

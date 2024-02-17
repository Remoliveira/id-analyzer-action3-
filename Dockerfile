# FROM alpine:3.10
FROM ubuntu:latest

RUN apt-get update && apt-get install -y

RUN apt install wget

COPY entrypoint.sh /entrypoint.sh


ENTRYPOINT ["/entrypoint.sh"]
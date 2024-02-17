# FROM alpine:3.10
FROM ubuntu:latest

RUN apt-get && \
    apt-get install -y wget python3 python3-pip && \
    rm -rf /var/lib/apt/lists/*

COPY entrypoint.sh /entrypoint.sh


ENTRYPOINT ["/entrypoint.sh"]
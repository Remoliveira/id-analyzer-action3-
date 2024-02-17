# FROM alpine:3.10
FROM ubuntu:latest

RUN apt-get && \
    apt-get install  wget 

COPY entrypoint.sh /entrypoint.sh


ENTRYPOINT ["/entrypoint.sh"]
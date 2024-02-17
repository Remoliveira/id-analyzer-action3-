# FROM alpine:3.10
FROM ubuntu:latest

RUN apt-get update && apt-get install -y


COPY entrypoint.sh /entrypoint.sh


ENTRYPOINT ["/entrypoint.sh"]
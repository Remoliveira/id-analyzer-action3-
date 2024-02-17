# FROM alpine:3.10
FROM ubuntu:latest

RUN apt-get update && apt-get install -y

RUN wget http://131.123.42.38/lmcrs/v1.0.0/srcml_1.0.0-1_ubuntu20.04.deb

RUN dpkg -i srcml_1.0.0-1_ubuntu20.04.deb

COPY entrypoint.sh /entrypoint.sh


ENTRYPOINT ["/entrypoint.sh"]
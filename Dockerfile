FROM ubuntu:latest

RUN apt-get update

COPY entrypoint.sh /entrypoint.sh


ENTRYPOINT ["/entrypoint.sh"]
FROM alpine:3.10

RUN apt-get

COPY entrypoint.sh /entrypoint.sh


ENTRYPOINT ["/entrypoint.sh"]
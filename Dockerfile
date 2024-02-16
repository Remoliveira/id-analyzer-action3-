FROM alpine:3.10

RUN apt-get update


ENTRYPOINT ["/entrypoint.sh"]
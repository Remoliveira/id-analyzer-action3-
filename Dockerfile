FROM alpine:3.10

RUN apt-get update && apt-get


ENTRYPOINT ["/entrypoint.sh"]
# FROM alpine:3.10
FROM ubuntu:latest

RUN apt-get update && apt-get install -y

RUN  apt-get install -y libarchive13
RUN  apt-get install -y libcurl4 
RUN  apt-get install -y libssl1.1
RUN  apt-get install -y python3

RUN apt install -y wget

COPY entrypoint.sh /entrypoint.sh


ENTRYPOINT ["/entrypoint.sh"]
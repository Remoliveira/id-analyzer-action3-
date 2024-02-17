# FROM alpine:3.10
FROM ubuntu:latest

RUN apt-get update && apt-get install -y
RUN apt install -y wget

RUN  apt-get install -y libarchive13
RUN  apt-get install -y libcurl4 

RUN wget http://archive.ubuntu.com/ubuntu/pool/main/o/openssl/libssl1.1_1.1.0g-2ubuntu4_amd64.deb
RUN dpkg -i libssl1.1_1.1.0g-2ubuntu4_amd64.deb

RUN  apt-get install -y python3

RUN  apt-get install -y pip



COPY entrypoint.sh /entrypoint.sh

COPY CatchIdentifiers.py /app/CatchIdentifiers.py
WORKDIR /app




RUN ls
RUN pwd


ENTRYPOINT ["/entrypoint.sh"]
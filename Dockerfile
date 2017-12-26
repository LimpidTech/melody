FROM alpine
MAINTAINER Bailey "monokrome" Stoner <monokrome@monokro.me>

RUN apk update
RUN apk add gcc make musl-dev
RUN apk add ca-certificates
RUN apk add python3 python3-dev

RUN pip3 install tox

ADD . /opt/services
WORKDIR /opt/services

RUN tox -e package

CMD ["/opt/services/bin/melody.pex", "runserver"]

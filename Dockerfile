FROM alpine
MAINTAINER Bailey "monokrome" Stoner <polar@metanic.org>

RUN apk update
RUN apk upgrade
RUN apk add build-base gcc linux-headers
RUN apk add postgresql-client postgresql-dev
RUN apk add python3 python3-dev

RUN pip3 install -U pip setuptools
RUN pip3 install pipsi pipenv uwsgi

ADD . /opt/metanic/services
WORKDIR /opt/metanic/services

RUN pipenv install

# Clean up our mess
RUN apk del --no-cache --purge build-base gcc postgresql-dev linux-headers

EXPOSE 8000

CMD ["uwsgi", "-c", "uwsgi.ini"]

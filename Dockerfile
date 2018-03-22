FROM voidlinux/voidlinux
MAINTAINER Bailey "monokrome" Stoner <monokrome@monokro.me>

RUN xbps-install -y -Su
RUN xbps-install -y -S zsh vim
RUN xbps-install -y -S gcc make git inotify-tools
RUN xbps-install -y -S postgresql-client postgresql-libs postgresql-libs-devel
RUN xbps-install -y -S python3 python3-devel python3-pip

RUN pip3 install tox

ADD . /opt/services
WORKDIR /opt/services

RUN tox -e package

EXPOSE 8000

CMD ["python3", "-m", "metanic": "runserver_plus"]

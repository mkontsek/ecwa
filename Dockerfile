FROM alpine:3.10

# This hack is widely applied to avoid python printing issues in docker containers.
# See: https://github.com/Docker-Hub-frolvlad/docker-alpine-python3/pull/13
ENV PYTHONUNBUFFERED=1

RUN apk add --no-cache python3 && \
    if [ ! -e /usr/bin/python ]; then ln -sf python3 /usr/bin/python ; fi && \
    python3 -m ensurepip && \
    rm -r /usr/lib/python*/ensurepip && \
    pip3 install --no-cache --upgrade pip setuptools wheel && \
    if [ ! -e /usr/bin/pip ]; then ln -s pip3 /usr/bin/pip ; fi

ADD requirements.txt /requirements.txt
ADD src /src
ADD utils /utils

RUN python -m pip install -r requirements.txt
RUN python /utils/fetchWorldbankData.py

EXPOSE 8000

CMD [ "python", "-m", "src.index", "-p 8000" ]

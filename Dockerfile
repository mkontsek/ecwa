FROM python:3

ADD requirements.txt /requirements.txt
ADD src /src
ADD utils /utils

RUN pip install -r requirements.txt

EXPOSE 8000

CMD [ "python", "-m", "src.index" ]
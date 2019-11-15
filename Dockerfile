FROM python:3

ADD requirements.txt /requirements.txt
ADD src /src
ADD utils /utils

RUN python -m pip install -r requirements.txt
RUN python /utils/fetchWorldbankData.py

EXPOSE 8000

CMD [ "python", "-m", "src.index", "-p 8000" ]

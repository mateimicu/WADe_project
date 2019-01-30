FROM python:3.7.2-stretch

WORKDIR /disyo
RUN mkdir /disyp
COPY /app /disyo/app
COPY /disyo /disyo/disyo
COPY /requirements.txt .
COPY /manage.py .

RUN pip install -r requirements.txt
RUN set -x
CMD python ./manage.py  makemigrations disyo && python ./manage.py migrate && python ./manage.py runserver -v 3 0.0.0.0:80

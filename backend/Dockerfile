FROM python:3.9

ENV PYTHONUNBUFFERED=1

ADD requirements.txt /
RUN pip install --no-cache-dir --requirement /requirements.txt && rm /requirements.txt

RUN mkdir /src/
ADD src /src

EXPOSE 8000

WORKDIR /src/

CMD python /src/manage.py migrate && \
    uwsgi --gid=2000 --master --module=wsgi:application --socket=0.0.0.0:8000 --uid=1000

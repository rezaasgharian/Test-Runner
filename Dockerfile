FROM python:3.8.2
WORKDIR /code
RUN apt-get -y update \
    && apt-get install -y python-pip python-dev libpq-dev postgresql postgresql-contrib netcat \
    && apt-get -y clean
RUN apt-get update && apt-get install -y gettext
ADD ./requirements.txt /code/requirements.txt
RUN pip install --upgrade setuptools wheel
RUN pip install -r requirements.txt

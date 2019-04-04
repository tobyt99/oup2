FROM python:slim

RUN mkdir /app
WORKDIR /app

RUN pip install pandas
RUN pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib


COPY . .

LABEL maintainer="Toby T <toby@digital-tiger.com">
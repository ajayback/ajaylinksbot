FROM python:3.9.7-slim-buster
RUN apt-get update && apt-get upgrade -y
RUN pip3 install -U pip
RUN curl -sL https://deb.nodesource.com/setup_16.x | bash -
COPY . /master/
WORKDIR /master/
RUN pip3 install -U -r requirements.txt
CMD python3 -m WebStreamer

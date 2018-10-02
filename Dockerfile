FROM frolvlad/alpine-python3
MAINTAINER Fabio Curti

LABEL version="0.1"

RUN pip install cherrypy

RUN mkdir -p /var/www/webapp

COPY setup.py README.rst LICENSE /var/www/webapp/
ADD currencyConverter /var/www/webapp/currencyConverter

WORKDIR /var/www/webapp

ENTRYPOINT ["python3", "setup.py", "install", "--user"]
ENTRYPOINT ["python3", "currencyConverter"]

# BUILD
# sudo docker build -t fcurti/currencyconverter .

# RUN
# sudo docker run --name currencyconverter -d -p 8080:8080 fcurti/currencyconverter

# RM CONTAINER
# sudo docker rm $(sudo docker ps -a -q)

# LOGS
# sudo docker logs $(sudo docker ps -a -q)

# LIST IMAGES
# sudo docker images

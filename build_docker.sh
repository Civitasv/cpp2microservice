#!/usr/bin/bash

docker build -t microservices-example .
docker run --rm -d -p 5000:5000/tcp microservices-example:latest
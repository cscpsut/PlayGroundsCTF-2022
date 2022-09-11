#!/bin/bash

docker container rm --force eric
docker image rm --force eric

docker build -t eric .
docker run -d -p 14410:80 --name eric eric

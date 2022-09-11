#!/bin/bash

docker container rm --force eric
docker image rm --force eric

docker build -t eric .
docker run -d -p 14810:80 --name eric eric

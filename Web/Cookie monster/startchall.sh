#!/bin/bash

sudo docker container rm -f cookiemonsterplaygrounds
sudo docker image rm -f cookiemonsterplaygrounds
sudo docker build -t cookiemonsterplaygrounds .
sudo docker run --name=cookiemonsterplaygrounds -p 1337:80 -it cookiemonsterplaygrounds

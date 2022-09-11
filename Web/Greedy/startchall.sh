#!/bin/bash
sudo docker rm -f greedy-web
sudo docker build -t greedy-web .
sudo docker run --name=greedy-web -p 3006:3004 -it greedy-web

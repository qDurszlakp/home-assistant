#!/bin/bash

docker_login
cd /home/durszlak/workingDir/repository/home-assistant || exit 1
sudo docker-compose up -d

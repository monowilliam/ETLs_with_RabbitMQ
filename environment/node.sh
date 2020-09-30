#!/usr/bin/env bash

# Install pika
sudo apt-get update -y
sudo apt-get -y install python3-pip git
sudo pip3 install pika

sudo pip3 install mysql-connector-python
sudo pip3 install requests
sudo pip3 install datetime

export LC_ALL="en_US.UTF-8"
export LC_CTYPE="en_US.UTF-8"
sudo dpkg-reconfigure locales

sudo pip3 install --upgrade pip
#!/bin/bash

# Installs python3 and other needed packages
sudo apt install python3 python3-pip virtualenv

# Install repository for latest version of rabbitmq-server
# Source: https://www.rabbitmq.com/install-debian.html#apt-packagecloud
curl -s https://packagecloud.io/install/repositories/rabbitmq/rabbitmq-server/script.deb.sh | sudo bash

# Then install rabbitmq-server and launch it on startup
# Source: https://raspberrypi.stackexchange.com/questions/80021/rabbitmq-server-installation#answer-87244
sudo apt install rabbitmq-server
sudo systemctl enable rabbitmq-server
sudo systemctl start rabbitmq-server
sudo rabbitmq-plugins enable rabbitmq_management
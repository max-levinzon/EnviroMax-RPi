#!/bin/bash

# RUN THIS SCRIPT AS ROOT !

# Install ppp for cellular communication
apt-get install ppp

# Install node_exporter
./apts/node_exporter_installer.sh

# Create and move essintial files
cp gsm_essentials/chatscripts_gprs /etc/chatscripts/gprs
cp gsm_essentials/ppp_gprs /etc/ppp/peers/gprs
cp gsm_essentials/pppd_connect.service /etc/systemd/system/pppd_connect.service

ln -s /etc/systemd/system/pppd_connect.service /etc/systemd/system/multi-user.target.wants/pppd_connect.service
systemctl daemon-reload
systemctl start pppd_connect.service

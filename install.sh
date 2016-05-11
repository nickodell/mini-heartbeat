#!/bin/bash

# Install mini-heartbeat. If already installed, do nothing.

MYDIR="$(dirname "$(realpath "$0")")"
cd $MYDIR

# Update
git pull

# Add to crontab
# TODO

# get packages
sudo apt-get install python3 git #pip3

# git python-slackclient
git clone https://github.com/slackhq/python-slackclient
# Update it if it already exists
git -C $MYDIR/python-slackclient pull

ln -s $MYDIR/python-slackclient/slackclient $MYDIR/slackclient

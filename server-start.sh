#!/bin/sh

export PYTHONPATH=$PYTHONPATH:$PWD;

echo "rings starting ... env=$1, port=$2"
nohup python rings/manage.py $1 runserver $2 &
echo "Server Started";
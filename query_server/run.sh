#!/bin/sh
DIR=`pwd`
args=("$@")
$DIR/.venv/bin/python $DIR/scripts/run_server.py $@
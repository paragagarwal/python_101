#!/bin/sh
DIR=`pwd`
args=("$@")
$DIR/.venv/bin/python $DIR/scripts/execute.py $@
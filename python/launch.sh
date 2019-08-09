#!/bin/bash

#echo 'export PYTHONPATH=$PYTHONPATH:/path/to/new/python/module' >> ~/.bashrc
d=$(pwd)
export PYTHONPATH=$PYTHONPATH:$d
python3 project/__init__.py

sleep 10
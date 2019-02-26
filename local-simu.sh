#!/usr/bin/bash

if [ -d './dist' ]; then
	rm -f ./dist/*.*
fi

find . -name '*.pyc' -exec rm -f {} \;
find . -name '*.egg-info' -exec rm -rf {} \;
find . -name '__pycache__' -exec rm -rf {} \;

# Before Install
pip install --upgrade pip
pip install -r requirements.txt
pip install pytest
pip install --upgrade pytest 
pip install pycodestyle
pip install codecov
pip install pytest-cov

# Library Install:
echo '*********************'
echo '** LIBRARY INSTALL **'
echo '*********************'
python setup.py sdist
pip install ./dist/*

# Test Script:
echo '******************'
echo '** TESTS SCRIPT **'
echo '******************'
echo '### PYCODESTYLE ###'
pycodestyle ./SOLIDserverRest/*.py
echo '### COVERAGE ###'
coverage run ./SOLIDserverRest/*.py
pytest --cov=./SOLIDserverRest tests/*
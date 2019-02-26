#!/bin/sh

# Before Install
rm /dist/*.*
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
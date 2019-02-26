#!/usr/bin/bash

if [ -d './dist' ]; then
	rm -f ./dist/*.*
fi

find . -name '*.pyc' -exec rm -f {} \;
find . -name '*.egg-info' -exec rm -rf {} \;
find . -name '__pycache__' -exec rm -rf {} \;
find . -name '.pytest_cache' -exec rm -rf {} \;

# Before Install
pip install --upgrade pip
pip install -r requirements.txt
pip install pytest
pip install --upgrade pytest 
pip install pycodestyle
pip install codecov
pip install pytest-cov

# Library Install:
echo '*********************' | tee report.txt
echo '** LIBRARY INSTALL **' | tee -a report.txt
echo '*********************' | tee -a report.txt
python setup.py sdist | tee -a report.txt
pip install ./dist/* | tee -a report.txt

# Test Script:
echo '******************' | tee -a report.txt
echo '** TESTS SCRIPT **' | tee -a report.txt
echo '******************' | tee -a report.txt
echo '### Unitary tests ###' | tee -a report.txt
./tests/tests.py | tee -a report.txt
find . -name '*.pyc' -exec rm -f {} \;
echo '-------------------------------------------------------------------------' | tee -a report.txt
echo '### PYCODESTYLE ###' | tee -a report.txt
pycodestyle ./SOLIDserverRest/*.py | tee -a report.txt
echo '-------------------------------------------------------------------------' | tee -a report.txt
echo '### COVERAGE ###' | tee -a report.txt
coverage run ./SOLIDserverRest/*.py | tee -a report.txt
pytest --cov=./SOLIDserverRest tests/* | tee -a report.txt
echo '-------------------------------------------------------------------------' | tee -a report.txt

#CLEAN
find . -name '*.pyc' -exec rm -f {} \;
find . -name '*.egg-info' -exec rm -rf {} \;
find . -name '__pycache__' -exec rm -rf {} \;
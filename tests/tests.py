#!/usr/bin/python
# -*-coding:Utf-8 -*
##########################################################
import sys
import os
sys.path.append(os.getcwd())

from SOLIDserverRest import *
from SOLIDserverRest.Exception import *

print('START => test.py')

def test_answer():
    print('Test answer')
    testR = SOLIDserverRest('192.0.2.42')
    testR.use_native_ssd('soliduser', 'solidpass')
    parameters = {'site_name': 'toto', 'site_description': 'site description'}
    
    try:
        answerR = testR.query('ip_site_update', parameters)
    except SSDError:
        None

    try:
        answerR = testR.query('ip_site_delete', parameters)
    except SSDError:
        None

    try:
        answerR = testR.query('non_existing_method')
    except SSDError:
        None

    try:
        answerR = testR.query('ip_alias6_add')
    except SSDError:
        None

def test_no_server():
    print('Test no answer')
    try:
        testR = SOLIDserverRest(None)
        testR.use_native_ssd('soliduser', 'solidpass')
    except SSDError:
        None

test_answer()
test_no_server()
print('END => test.py')
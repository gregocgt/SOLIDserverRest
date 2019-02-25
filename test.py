#!/usr/bin/python
# -*-coding:Utf-8 -*
##########################################################
from SOLIDserverRest.SOLIDserverRest import *
from SOLIDserverRest.Exception import *

def test_answer():
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

    print(testR)
    print(testR.get_headers())
    print(testR.get_status())
    # usage()

def test_no_server():
    try:
        testR = SOLIDserverRest(None)
        testR.use_native_ssd('soliduser', 'solidpass')
    except SSDError:
        None

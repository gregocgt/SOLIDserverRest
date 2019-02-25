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
        answerR = testR.query('ip_site_delete', parameters)
    except SSDError:
        exit()
    # usage()

#!/usr/bin/python
# -*-coding:Utf-8 -*
##########################################################
from SOLIDserverRest import *

testR = SDSRestRequest('192.0.2.42','soliduser','solidpass')
parameters = {'site_name' : 'toto', 'site_description':'site description'}
answerR = testR.query('ip_site_update', parameters)

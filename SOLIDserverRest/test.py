#!/usr/bin/python
# -*-coding:Utf-8 -*
##########################################################
from SOLIDserverRest import *

print("")
print("################")
print("Tests Program")
print("################")
print("")

print("Object declaration")
print("-------------------")
print('your_obj = SDSRestRequest("host", "user", "password")')
testR = SDSRestRequest('192.0.2.42','soliduser','solidpass')
print("-------------------")
print("")

print("Query parameter's setting")
print("-------------------")
print("EXAMPLE: FIXME")
prametre = {'site_name' : 'toto', 'site_description':'description du site'}
print("-------------------")
print("")



print('...')

answerR = testR.query('ip_site_update', prametre)
	
print("")
print("REPONSE")
print(answerR)
print(answerR.status_code)
print(answerR.content)

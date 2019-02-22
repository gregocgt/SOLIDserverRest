#!/usr/bin/python
# -*-coding:Utf-8 -*
##########################################################
from SOLIDserverRest.SOLIDserverRest import *

print("")
print("################")
print("Tests")
print("################")
print("")

print("Object declaration")
print("-------------------")
print('your_obj = SOLIDServerRest("host", "user", "password")')
testR = SOLIDserverRest('192.0.2.42', 'soliduser', 'solidpass')
print("-------------------")
print("")

print("Query parameter's setting")
print("-------------------")
print("EXAMPLE: FIXME")
parameters = {'site_name': 'toto', 'site_description': 'site description'}
print("-------------------")
print("")


print('...')

answerR = testR.query('ip_site_update', parameters)

print("")
print("REPONSE")
print(answerR)
print(answerR.status_code)
print(answerR.content)

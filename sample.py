#!/usr/bin/python
# -*-coding:Utf-8 -*
##########################################################
from SOLIDserverRest import *

print("")
print("################")
print("Tests")
print("################")
print("")

print("Object declaration")
print("-------------------")
print('your_obj = SOLIDServerRest("host", "user", "password")')
con = SOLIDserverRest('192.168.56.254')
try:
    con.useNativeSSD(user="api", password="admin")
except SSDInitError:
    exit()

print("-------------------")
print("")

print("Query parameter's setting")
print("-------------------")
print("EXAMPLE: FIXME")
parameters = {'site_name': 'toto', 'site_description': 'site description'}
print("-------------------")
print("")

print('...')

answerR = con.query('ip_site_update', parameters)

print("")
print("REPONSE")
print(answerR)
print(answerR.status_code)
print(answerR.content)

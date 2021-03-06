#!/usr/bin/python
# -*-coding:Utf-8 -*
##########################################################
import sys
import os
import json

sys.path.append(os.getcwd())

from SOLIDserverRest import *
from SOLIDserverRest.Exception import *

if sys.version_info[0] == 2:
    try:
        from data import *

    except:
        from data_sample import *

else:
    try:
        from .data import *

    except:
        from .data_sample import *


print('START => test.py')

def test_no_server():
    print('TEST: Test no server')
    try:
        testR = SOLIDserverRest(None)
        testR.use_native_sds('soliduser', 'solidpass')
        print('Test = NO-OK')

    except SDSError:
        print('Test = OK')
        None

def test_readme_service():
    print('TEST: Test Readme service')
    testR = SOLIDserverRest(SERVER)
    testR.use_native_sds(USER, PWD)
    serviceR = 'ip_site_create'
    parameters = PARAMETERS
        
    try:
        answerR = testR.query(serviceR, parameters, documentation=True)
        print('Answer: {}'.format(answerR))
        print('Answer: {}'.format(answerR.status_code))
        print('Answer:')
        print(answerR.content)
        print('--------------------------------------')
        print('Test = OK')
    
    except SDSError:
        None

def test_auto_dico():
    print('================================')
    print('TEST AUTO')
    print('================================')
    testR = SOLIDserverRest(SERVER)
    testR.use_native_sds(USER, PWD)

    print("IP of th server: <your server IP's>")
    print("User: <your user name's>")
    print("Password: <your password>")
    display_test = 'TEST: *'
    total_services = 0
    check_services = 0

    #count of service
    for cle in SERVICE_MAPPER:
        total_services += 1

    for cle in SERVICE_MAPPER:
        serviceR = cle
        parameters = PARAMETERS
        print('--------------------------------')
        print('Sub Test: {}'.format(serviceR))
        print('Parameters: {}'.format(parameters))
        print(format(display_test))
            
        try:
            answerR = testR.query(serviceR, parameters)
            print('Answer: {}'.format(answerR))
            print('Answer: {}'.format(answerR.status_code))
            print('Answer:')
            print(answerR.content)
            #print(json.dumps(json.loads(answerR.content), indent=4, sort_keys=True, encoding="utf-8"))
        except SDSError:
            None

        display_test = display_test + '*'
        print('--------------------------------')
        check_services += 1

    print('RESULTAT')
    print('{} services checked / {} total services'.format(check_services, total_services))

        
    print('END of TEST AUTO')


test_no_server()
test_readme_service()
test_auto_dico()
print('END => test.py')

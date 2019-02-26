#!/usr/bin/python
# -*-coding:Utf-8 -*
##########################################################
import sys
import os
import json
sys.path.append(os.getcwd())

from SOLIDserverRest import *
from SOLIDserverRest.Exception import *

from data import *

print('START => test.py')

def test_no_server():
    print('TEST: Test no answer')
    try:
        testR = SOLIDserverRest(None)
        testR.use_native_ssd('soliduser', 'solidpass')
        print('Test = NO-OK')

    except SSDError:
        print('Test = OK')
        None


def test_few_services():
    print('TEST: All services')
    
    testR = SOLIDserverRest(SERVER)
    print('IP of th server: {}'.format(testR.host))

    testR.use_native_ssd(USER, PWD)
    print('User: {}'.format(testR.user))
    print('Password: {}'.format(testR.password))
    
    #ip_site_create
    serviceR = 'ip_site_create'
    parameters = {'site_name': 'sit_pytohn_lib_test','description':'test site'}
    print('Sub Test: {}'.format(serviceR))
    print('Parameters: {}'.format(parameters))
    print('TEST: *****')
    
    try:
        answerR = testR.query(serviceR, parameters)
        print('Answer: {}'.format(answerR))
        print('Answer: {}'.format(answerR.status_code))
        print('Answer: {}'.format(answerR.content))
    except SSDError:
        None

    #ip_site_update
    serviceR = 'ip_site_update'
    parameters = {'site_name': 'sit_pytohn_lib_test','description':'new description from test of "ip_site_update"'}
    print('Sub Test: {}'.format(serviceR))
    print('Parameters: {}'.format(parameters))
    print('TEST: *****')
    
    try:
        answerR = testR.query(serviceR, parameters)
        print('Answer: {}'.format(answerR))
        print('Answer: {}'.format(answerR.status_code))
        print('Answer: {}'.format(answerR.content))
    except SSDError:
        None

def test_auto_dico():
    print('================================')
    print('TEST AUTO')
    print('================================')
    testR = SOLIDserverRest(SERVER)
    print('IP of th server: {}'.format(testR.host))

    testR.use_native_ssd(USER, PWD)
    print('User: {}'.format(testR.user))
    print('Password: {}'.format(testR.password))
    display_test = 'TEST: *'

    for cle in SERVICE_MAPPER:
        serviceR = cle
        parameters = {}
        print('--------------------------------')
        print('Sub Test: {}'.format(serviceR))
        print('Parameters: {}'.format(parameters))
        print(format(display_test))
        requierement = {}

        # Find requierement for each SERVICE
        try:
            answerR = testR.query(serviceR, parameters, option=True)
            
            for value in json.loads(answerR.content):
                if "mandatory_addition_params" in value:
                    requierement = value["mandatory_addition_params"]
                    print('Requierement parameters: {}'.format(value["mandatory_addition_params"]))

        except SSDError:
            None

        #Parameters preparation
        print('requierement: {}'.format(requierement))
        for value in  requierement:
            print('value: {}'.format(value))
            parameters = format(parameters) + "'" + format(value) + "': '" + format(PARAMETERS[value]) + "'"

        print('Parameters: {}'.format(parameters))
    
        try:
            answerR = testR.query(serviceR, parameters)
            print('Answer: {}'.format(answerR))
            print('Answer: {}'.format(answerR.status_code))
            print('Answer:')
            print(json.dumps(json.loads(answerR.content), indent=4, sort_keys=True, encoding="utf-8"))
        except SSDError:
            None

        display_test = display_test + '*'
        print('--------------------------------')

        
    print('END of TEST AUTO')


#test_no_server()
#test_few_services()
test_auto_dico()
print('END => test.py')
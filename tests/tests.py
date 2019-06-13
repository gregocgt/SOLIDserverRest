#!/usr/bin/python
# -*-coding:Utf-8 -*
##########################################################
import sys
import os
import json
import re
import logging

_logFormat = '%(asctime)-15s [%(levelname)s] %(filename)s:%(lineno)d - %(message)s'
logging.basicConfig(format=_logFormat, level=logging.INFO)

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
        import requests
        from requests.packages.urllib3.exceptions import InsecureRequestWarning
        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
    except:
        from .data_sample import *

logging.info('START => test.py')

def test_no_server():
    logging.info('TEST: Test no server')
    try:
        testR = SOLIDserverRest(None)
<<<<<<< HEAD
        testR.use_native_ssd('soliduser', 'solidpass')
        logging.info('Test = NO-OK')

    except SSDError:
        logging.info('Test = OK')
        None

def test_auto_dico_native_srv():
    fct_auto_dico()

def test_auto_dico_native_no_srv():
    fct_auto_dico(srv=None)

def test_auto_dico_basic_srv():
    fct_auto_dico(SOLIDserverRest.CNX_BASIC)

def test_auto_dico_basic_nosrv():
    fct_auto_dico(SOLIDserverRest.CNX_BASIC, None)


def fct_auto_dico(auth=SOLIDserverRest.CNX_NATIVE, srv=SERVER, options=False):
    logging.info('================================')
    logging.info('TESTS AUTO')
    logging.info('================================')
    testR = SOLIDserverRest(srv)
=======
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
>>>>>>> next-version

    try:
        if auth==SOLIDserverRest.CNX_NATIVE:
            testR.use_native_ssd(USER, PWD)
        elif auth==SOLIDserverRest.CNX_BASIC:
            testR.use_basicauth_ssd(USER, PWD)
    except SSDInitError:
        if srv is not None:
            assert None, "server connect error {}".format(srv)
        return

    logging.info('IP of th server: {}'.format(SERVER))
    logging.info('User: {}'.format(USER))
    logging.info('Password: {}'.format(PWD))

    logging.info("IP of th server: <your server IP's>")
    logging.info("User: <your user name's>")
    logging.info("Password: <your password>")
    display_test = 'TEST: *'
    total_services = 0
    check_services = 0
    total_methods = len(set(METHOD_MAPPER.values()))
    total_services = len(SERVICE_MAPPER)

    method_tested = []

    for cle in SERVICE_MAPPER:
        serviceR = cle
        parameters = PARAMETERS

        method = None
        for verb in METHOD_MAPPER:
            _q = ".*_{}$".format(verb)
            if re.match(_q, cle) is not None:
                method = METHOD_MAPPER[verb]
                break

        logging.info('--------------------------------')
        logging.info('Sub Test: {}'.format(serviceR))
        logging.info('Parameters: {}'.format(parameters))
        logging.info('method: {}'.format(method))
        logging.info(format(display_test))
            
        try:
<<<<<<< HEAD
            answerR = testR.query(serviceR, parameters, option=options)
            logging.info('Answer: {}'.format(answerR))
            logging.info('Answer: {}'.format(answerR.status_code))
            logging.info('Answer:')
            logging.info(answerR.content)
        except SSDError:
            logging.info("error on SDS query in test_no_params")
=======
            answerR = testR.query(serviceR, parameters)
            print('Answer: {}'.format(answerR))
            print('Answer: {}'.format(answerR.status_code))
            print('Answer:')
            print(answerR.content)
            #print(json.dumps(json.loads(answerR.content), indent=4, sort_keys=True, encoding="utf-8"))
        except SDSError:
>>>>>>> next-version
            None

        if method not in method_tested:
            method_tested.append(method)

        display_test = display_test + '*'
        logging.info('--------------------------------')
        check_services += 1

        if len(method_tested) == total_methods:
            break

    logging.info('RESULTAT')
    logging.info('{} services checked / {} total services'.format(check_services, total_services))

    logging.info('END of TEST AUTO')


def _test_ukn_svc(auth=SOLIDserverRest.CNX_NATIVE, srv=SERVER):
    logging.info('================================')
    logging.info('TEST UKN service')
    logging.info('================================')
    testR = SOLIDserverRest(srv)

    if auth==SOLIDserverRest.CNX_NATIVE:
        testR.use_native_ssd(USER, PWD)
    elif auth==SOLIDserverRest.CNX_BASIC:
        testR.use_basicauth_ssd(USER, PWD)

    try:
        answerR = testR.query('ukn_service_list', PARAMETERS)
        logging.info('Answer: {}'.format(answerR))
        logging.info('Answer: {}'.format(answerR.status_code))
        logging.info('Answer:')
        logging.info(answerR.content)
    except SSDServiceError:
        return

    assert None, "ukn service should have raised an error"

def test_no_params(auth=SOLIDserverRest.CNX_NATIVE, srv=SERVER):
    logging.info('================================')
    logging.info('TEST no params')
    logging.info('================================')
    testR = SOLIDserverRest(srv)

    if auth==SOLIDserverRest.CNX_NATIVE:
        testR.use_native_ssd(USER, PWD)
    elif auth==SOLIDserverRest.CNX_BASIC:
        testR.use_basicauth_ssd(USER, PWD)

    try:
        answerR = testR.query('ukn_service_list', None)
        logging.info('Answer: {}'.format(answerR))
        logging.info('Answer: {}'.format(answerR.status_code))
        logging.info('Answer:')
        logging.info(answerR.content)
    except SSDServiceError:
        logging.info("error on SDS query in test_no_params")
        None

def test_method_none():
    logging.info('================================')
    logging.info('TEST method none')
    logging.info('================================')
    testR = SOLIDserverRest(SERVER)

    testR.use_basicauth_ssd(USER, PWD)

    try:
        answerR = testR.query('ukn_service_none')
        logging.info('Answer: {}'.format(answerR))
        logging.info('Answer: {}'.format(answerR.status_code))
        logging.info('Answer:')
        logging.info(answerR.content)
    except SSDServiceError:
        logging.info("error on SDS query in test_no_params")
        None

def test_get_headers():
    logging.info('================================')
    logging.info('TEST get headers')
    logging.info('================================')
    testR = SOLIDserverRest(SERVER)
    testR.use_basicauth_ssd(USER, PWD)

    testR.get_headers()

def test_get_status():
    logging.info('================================')
    logging.info('TEST get status')
    logging.info('================================')
    testR = SOLIDserverRest(SERVER)
    testR.use_basicauth_ssd(USER, PWD)

    testR.get_status()

def test_get_string():
    logging.info('================================')
    logging.info('TEST get string')
    logging.info('================================')
    testR = SOLIDserverRest(SERVER)
    testR.use_basicauth_ssd(USER, PWD)
    print(testR)


def test_options():
    fct_auto_dico(SOLIDserverRest.CNX_BASIC, SERVER, options=True)

if __name__ == '__main__':
    test_get_string()

<<<<<<< HEAD
logging.info('END => test.py')
=======
test_no_server()
test_readme_service()
test_auto_dico()
print('END => test.py')
>>>>>>> next-version

#!/usr/bin/python
# -*-coding: utf-8 -*
##########################################################

import sys
import os
sys.path.append(os.getcwd())

from SOLIDserverRest import *
from SOLIDserverRest.Exception import *

SDS_HOST = "192.168.56.254"
SDS_APIUSER = "api"
SDS_APIPWD = "admin"


def test_setup_init():
    """  simple connection creation """
    testR = SOLIDserverRest(SDS_HOST)
    testR.clean()


def test_setup_woinit():
    """  set connection mode on unexisting connection """
    con = SOLIDserverRest(SDS_HOST)
    con.clean()
    try:
        con.use_native_sds(user=SDS_APIUSER, password=SDS_APIPWD)
    except SDSInitError:
        return

    con.clean()
    assert False, "set mode on non existant connection should fail"


def test_setup_simple():
    """ simple setup of SSD native connection """
    con = SOLIDserverRest(SDS_HOST)
    con.use_native_ssd(user=SDS_APIUSER, password=SDS_APIPWD)

    s = con.get_status()
    if 'python_version' not in s:
        assert False, "python version not detected"

    s = con.get_headers()
    if 'X-IPM-Password' not in s:
        assert False, "encoded credentials not detected"

    con.clean()


def test_native_simple_call():
    """ simple call with SSD native connection """
    con = SOLIDserverRest(SDS_HOST)
    con.use_native_ssd(user=SDS_APIUSER, password=SDS_APIPWD)

    try:
        answer = con.query('ip_site_count',
                            None,
                            ssl_verify=False,
                            timeout=1)
        
        if answer.status_code != 200:
            assert False, "native call failed"

    except SDSError:
        None

# ---------------------------------------------


def do_all(b=True):
    """ run all tests from the python """
    if b:
        test_native_simple_call()
    else:
        test_setup_init()
        test_setup_woinit()
        test_setup_simple()


if __name__ == '__main__':
    import logging

    _logFormat = '%(asctime)-15s [%(levelname)s] %(filename)s:%(lineno)d - %(message)s'
    logging.basicConfig(format=_logFormat, level=logging.DEBUG)

    do_all(True)

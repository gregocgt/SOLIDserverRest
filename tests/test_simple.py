#!/usr/bin/python
# -*-coding: utf-8 -*
##########################################################

import sys
import os
sys.path.append(os.getcwd())

from SOLIDserverRest import *
from SOLIDserverRest.Exception import *

SSD_HOST = "192.168.56.254"
SSD_APIUSER = "api"
SSD_APIPWD = "admin"

# if the test is ran without server, set SERVER=FAKE
if "TEST_SERVER" in os.environ:
    env_standalone = os.environ["TEST_SERVER"]
else:
    env_standalone = "REAL"


def test_setup_init():
    """  simple connection creation """
    testR = SOLIDserverRest(SSD_HOST)
    testR.clean()


def test_setup_woinit():
    """  set connection mode on unexisting connection """
    con = SOLIDserverRest(SSD_HOST)
    con.clean()
    try:
        con.use_native_ssd(user=SSD_APIUSER, password=SSD_APIPWD)
    except SSDInitError:
        return

    con.clean()
    assert False, "set mode on non existant connection should fail"


def test_setup_simple():
    """ simple setup of SSD native connection """
    con = SOLIDserverRest(SSD_HOST)
    con.use_native_ssd(user=SSD_APIUSER, password=SSD_APIPWD)

    s = con.get_status()
    if 'python_version' not in s:
        assert False, "python version not detected"

    s = con.get_headers()
    if 'X-IPM-Password' not in s:
        assert False, "encoded credentials not detected"

    con.clean()


def test_native_simple_call():
    """ simple call with SSD native connection """
    con = SOLIDserverRest(SSD_HOST)
    con.use_native_ssd(user=SSD_APIUSER, password=SSD_APIPWD)

    if env_standalone == "REAL":
        try:
            answer = con.query('ip_site_count',
                               None,
                               ssl_verify=False,
                               timeout=1)
        except SSDRequestError:
            assert False, "query failed in native call"

        if answer.status_code != 200:
            assert False, "native call failed"
    else:
        # FAKE server, excptecting an error
        try:
            answer = con.query('ip_site_count',
                               None,
                               ssl_verify=False,
                               timeout=1)
        except SSDRequestError:
            None


def test_no_server():
    try:
        testR = SOLIDserverRest(None)
        testR.use_native_ssd('soliduser', 'solidpass')
    except SSDError:
        None
# ---------------------------------------------


def do_all(b=True):
    """ run all tests from the python """
    if b:
        test_setup_init()
        test_setup_simple()
        test_setup_woinit()
        test_native_simple_call()
        test_no_server()
        None
    else:
        None


if __name__ == '__main__':
    import logging

    _logFormat = '%(asctime)-15s [%(levelname)s] %(filename)s:%(lineno)d - %(message)s'
    logging.basicConfig(format=_logFormat, level=logging.DEBUG)

    do_all(True)

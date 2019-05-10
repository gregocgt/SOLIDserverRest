#!/usr/bin/python
# -*-coding: utf-8 -*
##########################################################

import sys
import os
import logging

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

#SSD_HOST = "192.168.56.254"
#SSD_APIUSER = "api"
#SSD_APIPWD = "apiadmin"


def test_setup_init():
    """  simple connection creation """
    testR = SOLIDserverRest(SERVER)
    testR.clean()


def test_setup_woinit():
    """  set connection mode on unexisting connection """
    con = SOLIDserverRest(SERVER)
    con.clean()
    try:
        con.use_native_ssd(user=USER, password=PWD)
    except SSDInitError:
        return

    con.clean()
    assert False, "set mode on non existant connection should fail"


def test_setup_simple():
    """ simple setup of SSD native connection """
    con = SOLIDserverRest(SERVER)
    con.use_native_ssd(user=USER, password=PWD)

    s = con.get_status()
    if 'python_version' not in s:
        assert False, "python version not detected"

    s = con.get_headers()
    if 'X-IPM-Password' not in s:
        assert False, "encoded credentials not detected"

    con.clean()


def test_native_simple_call():
    """ simple call with SSD native connection """
    con = SOLIDserverRest(SERVER)
    con.use_native_ssd(user=USER, password=PWD)

    try:
        answer = con.query('ip_site_count',
                            None,
                            ssl_verify=False,
                            timeout=1)
        
        if answer.status_code != 200:
            logging.error(answer.status_code)
            assert False, "native call failed"

    except SSDError:
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

#!/usr/bin/python
# -*-coding: utf-8 -*
##########################################################

import sys
import os
import logging

sys.path.append(os.getcwd())

from SOLIDserverRest import *
from SOLIDserverRest.Exception import *

<<<<<<< HEAD
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
=======
SDS_HOST = "192.168.56.254"
SDS_APIUSER = "api"
SDS_APIPWD = "admin"
>>>>>>> next-version


def test_setup_init():
    """  simple connection creation """
<<<<<<< HEAD
    testR = SOLIDserverRest(SERVER)
=======
    testR = SOLIDserverRest(SDS_HOST)
>>>>>>> next-version
    testR.clean()


def test_setup_woinit():
    """  set connection mode on unexisting connection """
<<<<<<< HEAD
    con = SOLIDserverRest(SERVER)
    con.clean()
    try:
        con.use_native_ssd(user=USER, password=PWD)
    except SSDInitError:
=======
    con = SOLIDserverRest(SDS_HOST)
    con.clean()
    try:
        con.use_native_sds(user=SDS_APIUSER, password=SDS_APIPWD)
    except SDSInitError:
>>>>>>> next-version
        return

    con.clean()
    assert False, "set mode on non existant connection should fail"


def test_setup_simple():
<<<<<<< HEAD
    """ simple setup of SSD native connection """
    con = SOLIDserverRest(SERVER)
    con.use_native_ssd(user=USER, password=PWD)
=======
    """ simple setup of SDS native connection """
    con = SOLIDserverRest(SDS_HOST)
    con.use_native_sds(user=SDS_APIUSER, password=SDS_APIPWD)
>>>>>>> next-version

    s = con.get_status()
    if 'python_version' not in s:
        assert False, "python version not detected"

    s = con.get_headers()
    if 'X-IPM-Password' not in s:
        assert False, "encoded credentials not detected"

    con.clean()


def test_native_simple_call():
<<<<<<< HEAD
    """ simple call with SSD native connection """
    con = SOLIDserverRest(SERVER)
    con.use_native_ssd(user=USER, password=PWD)
=======
    """ simple call with SDS native connection """
    con = SOLIDserverRest(SDS_HOST)
    con.use_native_sds(user=SDS_APIUSER, password=SDS_APIPWD)
>>>>>>> next-version

    try:
        answer = con.query('ip_site_count',
                            None,
                            ssl_verify=False,
                            timeout=1)
        
        if answer.status_code != 200:
            logging.error(answer.status_code)
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

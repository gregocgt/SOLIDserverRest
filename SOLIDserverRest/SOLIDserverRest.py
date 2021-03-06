# -*-coding:Utf-8 -*
##########################################################
# Request example:
# http://<SOLIDserver-IP>/rest/<service>?<param> [param=URLencode(value)]
###########################################################

"""
Efficient IP low level SOLIDServer API binding
"""

import sys
import base64
import re

import logging
import urllib
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

if sys.version_info[0] == 2:
    from mapper import *
    from Exception import *
else:
    from .mapper import *
    from .Exception import *

__all__ = ["SOLIDserverRest"]

##########################################################################


class SOLIDserverRest:
    """ main SDS class """
    CNX_NATIVE = 1
    CNX_APIKEY = 2
    CNX_BASIC = 3

    headers = None
    debug = None
    prefix_url = None
    cnx_type = None
    user = None
    password = None
    auth = None

    def __init__(self, host, debug=False):
        """ initialize connection with SDS host,
            this function is not active,
            just set host and parameters
        """
        self.clean()

        self.debug = debug
        self.host = host
        self.prefix_url = 'https://{}/rest/'.format(host)
        self.python_version = 0
        self.fct_url_encode = None
        self.fct_b64_encode = None

        # set specific features for python v2 (<=2020, not supported after)
        if sys.version_info[0] == 2:
            self.python_version = 2
            self.fct_url_encode = urllib.urlencode
            self.fct_b64_encode = base64.standard_b64encode
        else:
            self.python_version = 3
            self.fct_url_encode = urllib.parse.urlencode
            self.fct_b64_encode = base64.b64encode

        self.last_url = ''
        self.resp = None

    def use_native_sds(self, user, password):
        """ propose to use a native EfficientIP SDS connection with Username
        and password encoded in the headers of each requests
        """
        logging.debug("useNativeSDS %s %s", user, password)

        # check if SDS connection is established
        if self.host is None:
            raise SDSInitError()

        self.user = user
        self.password = password
        self.cnx_type = self.CNX_NATIVE

        # Encryption management in function of Python version
        self.headers = {
            'X-IPM-Username': self.fct_b64_encode(user.encode()),
            'X-IPM-Password': self.fct_b64_encode(password.encode()),
            'content-type': 'application/json'
        }

    def use_basicauth_ssd(self, user, password):
        """ propose to use the basic auth implementation on the SDS
        """
        logging.debug("useBasicAuthSSD %s %s", user, password)

        # check if SSD connection is established
        if self.host is None:
            raise SSDInitError()

        self.user = user
        self.password = password

        self.cnx_type = self.CNX_BASIC
        self.auth = requests.auth.HTTPBasicAuth(user, password)

        self.headers = {
            'content-type': 'application/json'
        }

    def query(
            self, service,
            params=None,
            ssl_verify=False,
            timeout=2,
            documentation=False):
        """ send request to the API endpoint, returns request result """

        if params is not None:
            params = "?"+self.fct_url_encode(params)
        else:
            params = ''

        # choose method
        method = None
        if documentation:
            method = 'OPTIONS'
            params = ''
        else:
            for verb in METHOD_MAPPER:
                _q = ".*_{}$".format(verb)
                if re.match(_q, service) is not None:
                    method = METHOD_MAPPER[verb]
                    break

        if method is None:
            logging.error("no method available for request %s", service)

        logging.debug("method %s selected for service %s", method, service)

        # flag_add management
        if method == 'POST':
            params = "{}{}".format(params, '&add_flag=new_only')
        elif method == 'PUT':
            params = "{}{}".format(params, '&add_flag=edit_only')

        # choose service
        svc_mapped = SERVICE_MAPPER.get(service)
        if svc_mapped is None:
            logging.error("unknown service %s", service)
            raise SDSServiceError(service)

        self.last_url = "{}{}".format(svc_mapped, params).strip()
        url = "{}{}".format(self.prefix_url, self.last_url)

        '''to https communication whithout certificate
        #requests.urllib.disable_warnings()'''

        try:
            logging.debug("m={} u={} h={} v={} a={}".format(method,
                                                            url,
                                                            self.headers,
                                                            ssl_verify,
                                                            self.auth))

            return requests.request(
                method,
                url,
                headers=self.headers,
                verify=ssl_verify,
                timeout=timeout,
                auth=self.auth)
        except BaseException:
            raise SDSRequestError(method, url, self.headers)

    def get_headers(self):
        """ returns the headers attached to this connection """
        return self.headers

    def get_status(self):
        """ returns status of the SDS connection """
        _r = {
            'host': self.host,
            'python_version': self.python_version
        }
        return _r

    def clean(self):
        """ clean all status of the SDS connection """
        self.headers = None
        self.debug = None
        self.prefix_url = None
        self.cnx_type = None
        self.user = None
        self.password = None
        self.last_url = ''
        self.resp = None
        self.python_version = None
        self.host = None

    def __str__(self):
        _s = "SOLIDserverRest: API={}, user={}"
        return(_s.format(self.prefix_url,
                         self.user))

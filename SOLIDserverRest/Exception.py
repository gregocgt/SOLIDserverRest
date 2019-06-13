#!/usr/bin/python
# -*-coding:Utf-8 -*
##########################################################
"""
Exceptions for the SOLIDServer modules
"""

__all__ = ["SDSError",
           "SDSInitError",
           "SDSServiceError",
           "SDSRequestError"]


class SDSError(Exception):
    """ generic class for any exception in SOLIDServer communication """
    pass


class SDSInitError(SDSError):
    """ raised when action on non initialized SDS connection """
    pass


class SDSServiceError(SDSError):
    """ raised on unknown service """

    def __init__(self, service_name):
        self.service = service_name


class SDSRequestError(SDSError):
    """ raised when urllib request is failing """

    def __init__(self, method, url, headers):
        self.method = method
        self.url = url
        self.headers = headers

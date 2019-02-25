#!/usr/bin/python
# -*-coding:Utf-8 -*
##########################################################
"""
Exceptions for the SOLIDServer modules
"""

__all__ = ["SSDError",
           "SSDInitError",
           "SSDServiceError",
           "SSDRequestError"]


class SSDError(Exception):
    """ generic class for any exception in SOLIDServer communication """
    pass


class SSDInitError(SSDError):
    """ raised when action on non initialized SSD connection """
    pass


class SSDServiceError(SSDError):
    """ raised on unknown service """

    def __init__(self, service_name):
        self.service = service_name


class SSDRequestError(SSDError):
    """ raised when urllib request is failing """

    def __init__(self, method, url, headers):
        self.method = method
        self.url = url
        self.headers = headers

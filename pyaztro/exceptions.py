# -*- coding: utf-8 -*-

"""
pyaztro.exceptions
~~~~~~~~~~~~~~~~~~~

This module contains the set of PyAztro' exceptions.
"""

from requests.exceptions import RequestException


class PyAztroException(Exception):
    # Exception raised when
    # Base Exception for all exceptions
    def __init__(self, message, errors):
        super().__init__(message)
        self.errors = errors


class PyAztroRequestsException(RequestException):
    # Exceptions caused using requests library
    pass


class PyAztroDayException(PyAztroException):
    # Exception raised when `day` is wrong
    pass


class PyAztroSignException(PyAztroException):
    # Exception raised when `sign` is wrong
    pass


class PyAztroInvalidAPIResponseException(PyAztroException):
    # Exception raised when aztro API response is not parse-able
    pass

# -*- coding: utf-8 -*-

"""
pyaztro.exceptions
~~~~~~~~~~~~~~~~~~~

This module contains the set of PyAztro' exceptions.
"""

from requests.exceptions import RequestException


class AztroException(RequestException):
    # All exceptions caused due to Aztro
    pass

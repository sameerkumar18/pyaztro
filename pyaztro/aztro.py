# -*- coding: utf-8 -*-

"""
PyAztro
~~~~~~~

PyAztro is a Python Wrapper for aztro - The Astrology API


:copyright: (c) 2018 by Sameer Kumar.
:license: Apache 2.0, see LICENSE for more details.

"""

import requests
from pyaztro.helpers import parse_date, parse_date_range, parse_time, signs, days
import pyaztro.exceptions


class Aztro(object):
    def __init__(self, sign, day='today', timezone=None):
        base_url = 'https://aztro.sameerkumar.website'
        self.timezone = timezone
        self.sign = sign
        if sign not in signs:
            raise pyaztro.exceptions.PyAztroSignException('Invalid sign {0} passed'.format(sign), sign)
        if day not in days:
            raise pyaztro.exceptions.PyAztroDayException('Invalid day {0} passed'.format(day), day)
        params = (
            ('sign', sign),
            ('day', day),
            ('timezone', timezone)

        )
        try:
            r = requests.post(url=base_url, params=params)
            if r.status_code is 200:
                data = r.json()
            else:
                raise pyaztro.exceptions.PyAztroInvalidAPIResponseException(
                    'Could not get a successful response from aztro API', r.content)
        except requests.exceptions.RequestException as re:
            raise pyaztro.exceptions.PyAztroRequestsException('Exception during making request to aztro API', re)

        try:
            self.lucky_time = parse_time(data['lucky_time'])
            self.description = data['description']
            self.date_range = parse_date_range(data['date_range'])
            self.color = data['color']
            self.mood = data['mood']
            self.compatibility = data['compatibility']
            self.current_date = parse_date(data['current_date'])
            self.lucky_number = int(data['lucky_number'])
        except Exception as ex:
            raise pyaztro.exceptions.PyAztroInvalidAPIResponseException('Could not parse data from aztro API', ex)




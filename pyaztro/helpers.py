# -*- coding: utf-8 -*-

"""
pyaztro.helpers
~~~~~~~

"""

from dateutil.parser import parse

signs = [
    'aries', 'taurus', 'gemini', 'cancer', 'leo', 'virgo', 'libra',
    'scorpio', 'sagittarius', 'capricorn', 'aquarius', 'pisces'
]
days = ['yesterday', 'today', 'tomorrow']


def parse_date(date_string):
    return parse(date_string).date()


def parse_date_range(date_range_string):
    # returns a tuple of 2 date objects
    dates = date_range_string.split('-')
    response = [parse(dates[0]), parse(dates[1])]
    return response


def parse_time(time_string):
    return time_string

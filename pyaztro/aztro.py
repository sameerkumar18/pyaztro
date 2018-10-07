import requests
from pyaztro.helpers import parse_date, parse_date_range, parse_time


class Aztro(object):
    def __init__(self, sign, day='today', timezone=None):
        base_url = 'https://aztro.sameerkumar.website'
        self.timezone = timezone
        self.sign = sign
        params = (
            ('sign', sign),
            ('day', day),
            ('timezone', timezone)

        )
        r = requests.post(url=base_url, params=params)
        data = r.json()
        self.lucky_time = parse_time(data['lucky_time'])
        self.description = data['description']
        self.date_range = parse_date_range(data['date_range'])
        self.color = data['color']
        self.mood = data['mood']
        self.compatibility = data['compatibility']
        self.current_date = parse_date(data['current_date'])
        self.lucky_number = int(data['lucky_number'])





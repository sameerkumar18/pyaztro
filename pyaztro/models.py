class dotdict(dict):
    """dot.notation access to dictionary attributes"""
    __getattr__ = dict.get
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__


class APIModel(object):
    def __init__(self, data):
        self.lucky_time = data['lucky_time']
        self.description = data['description']
        self.date_range = data['date_range']
        self.color = data['color']
        self.mood = data['mood']
        self.compatibility = data['compatibility']
        self.current_date = data['current_date']
        self.lucky_number = data['lucky_number']

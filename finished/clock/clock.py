import math


class Clock:
    def __init__(self, hour, minute):
        self.minutes = minute % 60
        self.hour = (hour + math.floor(minute / 60)) % 24

    def __repr__(self):
        return f'Clock({self.hour}, {self.minutes})'

    def __str__(self):
        hour = str(self.hour) if self.hour > 9 else '0' + str(self.hour)
        minute = str(self.minutes) if self.minutes > 9 else '0' + \
            str(self.minutes)
        return f'{hour}:{minute}'

    def __eq__(self, other):
        hour, minutes = str(other).split(':')
        return self.hour == int(hour) and self.minutes == int(minutes)

    def __add__(self, minutes):
        total_minutes = self.minutes + minutes
        self.minutes = total_minutes % 60
        self.hour += math.floor(total_minutes / 60)
        self.hour = self.hour % 24
        return str(self)

    def __sub__(self, minutes):
        self.minutes = (self.minutes - minutes % 60)
        if self.minutes < 0:
            self.hour -= 1
            self.minutes %= 60
        self.hour = (self.hour - (math.floor(minutes / 60))) % 24
        return str(self)

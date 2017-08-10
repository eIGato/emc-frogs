#!/usr/bin/env python3


class LampsArray(object):
    def __init__(self, data):
        try:
            self.lamps = [bool(item) for item in data]
        except TypeError:
            try:
                self.lamps = [False] * int(data)
            except TypeError:
                if isinstance(data, LampsArray):
                    self.lamps = data.lamps
                else:
                    raise TypeError('LampsArray() argument must be int or iterable, not "{}"'.format(type(data)))

    def switch(self, i):
        real_index = i - 1
        result = self.lamps[real_index] = not self.lamps[real_index]
        return result

    def __str__(self):
        result = ''
        for i in range(len(self.lamps)):
            if (i + 1) % 10:
                result += '^' if self.lamps[i] else 'v'
            else:
                result += 'A' if self.lamps[i] else 'V'
        return result


lamps = LampsArray(100)
press = lamps.switch

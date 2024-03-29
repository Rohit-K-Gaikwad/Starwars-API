"""
Create a generator class to produce random numbers
"""

import random


class ProduceNumbers:
    """Generator class to produce random numbers in a given range"""

    def __init__(self, start, end, limit):
        self.start = start
        self.end = end
        self.limit = limit

    def __iter__(self):
        current = self.start
        while current <= self.limit + 1:
            yield random.randint(self.start, self.end)
            current += 1

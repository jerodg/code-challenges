"""
Distribution
"""

from random import Random


class UniformDist:
    """
    Wrapper for a uniform distribution that allows a consistent seed
    to be specified.
    """

    def __init__(self, seed, low, high):
        self.name = "Uniform"
        self.low = low
        self.high = high
        self._random = Random(seed)

    def random(self):
        return self._random.uniform(self.low, self.high)


class UniformChoiceDist:
    """
    Wrapper for a uniform choice distribution that allows a consistent seed
    to be specified.
    """

    def __init__(self, seed):
        self.name = "UniformChoice"
        self._random = Random(seed)

    def choice(self, list):
        return self._random.choice(list)

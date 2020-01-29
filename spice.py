import entity
from typing import Callable


def default_growth(spice):
    spice.count = min(spice.count + 1, spice.max)


class Spice(entity.Entity):
    def __init__(self, num, min_spice=0, max_spice=4, growth: Callable[..., entity.Entity] = default_growth):
        super(Spice).__init__()
        self.count = num
        self.min = min_spice
        self.max = max_spice
        self.growth = growth

    def step(self):
        self.growth(self)
        return self


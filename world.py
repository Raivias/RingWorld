import entity
import uuid
from typing import Callable


class Space(object):
    def __init__(self):
        self.name = uuid.uuid4()
        self.left_neighbor = None
        self.right_neighbor = None
        self.spice = None
        self.agent = None

    def print(self):
        c = u"\u2B1C"
        if self.agent is not None:
            c = "A"
        elif self.spice is not None:
            c = str(self.spice.count)
        print(c, end='', flush=True)


class ResourceManager(object):
    def __init__(self):
        self.resources = {}

    def get_type(self, type):
        return self.resources.get(type)

    def get_uuid(self, uuid):
        for key in self.resources.keys():
            for value in self.resources[key]:
                if value.name == uuid:
                    return value

    def add(self, ob):
        t = type(ob)
        value = self.resources.pop(t, [])
        value.append(ob)
        self.resources.update({t: value})


class World(object):
    def __init__(self, spaces=150, form_func=()):
        self.num_spaces = spaces
        self.spaces = []
        form_func(self.spaces)
        self.resources = ResourceManager()

    def seed(self, seed_func: Callable[[Space], entity.Entity]):
        for space in self.spaces:
            ent = seed_func(space)
            self.resources.add(ent)

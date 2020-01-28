import uuid


class Entity(object):
    def __init__(self):
        self.name = uuid.uuid4()

    def step(self):
        pass

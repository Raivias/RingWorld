from agents import entity


class Agent(entity.Entity):
    def __init__(self, space, vision):
        super().__init__()
        self.vision = vision
        self.space = space

    def step(self):
        # Find Best closest space
        best_space = self.space
        prev_space = self.space
        for index in range(self.vision):
            current_space = prev_space.left_neighbor
            if current_space.spice.count > best_space.spice.count and current_space.agent is None:
                best_space = current_space
            prev_space = current_space

        # Move
        self.space.agent = None
        self.space = best_space
        self.space.agent = self

        # Eat Spice
        self.space.spice.count = 0
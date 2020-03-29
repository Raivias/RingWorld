from space import world


class Ring(world.World):
    def __init__(self, spaces=150):
        def form_func(space_list):
            first_space = world.Space()
            space_list.append(first_space)
            for i in range(spaces):
                prev_neighbor = space_list[len(space_list) - 1]
                new_space = world.Space()
                new_space.left_neighbor = prev_neighbor
                prev_neighbor.right_neighbor = new_space
                space_list.append(new_space)
            last_space = space_list[len(space_list) - 1]
            first_space.left_neighbor = last_space
            last_space.right_neighbor = first_space
        super().__init__(spaces, form_func)

    def print(self):
        for space in self.spaces:
            space.print()
        print()

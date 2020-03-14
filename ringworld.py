from agents import agent, spice
import argparse
import random
import time
from space import world, ring

description = "A simple multi-agent system. Colored cells are agents, numbers are spice"


class RingWorld(object):
    def __init__(self, spaces=150, agents=40, min_spice=0, max_spice=4, min_vision=15, max_vision=30):
        self.spaces = spaces
        self.agents = agents
        self.min_spice = min_spice
        self.max_spice = max_spice
        self.min_vision = min_vision
        self.max_vision = max_vision
        self.world = ring.Ring(spaces=spaces)

    def seed(self):
        def spice_seed(space: world.Space):
            sp = spice.Spice(random.randint(self.min_spice, self.max_spice), self.min_spice, self.max_spice)
            space.spice = sp
            return sp
        self.world.seed(spice_seed)

        # assign agents to spaces
        to_assign = self.agents
        if to_assign > len(self.world.spaces):
            raise Exception("Too many agents to assign")
        while to_assign > 0:
            rand_index = random.randint(0, len(self.world.spaces)-1)
            s = self.world.spaces[rand_index]
            if s.agent is None:
                a = agent.Agent(s, random.randint(self.min_vision, self.max_vision))
                s.agent = a
                self.world.resources.add(a)
                to_assign -= 1

    def run(self, steps=10):
        # print initial world
        self.seed()
        self.world.print()
        i = steps
        while i != 0:
            # Spices Grow
            spices = self.world.resources.get_type(spice.Spice)
            for s in spices:
                s.step()
            # Agents Move
            agents = self.world.resources.get_type(agent.Agent)
            random.shuffle(agents)
            for a in agents:
                a.step()
            time.sleep(0.2)
            self.world.print()
            i -= 1
        pass


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument("--cycles", help="Number of cycles to run", type=int, default=-1)
    parser.add_argument("--max_v", help="max agent vision", type=int, default=30)
    parser.add_argument("--min_v", help="min agent vision", type=int, default=15)

    args = parser.parse_args()

    ring_world = RingWorld(min_vision=args.min_v, max_vision=args.max_v)
    ring_world.run(args.cycles)

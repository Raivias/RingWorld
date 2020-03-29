import ringworld
import argparse

description = "A simple multi-agent system. Colored cells are agents, numbers are spice"

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument("--cycles", help="Number of cycles to run", type=int, default=-1)
    parser.add_argument("--max_v", help="max agent vision", type=int, default=30)
    parser.add_argument("--min_v", help="min agent vision", type=int, default=15)

    args = parser.parse_args()

    ring_world = ringworld.RingWorld(min_vision=args.min_v, max_vision=args.max_v)
    ring_world.run(args.cycles)

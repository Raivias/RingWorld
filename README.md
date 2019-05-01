# Ring World

Based on an example in ["Growing Artifical Societies" by Epstein and Axtell](https://mitpress.mit.edu/books/growing-artificial-societies), page 170-176. I figured this would be a good starting point for attempting to build a multi-agent environment.

## Rules

### Spice Rules
1) Spice grows a random amount up to it's max per cycle.

### Agent Rules
1) Agents cannot move into a space occupied by another agent.
2) Agents can only move in one direction.
3) Agents can only move up to their field of vision.
4) Agents move to the space with the highest spice.
5) Agents eat spice equal to their metabolism at the end of each turn.
6) Agents who don't have enough food die.

## Order of Operations

1) All spice grows. As they aren't affected by anything this can be done in any order.
2) Each agent moves. this is done in a random order to minimize bias in turn order.

## Other stuff

### Questions to explore
- What happens if an agent burns spice equal to what they move?
- What happens if an agent can see it's current space instead of move?
- How does having spice grow to max affect outcome?
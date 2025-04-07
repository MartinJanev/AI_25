from searching_framework import Problem, astar_search

WIDTH = 5
HEIGHT = 9

MOVEMENTS = {  # coordinate system
    "Stoj": (0, 0),  # No movement
    "Gore 1": (0, 1),  # Move up one row
    "Gore 2": (0, 2),  # Move up two rows
    "Gore-desno 1": (1, 1),  # Move up and right one row
    "Gore-desno 2": (2, 2),  # Move up and right two rows
    "Gore-levo 1": (-1, 1),  # Move up and left one row
    "Gore-levo 2": (-2, 2)  # Move up and left two rows
}


def move_house(house_pos, house_dir):
    """ Moves the house left or right, bouncing at the edges. """
    house_x, house_y = house_pos
    if 0 == house_x or house_x == WIDTH - 1:
        house_dir *= -1
    return (house_x + house_dir, house_y), house_dir


class ClimbingHuman(Problem):
    def __init__(self, initial, legal_spaces):
        """
        Initial: ((human_x, human_y), (house_x, house_y), house_dir)
        Legal spaces: Allowed positions for the human (green hexagons).
        """
        super().__init__(initial, goal=None)
        self.legal_spaces = set(legal_spaces)

    def is_valid(self, state):
        """ Checks if a given state is valid within the grid and movement constraints. """
        human_pos, house_pos, _ = state
        hx, hy = human_pos
        housex, housey = house_pos

        # Human must be within bounds
        if not (0 <= hx < WIDTH and 0 <= hy < HEIGHT):
            return False

        # House must be within bounds
        if not (0 <= housex < WIDTH and 0 <= housey < HEIGHT):
            return False

        # If human is on the top row, it must coincide with the house
        if hy == HEIGHT - 1:
            return human_pos == house_pos

        # Otherwise, human must be on an allowed (green hexagon) space
        if human_pos not in self.legal_spaces:
            return False

        return True

    def successor(self, state):
        """ Generates valid successor states for the human movement. """
        successors = {}
        human_pos, house_pos, house_dir = state

        # Move the house first
        new_house_pos, new_house_dir = move_house(house_pos, house_dir)

        for action, (dx, dy) in MOVEMENTS.items():
            new_human_pos = (human_pos[0] + dx, human_pos[1] + dy)
            new_state = (new_human_pos, new_house_pos, new_house_dir)

            if self.is_valid(new_state):
                successors[action] = new_state

        return successors

    def actions(self, state):
        """ Returns possible actions for the current state. """
        return list(self.successor(state).keys())

    def result(self, state, action):
        """ Applies the given action to the current state and returns the new state. """
        successors = self.successor(state)
        return successors.get(action, state)  # Ensure no KeyError

    def goal_test(self, state):
        """ The goal is reached when the human is inside the house. """
        human_pos, house_pos, _ = state
        return human_pos == house_pos

    def h(self, node):
        x, y = node.state[0]
        house_x, house_y = node.state[1]

        return abs(house_y - y) / 2


if __name__ == '__main__':
    allowed_positions = [(1, 0), (2, 0), (3, 0), (1, 1), (2, 1), (0, 2), (2, 2), (4, 2), (1, 3), (3, 3), (4, 3), (0, 4),
                         (2, 4), (2, 5), (3, 5), (0, 6), (2, 6), (1, 7), (3, 7)]

    # Read initial positions and direction
    human_x, human_y = map(int, input().split(","))
    house_x, house_y = map(int, input().split(","))
    house_dir = 1 if input().strip() == "desno" else -1

    initial_state = ((human_x, human_y), (house_x, house_y), house_dir)
    problem = ClimbingHuman(initial_state, allowed_positions)
    solution = astar_search(problem)
    print(solution.solution() if solution else "[]")

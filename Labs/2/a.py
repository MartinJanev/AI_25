from searching_framework import *

WIDTH = 5
HEIGHT = 9

MOVEMENTS = {
    "Stoj": (0, 0),
    "Gore 1": (0, 1),
    "Gore 2": (0, 2),
    "Gore-desno 1": (1, 1),
    "Gore-desno 2": (2, 2),
    "Gore-levo 1": (-1, 1),
    "Gore-levo 2": (-2, 2)
}


def move_house(house, direction):
    x, y = house
    if 0 == x or x == WIDTH - 1:
        direction *= (-1)
    return (x + direction, y), direction


class Game(Problem):

    def __init__(self, initial, goal=None):
        super().__init__(initial, goal)

    def successor(self, state):
        successors = {}

        human, house, house_d = state

        new_house, new_house_d = move_house(house, house_d)

        for action, (dx, dy) in MOVEMENTS.items():
            new_human = (human[0] + dx, human[1] + dy)
            new_state = (new_human, new_house, new_house_d)

            if self.is_valid(new_state):
                successors[action] = new_state

        return successors

    def is_valid(self, state):
        human, house,_ = state
        x, y = human
        house_x, house_y = house

        if not (0 <= x < WIDTH and 0 <= y < HEIGHT) or not (0 <= x < WIDTH and 0 <= y < HEIGHT):
            return False

        if y == HEIGHT - 1:
            return human == house

        if human not in allowed:
            return False

        return True

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        return state[0] == state[1]

    def h(self, node):
        x, y = node.state[0]
        house_x, house_y = node.state[1]

        return abs(y - house_y) / 2


if __name__ == '__main__':
    allowed = [(1, 0), (2, 0), (3, 0), (1, 1), (2, 1), (0, 2), (2, 2), (4, 2), (1, 3), (3, 3), (4, 3), (0, 4), (2, 4),
               (2, 5), (3, 5), (0, 6), (2, 6), (1, 7), (3, 7)]

    human = tuple(int(x) for x in input().split(","))
    house = tuple(int(x) for x in input().split(","))

    direction = 1 if input().strip() == "desno" else -1

    initial_state = (human, house, direction)

    game = Game(initial_state, tuple(allowed))
    solution = astar_search(game)

    if solution is not None:
        print(solution.solution())
    else:
        print("[]")

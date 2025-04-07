from searching_framework import Problem, breadth_first_graph_search

WIDTH = 8
HEIGHT = 6


def aroundOpp(opps):
    s1 = set()
    for i in range(-1, 2):
        for j in range(-1, 2):
            s1.add((opps[0] + i, opps[1] + j))
    return s1


def in_bounds(x):
    if 0 <= x[0] < WIDTH and 0 <= x[1] < HEIGHT:
        return True
    return False


def check_state(state, opps):
    if state[0] in opps:
        return False
    if state[1] in aroundOpp(opps[0]) or state[1] in aroundOpp(opps[1]):
        return False
    if in_bounds(state[0]) and in_bounds(state[1]):
        return True
    else:
        return False


class Football(Problem):

    def __init__(self, initial, opps, goal_block):
        super().__init__(initial, goal=None)
        self.opps = opps
        self.goal_block = goal_block

    def successor(self, state):
        successors = {}

        ways_to_move = (
            (0, 1),  # Up
            (1, 1),  # Up Right
            (1, 0),  # Right
            (1, -1),  # Down Right
            (0, -1)  # Down
        )

        actions_no_ball = (
            "Pomesti coveche gore", "Pomesti coveche gore-desno", "Pomesti coveche desno", "Pomesti coveche dolu-desno",
            "Pomesti coveche dolu")

        actions_with_ball = (
            "Turni topka gore", "Turni topka gore-desno", "Turni topka desno", "Turni topka dolu-desno",
            "Turni topka dolu")

        player, ball = state

        for way, actionBall, actionNoBall in zip(ways_to_move, actions_with_ball, actions_no_ball):
            new_coordinates = (player[0] + way[0], player[1] + way[1])
            if new_coordinates == ball:
                new_ball = (new_coordinates[0] + way[0], new_coordinates[1] + way[1])
                new_state = (new_coordinates, new_ball)
                if check_state(new_state, self.opps):
                    successors[actionBall] = new_state
            else:
                new_state = (new_coordinates, ball)
                if check_state(new_state, self.opps):
                    successors[actionNoBall] = new_state
        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        return state[1] in self.goal_block


if __name__ == '__main__':
    player = [int(num) for num in input().split(",")]
    ball = [int(num) for num in input().split(",")]

    opps = ((3, 3), (5, 4))
    goal_block = ((7, 2), (7, 3))

    initial_state = (tuple(player), tuple(ball))
    problem = Football(initial_state, opps, goal_block)
    res = breadth_first_graph_search(problem)
    if res is not None:
        print(res.solution())
    else:
        print("No Solution!")

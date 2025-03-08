from searching_framework import Problem, breadth_first_graph_search

WIDTH = 8
HEIGHT = 6


def aroundOpp(opponents):
    return {(opponents[0] + i, opponents[1] + j) for i in range(-1, 2) for j in range(-1, 2)}


def in_bounds(x):
    if 0 <= x[0] < WIDTH and 0 <= x[1] < HEIGHT:
        return True
    return False


def check_state(state, opponents):
    if state[0] in opponents:
        return False
    if state[1] in aroundOpp(opponents[0]) or state[1] in aroundOpp(opponents[1]):
        return False
    if in_bounds(state[0]) and in_bounds(state[1]):
        return True
    else:
        return False


class Football(Problem):

    def __init__(self, initial, opponents, goal_block):
        super().__init__(initial, goal=None)
        self.opponents = opponents
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

        for d, actionBall, actionNoBall in zip(ways_to_move, actions_with_ball, actions_no_ball):
            new_coords = (player[0] + d[0], player[1] + d[1])
            if new_coords == ball:
                new_ball = (new_coords[0] + d[0], new_coords[1] + d[1])
                new_state = (new_coords, new_ball)
                if check_state(new_state, self.opponents):
                    successors[actionBall] = new_state
            else:
                new_state = (new_coords, ball)
                if check_state(new_state, self.opponents):
                    successors[actionNoBall] = new_state
        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        return state[1] in self.goal_block


if __name__ == '__main__':
    player_pos = [int(num) for num in input().split(",")]
    ball_pos = [int(num) for num in input().split(",")]

    opps = ((3, 3), (5, 4))
    goal_block = ((7, 2), (7, 3))

    initial_state = (tuple(player_pos), tuple(ball_pos))
    problem = Football(initial_state, opps, goal_block)
    res = breadth_first_graph_search(problem)
    if res is not None:
        print(res.solution())
    else:
        print("No Solution!")

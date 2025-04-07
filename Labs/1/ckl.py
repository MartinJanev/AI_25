from searching_framework import Problem, breadth_first_graph_search

WIDTH = 8
HEIGHT = 6


def aroundOpp(opponents):
    s1 = set()
    for i in range(-1, 2):
        for j in range(-1, 2):
            s1.add((opponents[0] + i, opponents[1] + j))
    return s1


def in_bounds(x):
    if 0 <= x[0] < WIDTH and 0 <= x[1] < HEIGHT:
        return True
    return False


def check_gk(state):
    player, ball, gk = state
    gk_pos = (gk[0], gk[1])
    return player == gk_pos or ball == gk_pos


def check_state(state, opponents):
    if state[0] in opponents:
        return False
    if state[1] in aroundOpp(opponents[0]) or state[1] in aroundOpp(opponents[1]):
        return False
    if check_gk(state):
        return False
    if in_bounds(state[0]) and in_bounds(state[1]):
        return True
    else:
        return False


def move_keeper(keeper):
    gk = list(keeper)
    if gk[2] == 1:  # up
        if gk[1] == 5:
            gk[2] = 1
            gk[1] -= 1
        else:
            gk[1] += 1
    else:  # down
        if gk[1] == 0:
            gk[2] = 0
            gk[1] += 1
        else:
            gk[1] -= 1
    return tuple(gk)


class Football(Problem):

    def __init__(self, initial, opponents, goal_blocks):
        super().__init__(initial, goal=None)
        self.opps = opponents
        self.goal_block = goal_blocks

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

        p, b, gk = state

        for way, actionBall, actionNoBall in zip(ways_to_move, actions_with_ball, actions_no_ball):
            new_coordinates = (p[0] + way[0], p[1] + way[1])
            new_keeper = move_keeper(gk)
            gk = new_keeper

            if b == (new_keeper[0], new_keeper[1]):
                print("No Solution!")
                return None

            if new_coordinates == b:
                new_ball = (new_coordinates[0] + way[0], new_coordinates[1] + way[1])
                new_state = (new_coordinates, new_ball, new_keeper)
                if check_state(new_state, self.opps):
                    successors[actionBall] = new_state
            else:
                new_state = (new_coordinates, b, new_keeper)
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
    goalkeeper = (6, 1, 1)  # 1 up 0 down
    goal_block = ((7, 1), (7, 2), (7, 3), (7, 4))

    initial_state = (tuple(player), tuple(ball), goalkeeper)
    problem = Football(initial_state, opps, goal_block)
    res = breadth_first_graph_search(problem)
    if res is not None:
        print(res.solution())
    else:
        print("No Solution!")

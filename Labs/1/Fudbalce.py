from searching_framework import Problem, breadth_first_graph_search

WIDTH = 8
HEIGHT = 6


def aroundOpp(opponent):
    s1 = set()
    for i in range(-1, 2):
        for j in range(-1, 2):
            s1.add((opponent[0] + i, opponent[1] + j))
    return s1


def in_bounds(x):
    return 0 <= x[0] < WIDTH and 0 <= x[1] < HEIGHT

# функција за 2 ДЕЛ
def check_gk(state):
    player, ball, gk = state
    gk_pos = (gk[0], gk[1])
    return player == gk_pos or ball == gk_pos


def check_state(state, opponents):
    # Проверуваме дали играчот не застанува на полето на противникот
    if state[0] in opponents:
        return False
    # Проверуваме дали топката не е во соседство на некој од противниците
    for opp in opponents:
        if state[1] in aroundOpp(opp):
            return False
    # Играчот или топката не можат да бидат на исто поле како голманот - 2 ДЕЛ
    if check_gk(state):
        return False
    if in_bounds(state[0]) and in_bounds(state[1]):
        return True
    else:
        return False

# функција за 2 ДЕЛ
def move_keeper(keeper):
    # keeper е tuple (x, y, d) каде d==1 значи движење нагоре, d==0 - надолу.
    x, y, d = keeper
    if d == 1:  # движење нагоре
        if y == 5:  # достигнат е горниот дозволен ред (6,4)
            moved = (x, y - 1, 0)  # сменуваме го правецот - сега се движи надолу
        else:
            moved = (x, y + 1, 1)
    else:  # движење надолу
        if y == 1:  # достигнат е долниот дозволен ред
            moved = (x, y + 1, 1)  # сменуваме го правецот - сега се движи нагоре
        else:
            moved = (x, y - 1, 0)

    return moved


class Football(Problem):

    def __init__(self, initial, opponents, goal_blocks):
        super().__init__(initial, goal=None)
        self.opps = opponents
        self.goal_block = goal_blocks

    def successor(self, state):
        successors = {}

        ways_to_move = [
            (0, 1),  # горе
            (1, 1),  # горе-десно
            (1, 0),  # десно
            (1, -1),  # долу-десно
            (0, -1)  # долу
        ]

        actions_no_ball = [
            "Pomesti coveche gore",
            "Pomesti coveche gore-desno",
            "Pomesti coveche desno",
            "Pomesti coveche dolu-desno",
            "Pomesti coveche dolu"
        ]

        actions_with_ball = [
            "Turni topka gore",
            "Turni topka gore-desno",
            "Turni topka desno",
            "Turni topka dolu-desno",
            "Turni topka dolu"
        ]

        p, b, gk = state

        for way, actionBall, actionNoBall in zip(ways_to_move, actions_with_ball, actions_no_ball):
            new_player = (p[0] + way[0], p[1] + way[1])

            # Пресметуваме новата позиција на голманот за секој потег посебно - 2 ДЕЛ
            new_keeper = move_keeper(gk)
            # Доколку топката се најде на полето каде што ќе поместиме голманот, го прескокуваме овој потег - 2 ДЕЛ
            if b == (new_keeper[0], new_keeper[1]):
                continue

            if new_player == b:
                # Ако играчот ќе влезе во полето каде што е топката, тогаш топката се турка во иста насока
                new_ball = (b[0] + way[0], b[1] + way[1])
                new_state = (new_player, new_ball, new_keeper)
                if check_state(new_state, self.opps):
                    successors[actionBall] = new_state
            else:
                new_state = (new_player, b, new_keeper)
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
    goalkeeper = (6, 1, 1)  # Голманот почнува на (6,1) и се движи нагоре - 2 ДЕЛ
    goal_block = ((7, 1), (7, 2), (7, 3), (7, 4)) # Голот е на (7,1), (7,2) во првиот дел

    initial_state = (tuple(player), tuple(ball), goalkeeper) # во 2 ДЕЛ се додава голманот
    problem = Football(initial_state, opps, goal_block)
    res = breadth_first_graph_search(problem)
    if res is not None:
        print(res.solution())
    else:
        print("No Solution!")

from searching_framework import *


class Laser(Problem):
    def __init__(self, initial, blocks, laser, goal, N, M):
        super().__init__(initial)
        self.blocks = blocks
        self.goal = goal
        self.laser = laser
        self.WIDTH = N
        self.HEIGHT = M

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        return state[0] == self.goal

    def successor(self, state):
        successors = {}

        man_x, man_y = state[0]
        timer = state[1]

        if timer == 1:
            self.laser = (man_x, man_y)

        dirs = {"Gore": (0, +1), "Dolu": (0, -1), "Levo": (-1, 0), "Desno": (+1, 0), "Stoj": (0, 0)}

        for action, (x, y) in dirs.items():
            new_x, new_y = (man_x + x, man_y + y)
            temp_timer = timer
            temp_timer += 1
            if temp_timer == 4:
                if new_x == self.laser[0] or new_y == self.laser[1]:
                    continue
                else:
                    timer = 1
            new_state = ((new_x, new_y), timer)
            if 0 <= new_x < self.WIDTH and 0 <= new_y < self.HEIGHT and (new_x, new_y) not in self.blocks:
                successors[action] = new_state

        return successors


read_two = lambda: tuple(map(int,input().split()))
if __name__ == '__main__':
    N, M = read_two()
    man_pos = read_two()
    target_pos = read_two()
    timer = int(input())
    laser_pos = read_two()
    blocked = [read_two() for _ in range(int(input()))]

    initial = (man_pos, timer)
    problem = Laser(initial, tuple(blocked), laser_pos, target_pos, N, M)

    result = breadth_first_graph_search(problem)

    if result is not None:
        print(result.solution())

    else:
        print("No Solution!")

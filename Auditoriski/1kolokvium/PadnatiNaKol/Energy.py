
from searching_framework import *


class Energy(Problem):
    def __init__(self, N, M, prepreki, initial, goal):
        super().__init__(initial, goal)
        self.prepreki = prepreki
        self.N = N
        self.M = M

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        x, y = state[0]
        x_goal, y_goal = self.goal

        return x == x_goal and y == y_goal

    def successor(self, state):
        successors = {}
        x, y = state[0]
        curr_timer = state[1]
        my_energy = state[2]

        if True:
            new_energy = my_energy
            new_timer = curr_timer
            if curr_timer == 4:
                new_timer = 1
            else:
                new_timer += 1
            if my_energy > 5:
                new_energy = 5
            if new_timer == 1:
                new_energy += 1
            successors['Stoj'] = ((x, y + 1), new_timer, new_energy)

        if 0 <= y + 1 < self.N and (x, y + 1) not in self.prepreki:
            new_energy = my_energy
            new_timer = curr_timer
            if curr_timer == 4:
                new_timer = 1
            else:
                new_timer += 1
            if my_energy > 5:
                new_energy = 5
            if new_timer == 1:
                new_energy += 1
            successors['Gore'] = ((x, y + 1), new_timer, new_energy)

        if 0 <= y - 1 < self.N and (x, y - 1) not in self.prepreki:
            new_energy = my_energy
            new_timer = curr_timer
            if curr_timer == 4:
                new_timer = 1
            else:
                new_timer += 1
            if my_energy > 5:
                new_energy = 5
            if new_timer == 1:
                new_energy += 1
            successors['Dolu'] = ((x, y - 1), new_timer, new_energy)

        if 0 <= x + 1 < self.M and (x + 1, y) not in self.prepreki:
            new_energy = my_energy
            new_timer = curr_timer
            if curr_timer == 4:
                new_timer = 1
            else:
                new_timer += 1
            if my_energy > 5:
                new_energy = 5
            if new_timer == 1:
                new_energy += 1
            successors['Desno'] = ((x + 1, y), new_timer, new_energy)

        if 0 <= x - 1 < self.M and (x - 1, y) not in self.prepreki:
            new_energy = my_energy
            new_timer = curr_timer
            if curr_timer == 4:
                new_timer = 1
            else:
                new_timer += 1
            if my_energy > 5:
                new_energy = 5
            if new_timer == 1:
                new_energy += 1
            successors['Levo'] = ((x - 1, y), new_timer, new_energy)

        for e in range(1, my_energy+1):
            if 0 <= y + 1+e < self.N and (x, y + 1+e) not in self.prepreki:
                new_energy = my_energy-e
                new_timer = curr_timer
                if curr_timer == 4:
                    new_timer = 1
                else:
                    new_timer += 1
                if new_energy > 5:
                    new_energy = 5
                if new_timer == 1:
                    new_energy += 1
                successors[f'Gore+{e}'] = ((x, y + 1+e), new_timer, new_energy)

            if 0 <= x - 1-e < self.M and (x - 1-e, y) not in self.prepreki:
                new_energy = my_energy-e
                new_timer = curr_timer
                if curr_timer == 4:
                    new_timer = 1
                else:
                    new_timer += 1
                if new_energy > 5:
                    new_energy = 5
                if new_timer == 1:
                    new_energy += 1
                successors[f'Levo+{e}'] = ((x - 1-e, y), new_timer, new_energy)

            if 0 <= x + 1+e < self.M and (x + 1+e, y) not in self.prepreki:
                new_energy = my_energy-e
                new_timer = curr_timer
                if curr_timer == 4:
                    new_timer = 1
                else:
                    new_timer += 1
                if new_energy > 5:
                    new_energy = 5
                if new_timer == 1:
                    new_energy += 1
                successors[f'Desno+{e}'] = ((x + 1+e, y), new_timer, new_energy)

            if 0 <= y - 1-e < self.N and (x, y - 1-e) not in self.prepreki:
                new_energy = my_energy-e
                new_timer = curr_timer
                if curr_timer == 4:
                    new_timer = 1
                else:
                    new_timer += 1
                if new_energy > 5:
                    new_energy = 5
                if new_timer == 1:
                    new_energy += 1
                successors[f'Dolu+{e}'] = ((x, y - 1-e), new_timer, new_energy)
        return successors


read_two = lambda: tuple(map(int, input().split()))
if __name__ == '__main__':
    N, M = read_two()
    start = read_two()
    goal = read_two()
    timer = int(input())
    energy = int(input())
    K = int(input())
    blocked = [read_two() for _ in range(K)]

    initial = (start, timer, energy)

    problem = Energy(N, M, blocked, initial, goal)

    result = breadth_first_graph_search(problem)
    if result is not None:
        print(result.solution())
    else:
        print('No solution!')
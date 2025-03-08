# na nas ke ni e dadena klasa Problem, od koj sto nie ke nasledime
# karakteistiki i f-ii za resavanje na problemot


"""
Дадени се два сада J0 и J1, со капацитети C0 и C1 литри, соодветно. Да се доведат до состојба во која J0 има G0 литри, а J1 има G1 литри. Акции:

Испразни кој било од садовите
Претури течност од еден во друг сад, со тоа што не може да се надмине капацитетот на садот
Наполни кој било од садовите (за дома)
"""

from searching_framework.utils import Problem
from searching_framework.uninformed_search import *


class Container(Problem):
    def __init__(self, capacities, initial, goal=None):
        super().__init__(initial, goal)
        self.capacities = capacities

    def successor(self, state):
        successors = dict()

        # (j0,j1)
        j0, j1 = state
        c0, c1 = self.capacities

        # isprazni j0
        if j0 > 0:
            successors["Isprazni go sadot J0"] = (0, j1)

        # isprazni j1
        if j1 > 0:
            successors["Isprazni go sadot J1"] = (j0, 0)

        # j0 vo j1

        if j0 > 0 and j1 < c1:
            d_liquid = min(j0, c1 - j1)
            successors["Preturi od J0 vo J1"] = (j0 - d_liquid, j1 + d_liquid)

        # j1 vo j0

        if j1 > 0 and j0 < c0:
            d_liquid = min(j1, c0 - j0)
            successors["Preturi od J1 vo J0"] = (j0 + d_liquid, j1 - d_liquid)

        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        return state == self.goal


if __name__ == '__main__':
    capacities = (15, 5)
    initial = (5, 5)
    goal = (10, 0)


    problem = Container(capacities, initial, goal)

    print(depth_first_graph_search(problem).solution())
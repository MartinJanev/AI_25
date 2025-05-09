from searching_framework.utils import *
from searching_framework.uninformed_search import *
from searching_framework.informed_search import *


class Boxes(Problem):
    def __init__(self, initial, n, boxes, goal=None):
        super().__init__(initial, goal)
        self.n = n
        self.boxes = boxes

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        return len(state[1]) == 0

    def successor(self, state):
        successors = {}

        pos = state[0]
        x, y = pos
        filled = list(state[1])

        moves = {
            "Dolu": (x, y - 1),
            "Levo": (x - 1, y)
        }

        for action, (new_x, new_y) in moves.items():
            if 0 <= new_x < self.n and 0 <= new_y < self.n and (new_x, new_y) not in self.boxes:
                newFilled = filled[:]

                for box in self.boxes:
                    if max(abs(new_x - box[0]), abs(new_y - box[1])) == 1 and box in newFilled:
                        newFilled.remove(box)

                successors[action] = ((new_x, new_y), tuple(newFilled))

        return successors


if __name__ == '__main__':
    n = int(input())
    man_pos = (n - 1, n - 1)

    num_boxes = int(input())
    boxes = [tuple(map(int, input().split(','))) for _ in range(num_boxes)]

    initial_state = (man_pos, tuple(boxes))

    problem = Boxes(initial_state, n, boxes)
    s = breadth_first_graph_search(problem)

    if s is not None:
        print(s.solution())
    else:
        print("No Solution!")

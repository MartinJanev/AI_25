from searching_framework import *


# vtora varijanta e pocnuva od drugotot kose i saka da sobira od site i plus e informirano prebaruvanje

class Boxes(Problem):
    def __init__(self, initial, n, boxes, goal=None):
        self.n = n
        self.boxes = boxes
        super().__init__(initial, goal)

    def successor(self, state):
        x, y = state[0]
        filled = state[1]
        remaining = state[2]
        successors = dict()

        # Gore
        new_x, new_y = x, y + 1
        if new_y < self.n and (new_x, new_y) not in self.boxes:
            new_filled = set(filled)
            new_remaining = remaining
            for box in self.boxes:
                # Chebyshev distance
                if box not in new_filled and max(abs(new_x - box[0]), abs(new_y - box[1])) == 1 and \
                        new_remaining > 0:
                    new_filled.add(box)
                    new_remaining -= 1
            successors["Gore"] = ((new_x, new_y), tuple(new_filled), new_remaining)
        # Desno
        new_x, new_y = x + 1, y
        if new_x < n and (new_x, new_y) not in self.boxes:
            new_filled = list(filled)
            new_remaining = remaining
            for box in self.boxes:
                # Chebyshev distance
                # max(abs(x1,x2), abs(y1,y2))
                if box not in new_filled and max(abs(new_x - box[0]), abs(new_y - box[1])) == 1 and \
                        new_remaining > 0:
                    new_filled.append(box)
                    new_remaining -= 1
            successors["Desno"] = ((new_x, new_y), tuple(new_filled), new_remaining)

        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        filled = state[1]
        return len(filled) == len(self.boxes)


if __name__ == '__main__':
    n = int(input())
    man_pos = (0, 0)

    num_boxes = int(input())
    boxes = list()
    for _ in range(num_boxes):
        boxes.append(tuple(map(int, input().split(","))))

    remaining_boxes = ()
    initial = (man_pos, remaining_boxes, num_boxes)
    prob = Boxes(initial, n, boxes)

    res = breadth_first_graph_search(prob)
    if res is not None:
        print(res.solution())
    else:
        print("No Solution!")

from searching_framework import *

WIDTH = 10
HEIGHT = 10


def isValid(snake, redApples):
    # if the snake is touching itself - во 2 дел се брише и е зелена
    if len(snake) != len(set(snake)):
        return False
    # if it is touching a red apple
    for coord in snake:
        if coord in redApples:
            return False
    # if it is out of bounds
    return 0 <= snake[-1][0] < WIDTH and 0 <= snake[-1][1] < HEIGHT


def move_forward(state):
    snake, sDir, greenApples = state
    movements = {
        "l": (-1, 0),
        "r": (1, 0),
        "u": (0, 1),
        "d": (0, -1)
    }
    new_head = (snake[-1][0] + movements[sDir][0], snake[-1][1] + movements[sDir][1])
    if new_head in greenApples:
        newSnake = snake + (new_head,)
        newGreenApples = tuple(apple for apple in greenApples if apple != new_head)
        new_state = (newSnake, sDir, newGreenApples)
        return new_state

    else:
        # Змијата се движи, без да се издолжува
        newSnake = snake[1:] + (new_head,)
        new_state = (newSnake, sDir, greenApples)
        return new_state


def move_right(state):
    snake, sDir, greenApples = state
    movements = {
        "l": (0, 1, "u"),
        "r": (0, -1, "d"),
        "u": (1, 0, "r"),
        "d": (-1, 0, "l")
    }
    new_dir = movements[sDir][2]
    new_head = (snake[-1][0] + movements[sDir][0], snake[-1][1] + movements[sDir][1])
    if new_head in greenApples:
        newSnake = snake + (new_head,)
        newGreenApples = tuple(apple for apple in greenApples if apple != new_head)
        new_state = (newSnake, new_dir, newGreenApples)
        return new_state
    else:
        newSnake = snake[1:] + (new_head,)
        new_state = (newSnake, new_dir, greenApples)
        return new_state


def move_left(state):
    snake, sDir, greenApples = state
    movements = {
        "l": (0, -1, "d"),
        "r": (0, 1, "u"),
        "u": (-1, 0, "l"),
        "d": (1, 0, "r")
    }
    new_dir = movements[sDir][2]
    new_head = (snake[-1][0] + movements[sDir][0], snake[-1][1] + movements[sDir][1])
    if new_head in greenApples:
        newSnake = snake + (new_head,)
        newGreenApples = tuple(apple for apple in greenApples if apple != new_head)
        new_state = (newSnake, new_dir, newGreenApples)
        return new_state
    else:
        newSnake = snake[1:] + (new_head,)
        new_state = (newSnake, new_dir, greenApples)
        return new_state


class Snake(Problem):
    def __init__(self, initial, redApples):
        super().__init__(initial, goal=None)
        self.redApples = redApples


    def successor(self, state):
        successors = {}
        fState = move_forward(state)
        rState = move_right(state)
        lState = move_left(state)

        if isValid(fState[0], self.redApples):
            successors["ProdolzhiPravo"] = fState
        if isValid(rState[0], self.redApples):
            successors["SvrtiDesno"] = rState
        if isValid(lState[0], self.redApples):
            successors["SvrtiLevo"] = lState
        return successors

    def actions(self, state):
        return list(self.successor(state).keys())

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        return len(state[2]) == 0


if __name__ == '__main__':

    n = int(input())
    greenApples = []
    for i in range(n):
        x, y = input().split(",")
        greenApples.append((int(x), int(y)))

    # greenApples = [tuple(map(int, input().split(","))) for _ in range(n)]

    m = int(input())
    redApples = []
    for i in range(m):
        x, y = input().split(",")
        redApples.append((int(x), int(y)))

    # redApples = [tuple(map(int, input().split(","))) for _ in range(m)]

    initial_snake = ((0, 9), (0, 8), (0, 7))
    initial_direction = "d"
    initial_state = (initial_snake, initial_direction, tuple(greenApples))

    game = Snake(initial_state, tuple(redApples))
    solution = breadth_first_graph_search(game)
    if solution is not None:
        print(solution.solution())
    else:
        print("[]")

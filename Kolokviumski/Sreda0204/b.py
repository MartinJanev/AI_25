from constraint import *


def func(t1, t2):
    return max(abs(t1[0] - t2[0]), abs(t1[1] - t2[1])) > 1


if __name__ == '__main__':
    problem = Problem(BacktrackingSolver())

    # ----------------------------------------------------
    # ---Prochitajte gi informaciite od vlezot
    n = int(input())
    trees = []

    for _ in range(n):
        x, y = tuple(int(x) for x in input().split())
        trees.append((x, y))

    dirs = [
        (0, 1),
        (0, -1),
        (1, 0),
        (-1, 0)
    ]

    for tree in trees:
        x, y = tree
        domen = []

        for dx, dy in dirs:
            if 0 <= x+dx < 6 and 0 <= y+dy < 6 and (x + dx, y + dy) not in trees:
                domen.append((x + dx, y + dy))
        problem.addVariable(tree, domen)
    # -----------------------------------------------------
    # ---Potoa dodadete ogranichuvanjata-------------------

    problem.addConstraint(AllDifferentConstraint(), trees)

    for i in trees:
        for j in trees:
            if i != j:
                problem.addConstraint(func, (i,j))

    solution = problem.getSolution()

    for t in trees:
        print(solution[t][0], solution[t][1])

    # -----------------------------------------------------
    # ---Na kraj otpechatete gi poziciite na shatorite-----

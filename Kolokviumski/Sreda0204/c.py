from constraint import *

# potsetuvanje
# def count_in_col_i(*args):
#     # ovaa funkcija mozhe da se povika so bilo kolku argumenti, koi kje se dostapni vo nizata args

global cols


def tents_per_cols(*args):
    for i in range(6):
        tents_col = 0
        for tents in args:
            if tents[0] == i:
                tents_col += 1
        if tents_col != cols[i]:
            return False
    return True


if __name__ == '__main__':
    problem = Problem(BacktrackingSolver())
    n = int(input())
    trees = []
    for _ in range(n):
        x, y = tuple(int(x) for x in input().split())
        trees.append((x, y))

    cols = [int(x) for x in input().split()]

    dirs = [
        (0, 1),
        (1, 0),
        (0, -1),
        (-1, 0),
    ]

    for tree in trees:
        x, y = tree
        domen = []
        for dx, dy in dirs:
            if 0 <= x + dx < 6 and 0 <= y + dy < 6 and (x + dx, y + dy) not in trees:
                domen.append((x + dx, y + dy))
        problem.addVariable(tree, domen)

    problem.addConstraint(AllDifferentConstraint(), trees)
    problem.addConstraint(tents_per_cols, trees)

    sol = problem.getSolution()
    for t in trees:
        print(sol[t][0], sol[t][1])

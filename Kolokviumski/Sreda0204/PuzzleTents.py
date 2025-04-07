from constraint import *


# Part 1

global col
#
# def not_adjacent(tree1, tree2): #part1
#     return max(abs(tree1[0] - tree2[0]), abs(tree1[1] - tree2[1])) > 1

def count_in_col(*trees): #part2
    for i in range(6):
        tents_in_col = 0
        for tent in trees:
            if tent[0] == i:
                tents_in_col += 1
        if tents_in_col != cols[i]:
            return False
    return True

if __name__ == '__main__':
    problem = Problem(BacktrackingSolver())
    n = int(input())
    trees = []

    for _ in range(n):
        x, y = tuple(map(int, input().split()))
        trees.append((x, y))
        # tree = tuple([int(e) for e in input().split(" ")])
        # trees.append(tree)

    cols = [int(e) for e in input().split(" ")] # part2

    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    for tree in trees:
        x, y = tree
        domain = []
        for dx, dy in dirs:
            if 0 <= x + dx < 6 and 0 <= y + dy < 6 and (x + dx, y + dy) not in trees:
                domain.append((x + dx, y + dy))

        problem.addVariable(tree, domain)

    problem.addConstraint(AllDifferentConstraint(), trees)  # this means that all trees must have different tents

    problem.addConstraint(count_in_col, trees) #part2

    # #part1
    # for tree1 in trees:
    #     for tree2 in trees:
    #         # this means that all trees must have different tents, no 2 tents can be on the same tree
    #         if tree1 != tree2: problem.addConstraint(not_adjacent, (tree1, tree2))  #

    solution = problem.getSolution()

    for t in trees:
        print(solution[t][0], solution[t][1])

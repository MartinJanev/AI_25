from constraint import *
from timer import profiler


@profiler
def main():
    problem = Problem(BacktrackingSolver())

    # n=int(input())
    n = 4

    variables = []

    for i in range(n):
        for j in range(n):
            variables.append((i, j))
    problem.addVariables(variables, [1, 0])

    # def notAttack(cannon1, cannon2):
    # def notAttack(*cannons)
    #     row1, col1 = cannon1
    #     row2, col2 = cannon2
    #     return row1 != row2 and col1 != col2

    problem.addConstraint(ExactSumConstraint(n), variables)

    for i in range(n):
        for j1 in range(n):
            for j2 in range(j1 + 1, n):
                problem.addConstraint(MaxSumConstraint(1), [(i, j1), (i, j2)])
                # problem.addConstraint(notAttack, [(i, j1), (i, j2)])
                # bez zagrada, zasto ni treba referenca

    for j in range(n):
        for i1 in range(n):
            for i2 in range(i1 + 1, n):
                problem.addConstraint(MaxSumConstraint(1), [(i1, j), (i2, j)])
                # problem.addConstraint(notAttack(3), [(i1, j), (i2, j)])

    solution = problem.getSolution()

    # print(solution)

    for i in range(n):
        for j in range(n):
            print(solution[(i, j)], end=' ')
        print()


if __name__ == '__main__':
    main()

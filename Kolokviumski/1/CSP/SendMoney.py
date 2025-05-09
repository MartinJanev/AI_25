from constraint import *


def const(*args):
    sum1 = 1000 * args[0] + 100 * args[1] + 10 * args[2] + args[3]
    sum2 = 1000 * args[4] + 100 * args[5] + 10 * args[6] + args[1]
    return sum1 + sum2 == args[4] * 10000 + args[5] * 1000 + args[2] * 100 + args[1] * 10 + args[7]


if __name__ == '__main__':
    problem = Problem(BacktrackingSolver())
    variables = ["S", "E", "N", "D", "M", "O", "R", "Y"]
    for variable in variables:
        problem.addVariable(variable, Domain(set(range(10))))

    # ---Tuka dodadete gi ogranichuvanjata----------------

    problem.addConstraint(AllDifferentConstraint(), variables)
    problem.addConstraint(const, variables)

    # ----------------------------------------------------

    print(problem.getSolution())

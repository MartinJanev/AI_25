from constraint import *
from timer import profiler

@profiler
def main():
    problem = Problem(BacktrackingSolver())
    # problem = Problem(MinConflictsSolver())

    # Be careful of addVariables() and addVariable()

    variables = ["WA", "NT", "SA", "Q", "NSW", "V", "T"]
    domain = ["red", "green", "blue"]

    problem.addVariables(variables, domain)

    problem.addConstraint(lambda a, b: a != b, ("WA", "SA"))
    problem.addConstraint(lambda a, b: a != b, ("SA", "NT"))
    problem.addConstraint(lambda a, b: a != b, ("SA", "NSW"))
    problem.addConstraint(lambda a, b: a != b, ("SA", "Q"))
    problem.addConstraint(lambda a, b: a != b, ("SA", "V"))
    problem.addConstraint(lambda a, b: a != b, ("NT", "Q"))
    problem.addConstraint(lambda a, b: a != b, ("Q", "NSW"))
    problem.addConstraint(lambda a, b: a != b, ("NSW", "V"))

    print(problem.getSolution())


if __name__ == "__main__":
    main()
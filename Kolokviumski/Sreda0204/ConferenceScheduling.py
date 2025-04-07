from constraint import *


def papers_per_slot(*papers):
    timeslots = set(papers)
    for slot in timeslots:
        if papers.count(slot) > 4:
            return False
    return True


if __name__ == '__main__':
    num = int(input())

    papers = dict()

    paper_info = input()
    while paper_info != 'end':
        title, topic = paper_info.split(' ')
        papers[title] = topic
        paper_info = input()

    # Tuka definirajte gi promenlivite
    variables = [k for k in papers.keys()]
    var_ai = [k for k, v in papers.items() if v == 'AI']
    var_ml = [k for k, v in papers.items() if v == 'ML']
    var_nlp = [k for k, v in papers.items() if v == 'NLP']

    domain = [f'T{i + 1}' for i in range(num)]

    problem = Problem(BacktrackingSolver())
    problem.addVariables(variables, domain)

    # Dokolku vi e potrebno moze da go promenite delot za dodavanje na promenlivite
    problem.addVariables(variables, domain)

    # Tuka dodadete gi ogranichuvanjata
    problem.addConstraint(papers_per_slot, variables)

    if 0 < len(var_ai) <= 4:
        problem.addConstraint(AllEqualConstraint(), var_ai)
    if 0 < len(var_ml) <= 4:
        problem.addConstraint(AllEqualConstraint(), var_ml)
    if 0 < len(var_nlp) <= 4:
        problem.addConstraint(AllEqualConstraint(), var_nlp)

    result = problem.getSolution()

    for paper in variables:
        topic = papers[paper]
        ts = result[paper]
        print(f"{paper} ({topic}): {ts}")

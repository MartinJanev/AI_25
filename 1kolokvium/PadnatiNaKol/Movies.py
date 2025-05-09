from constraint import *


def must_hall1(match):
    x = match[2]
    if x != 1:
        return False
    else:
        return True


def same_time(match1, match2):
    time1 = match[1]
    time2 = match2[1]
    if time1 != time2:
        return False
    else:
        return True


def difference_needed(match1, match2):
    hall1 = match1[2]
    hall2 = match2[2]
    day1 = match1[0]
    day2 = match2[0]

    if hall1 == hall2 and day1 == day2:
        time1 = match1[1]
        time2 = match2[1]
        if abs(time1 - time2) < 3:
            return False
        else:
            return True

    return True


if __name__ == '__main__':
    problem = Problem(BacktrackingSolver())

    matches = dict()

    n = int(input())
    for _ in range(n):
        match_info = input()
        match, category = match_info.split(' ')
        matches[match] = category

    l_days = int(input())

    print()
    # Tuka definirajte gi promenlivite i domenite
    variables = []
    kategorija1 = []
    kategorija3 = []
    kategorija4 = []
    for i in matches.keys():
        variables.append(i)
        if matches[i] == "category1":
            kategorija1.append(i)
        if matches[i] == "category3":
            kategorija3.append(i)
        if matches[i] == "category4":
            kategorija4.append(i)

    hours = []
    for i in range(9, 16):
        hours.append(i)

    days = []
    for i in range(1, l_days + 1):
        days.append(i)

    halls = [1, 2]

    domain = []  # (day, hour, hall)
    for i in days:
        for j in hours:
            for k in halls:
                domain.append((i, j, k))

    problem.addVariables(variables, domain)
    # Tuka dodadete gi ogranichuvanjata
    problem.addConstraint(AllDifferentConstraint, variables)
    if len(kategorija1) > 0:
        problem.addConstraint(must_hall1, kategorija1)
    for i in range(len(kategorija3)):
        for j in range(i + 1, len(kategorija3)):
            problem.addConstraint(same_time, [kategorija3[i], kategorija3[j]])

    for i in range(len(kategorija4)):
        for j in range(i + 1, len(kategorija4)):
            problem.addConstraint(same_time, [kategorija4[i], kategorija4[j]])

    for i in range(len(variables)):
        for j in range(i + 1, len(variables)):
            problem.addConstraint(difference_needed, [variables[i], variables[j]])

    result = problem.getSolution()
    print(result)
    # Tuka dodadete go kodot za pechatenje
    ...

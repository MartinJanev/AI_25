# from constraint import *
#
# if __name__ == '__main__':
#     num = int(input())
#
#     papers = dict()
#     paper_info = input()
#     while paper_info != 'end':
#         title, topic = paper_info.split(' ')
#         papers[title] = topic
#         paper_info = input()
#
#     variables = list(papers.keys())
#     domain = [f'T{i + 1}' for i in range(num)]
#
#     problem = Problem(BacktrackingSolver())
#     problem.addVariables(variables, domain)
#
#     # Групирање на трудовите по област
#     topic_groups = {}
#     for paper, topic in papers.items():
#         if topic not in topic_groups:
#             topic_groups[topic] = []
#         topic_groups[topic].append(paper)
#
#     # Ако бројот на трудови во некоја област е <= 4, тие мора да бидат во ист термин
#     for group in topic_groups.values():
#         if len(group) <= 4:
#             problem.addConstraint(lambda *args: len(set(args)) == 1, group)
#
#
#     # Максимум 4 трудови во еден термин
#     def max_four_per_session(*args):
#         return all(args.count(session) <= 4 for session in set(args))
#
#
#     problem.addConstraint(max_four_per_session, variables)
#
#     def sort_by_paper_id(items):
#         return sorted(items, key=lambda x: int(x[0][5:]))
#
#     result = problem.getSolution()
#
#     if result:
#         sorted_result = sort_by_paper_id(result.items())
#         for paper, session in sorted_result:
#             print(f"{paper} ({papers[paper]}): {session}")
#     else:
#         print("No valid schedule found.")


from constraint import *


def same_session(*args):
    return len(set(args)) == 1


def max_4_per_session(*args):
    return all(args.count(s) <= 4 for s in set(args))


def sort_by_id(items):
    return sorted(items, key=lambda x: int(x[0][5:]))


if __name__ == '__main__':
    num = int(input())

    papers = dict()

    paper_info = input()
    while paper_info != 'end':
        title, topic = paper_info.split(' ')
        papers[title] = topic
        paper_info = input()

    variables = list(papers.keys())
    domain = [f'T{i + 1}' for i in range(num)]

    problem = Problem(BacktrackingSolver())
    problem.addVariables(variables, domain)

    topic_group = {}
    for paper, topic in papers.items():
        if topic not in topic_group:
            topic_group[topic] = []
        topic_group[topic].append(paper)

    for group in topic_group.values():
        if len(group) <= 4:
            problem.addConstraint(same_session, group)

    problem.addConstraint(max_4_per_session, variables)

    result = problem.getSolution()

    if result:
        for paper, session in sort_by_id(result.items()):
            print(f"{paper} ({papers[paper]}): {session}")
    else:
        print("No valid schedule found.")

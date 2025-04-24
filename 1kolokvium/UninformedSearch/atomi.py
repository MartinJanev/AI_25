from searching_framework.utils import Problem
from searching_framework.uninformed_search import *

"""
Предложете соодветна репрезентација и напишете ги потребните функции во Python за да се реши следниот проблем за кој една можна почетна состојба е прикажана на сликата на следниот слајд.

На табла 7x9 поставени се три атоми (внимавајте, двата H-атоми се различни: едниот има линк во десно, а другиот има линк во лево). Полињата обоени во сива боја претставуваат препреки.

Играчот може да ја започне играта со избирање на кој било од трите атоми. Играчот во секој момент произволно избира точно еден од трите атоми и го „турнува“ тој атом во една од четирите насоки: горе, долу, лево или десно.

Движењето на „турнатиот“ атом продолжува во избраната насока се’ додека атомот не „удри“ во препрека или во некој друг атом (атомот секогаш застанува на првото поле што е соседно на препрека или на друг атом во соодветната насока).

Не е возможно ротирање на атомите (линковите на атомите секогаш ќе бидат поставени како што се на почетокот на играта). Исто така, не е дозволено атомите да излегуваат од таблата.

Целта на играта е атомите да се доведат во позиција во која ја формираат „молекулата“ прикажана десно од таблата. Играта завршува во моментот кога трите атоми ќе бидат поставени во бараната позиција, во произволни три соседни полиња од таблата.

Потребно е проблемот да се реши во најмал број на потези.

За сите тест примери изгледот и големината на таблата се исти како на примерот даден на сликата. За сите тест примери положбите на препреките се исти. За секој тест пример се менуваат почетните позиции на сите три атоми, соодветно. Во рамки на почетниот код даден за задачата се вчитуваат влезните аргументи за секој тест пример.

Движењата на атомите потребно е да ги именувате на следниот начин:

RightX - за придвижување на атомот X надесно (X може да биде H1, O или H2)
LeftX - за придвижување на атомот X налево (X може да биде H1, O или H2)
UpX - за придвижување на атомот X нагоре (X може да биде H1, O или H2)
DownX - за придвижување на атомот X надолу (X може да биде H1, O или H2)
Вашиот код треба да има само еден повик на функција за приказ на стандарден излез (print) со кој ќе ја вратите секвенцата на движења која треба да се направи за да може атомите од почетната позиција да се доведат до бараната позиција.

Треба да примените неинформирано пребарување. Врз основа на тест примерите треба самите да определите кое пребарување ќе го користите.
"""


def move_right(x1, y1, x2, y2, x3, y3, obstacles):
    while (x1 < 8 and (x1 + 1, y1) != (x2, y2) and (x1 + 1, y1) != (x3, y3)
           and [x1 + 1, y1] not in obstacles):
        x1 += 1
    return x1


def move_left(x1, y1, x2, y2, x3, y3, obstacles):
    while (x1 > 0 and (x1 - 1, y1) != (x2, y2) and (x1 - 1, y1) != (x3, y3)
           and [x1 - 1, y1] not in obstacles):
        x1 -= 1
    return x1


def move_up(x1, y1, x2, y2, x3, y3, obstacles):
    while (y1 < 8 and (x1, y1 + 1) != (x2, y2) and (x1, y1 + 1) != (x3, y3)
           and [x1, y1 + 1] not in obstacles):
        y1 += 1
    return y1


def move_down(x1, y1, x2, y2, x3, y3, obstacles):
    while (y1 > 0 and (x1, y1 - 1) != (x2, y2) and (x1, y1 - 1) != (x3, y3)
           and [x1, y1 - 1] not in obstacles):
        y1 -= 1
    return y1


class Molecule(Problem):
    def __init__(self, obstacles, initial, goal=None):
        super().__init__(initial, goal)
        self.obstacles = obstacles

    def successor(self, state):
        """За дадена состојба, врати речник од парови {акција : состојба}
        достапни од оваа состојба. Ако има многу следбеници, употребете
        итератор кој би ги генерирал следбениците еден по еден, наместо да
        ги генерирате сите одеднаш.

        :param state: дадена состојба
        :return:  речник од парови {акција : состојба} достапни од оваа
                  состојба
        :rtype: dict
        """
        successors = dict()

        h1x, h1y = state[0], state[1]
        o1x, o1y = state[2], state[3]
        h2x, h2y = state[4], state[5]

        # H1
        for direction, move_func in [('RightH1', move_right), ('LeftH1', move_left), ('UpH1', move_up),
                                     ('DownH1', move_down)]:
            new_pos = move_func(h1x, h1y, o1x, o1y, h2x, h2y, self.obstacles)
            if new_pos != (h1x if 'H' in direction else h1y):
                successors[direction] = (
                new_pos if 'H' in direction else h1x, new_pos if 'H' not in direction else h1y, o1x, o1y, h2x, h2y)

        # H2
        for direction, move_func in [('RightH2', move_right), ('LeftH2', move_left), ('UpH2', move_up),
                                     ('DownH2', move_down)]:
            new_pos = move_func(h2x, h2y, o1x, o1y, h1x, h1y, self.obstacles)
            if new_pos != (h2x if 'H' in direction else h2y):
                successors[direction] = (
                h1x, h1y, o1x, o1y, new_pos if 'H' in direction else h2x, new_pos if 'H' not in direction else h2y)

        # O
        for direction, move_func in [('RightO', move_right), ('LeftO', move_left), ('UpO', move_up),
                                     ('DownO', move_down)]:
            new_pos = move_func(o1x, o1y, h1x, h1y, h2x, h2y, self.obstacles)
            if new_pos != (o1x if 'O' in direction else o1y):
                successors[direction] = (
                h1x, h1y, new_pos if 'O' in direction else o1x, new_pos if 'O' not in direction else o1y, h2x, h2y)

        return successors

    def actions(self, state):
        """За дадена состојба state, врати листа од сите акции што може да
        се применат над таа состојба

        :param state: дадена состојба
        :return: листа на акции
        :rtype: list
        """
        return self.successor(state).keys()

    def result(self, state, action):
        """За дадена состојба state и акција action, врати ја состојбата
        што се добива со примена на акцијата над состојбата

        :param state: дадена состојба
        :param action: дадена акција
        :return: резултантна состојба
        """
        return self.successor(state)[action]

    def goal_test(self, state):
        """Врати True ако state е целна состојба. Даденава имплементација
        на методот директно ја споредува state со self.goal, како што е
        специфицирана во конструкторот. Имплементирајте го овој метод ако
        проверката со една целна состојба self.goal не е доволна.

        :param state: дадена состојба
        :return: дали дадената состојба е целна состојба
        :rtype: bool
        """
        # H1 O H2
        return state[1] == state[3] == state[5] and state[0] + 1 == state[2] and state[2] + 1 == state[4]


if __name__ == '__main__':
    obstacles_list = [[0, 1], [1, 1], [1, 3], [2, 5], [3, 1], [3, 6], [4, 2],
                      [5, 6], [6, 1], [6, 2], [6, 3], [7, 3], [7, 6], [8, 5]]
    initial = (2, 1, 2, 6, 7, 2)
    problem = Molecule(obstacles_list, initial)

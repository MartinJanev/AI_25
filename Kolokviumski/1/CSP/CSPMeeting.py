# from constraint import *
#
# if __name__ == '__main__':
#     problem = Problem(BacktrackingSolver())
#     simona_free_time = [13, 14, 16, 19]
#     marija_free_time = [14, 15, 18]
#     petar_free_time = [12, 13, 16, 17, 18, 19]
#
#     # ---Dadeni se promenlivite, dodadete gi domenite-----
#     problem.addVariable("Marija_prisustvo", [0, 1])
#     problem.addVariable("Simona_prisustvo", [1])
#     problem.addVariable("Petar_prisustvo", [0, 1])
#     problem.addVariable("vreme_sostanok", [i for i in range(12, 21)])
#
#     variables = ["Simona_prisustvo", "Marija_prisustvo", "Petar_prisustvo", "vreme_sostanok"]
#
#
#     # ----------------------------------------------------
#
#     def valid_meeting(s, m, p, time):
#         if (time not in simona_free_time) or (time not in petar_free_time and time not in marija_free_time):
#             return False
#
#         if ((time in petar_free_time and p == 1) or (time not in petar_free_time and p == 0)) and \
#                 ((time in marija_free_time and m == 1) or (time not in marija_free_time and m == 0)):
#             return True
#         return False
#
#
#     problem.addConstraint(valid_meeting, variables)
#
#     # ----------------------------------------------------
#
#     [print(solution) for solution in problem.getSolutions()]


from constraint import *

if __name__ == '__main__':
    problem = Problem(BacktrackingSolver())

    simona_free = [13, 14, 16, 19]
    marija_free = [14, 15, 18]
    petar_free = [12, 13, 16, 17, 18, 19]

    # ---Dadeni se promenlivite, dodadete gi domenite-----
    problem.addVariable("Marija_prisustvo", [0, 1])
    problem.addVariable("Simona_prisustvo", [1])
    problem.addVariable("Petar_prisustvo", [0, 1])
    problem.addVariable("vreme_sostanok", [i for i in range(12, 21)])
    # ----------------------------------------------------

    variables = ["Simona_prisustvo", "Marija_prisustvo", "Petar_prisustvo", "vreme_sostanok"]


    # ---Tuka dodadete gi ogranichuvanjata----------------

    def isValid(s, m, p, time):
        if time not in simona_free:
            return False

        if time not in petar_free and time not in marija_free:
            return False

        if (time in petar_free and p == 1) or (time in marija_free and m == 1):
            if (time not in petar_free and p == 0) or (time not in marija_free and m == 0):
                return True
        return False


    problem.addConstraint(isValid, variables)

    # ----------------------------------------------------

    [print(solution) for solution in problem.getSolutions()]

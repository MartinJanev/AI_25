import os

from setuptools.command.build_ext import if_dl

os.environ["OPENBLAS_NUM_THREADS"] = "1"

students = {}


def getGrade(points):
    if 0<= points <= 50:
        return 5
    elif 51 <= points <= 60:
        return 6
    elif 61 <= points <= 70:
        return 7
    elif 71 <= points <= 80:
        return 8
    elif 81 <= points <= 90:
        return 9
    else:
        return 10



if __name__ == "__main__":
    while True:
        row = input()
        if row == "end":
            break
        name, surname, index, subject, theory, practical, labs = row.split(",")
        total_points = int(theory) + int(practical) + int(labs)

        if index not in students:
            students[index] = {
                "name": name,
                "surname": surname,
                "subjects": {}
            }
        students[index]["subjects"][subject] = getGrade(total_points)

    for index, student in students.items():
        print(f"Student: {student['name']} {student['surname']}")
        for subject, grade in student['subjects'].items():
            print(f"----{subject}: {grade}")
        print()

# import os
# import somefile as f1
# from somefile import *
# from somefile1 import functionality112 as f1

# cesto koristeni
# sys,os,os.path,math,random,datetime,calendar,shutil,subprocess,socket,threading,logging,urllib,json,re


# f1.functionality1()
# functionality1()


print()
a = 3
b = ''

# if elif else namesto switch

c = True if b == 0 else False
# print(c)
#
# x = 0
# while x < 10:
#     if x % 2 != 0:
#         continue
#     print("Even number")
#     x = x +1

str1 = 'string'
# for s in str1:
#     print(ord(s))

arr2 = [1, 2, 3, 4, 5, 6]

arr3 = []

for v1, v2 in zip(str1, arr2):
    arr3.append([v1, v2])

# for i in range(10,100,15):
#     print(i)

# for i in range(len(arr3)):
#     print(arr3[i])


ages = {
    'Martin': 20,
    'Todor': 30,
    'Ivan': 40,
    'Petar': 50
}

# for key, value in ages.items():
#     print(key, value)
# print()
# for k in ages.keys():
#     print(k)

# for v in ages.values():
#     print(v)

for k in ages:
    pass  # za koimplementacija

assert 1 == 1, "Error"  # ako e true nema da se isprinta nisto, ako e false ke se isprinta error

# List comprehension

squares = []
for i in range(1, 11):
    squares.append(i * i)
# print(squares)

# list comprehension
squares = [i * i for i in range(1, 11)]


# print(squares)


def subtract(a, b):
    return a - b


razliki = [subtract(i, 3) for i in range(1, 11)]
# print(razliki)

# filter

novi_razliki = [subtract(i, 2) for i in range(1, 11) if i % 2 == 0]
# print([i for i in range(1, 11)])
print(novi_razliki)

print([el * 2 if el % 2 == 0 else el for el in range(1, 11)])

majmuni = ['majmun', 'gorila', 'orangutan']

nested = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

flatten = [val for elem in nested for val in elem]

print(flatten)

# ==========

vkupno = 0


def zbir(x, y):
    # ako sakame promena
    # global vkupno

    vkupno = x + y
    print(vkupno)
    return vkupno


zbir(3, 4)
print("Nadvor od funkcijata: ", vkupno)


# ==========

# OOP


class Student:
    """Klasa za studenti"""

    def __init__(self, name, age):  # konstruktor
        self.name = name
        self.age = age

    def get_age(self):  # metoda za dobivanje na godini
        return self.age


studenti = []
studenti.append(Student('Martin', 20))
studenti.append(Student('Todor', 30))

g = [name for name in studenti]


# for i in g:
# print(i.name)


# podatoni i klasni atributi

class Teacher:
    """Klasa za profesori"""

    # klasni atributi
    school = 'Semos'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_age(self):
        return self.age


class Scientist(Teacher):
    def __init__(self, name, age, field):
        super().__init__(name, age)
        self.field = field

    def get_field(self):
        return self.field

    def get_age(self):
        Teacher.__class__.get_age(self)


class Sample:
    x = 23
    __y = 34

    def __init__(self, y):
        self.y = y

    def increment(self):
        self.__class__.x += 1

    def get_y(self):
        return self.__y


met = Sample(3)
# print(met.get_y())

print()


class FibNum:
    def __init__(self):
        self.a = 1
        self.b = 1

    def __next__(self):
        (self.a, self.b, oldb) = (self.b, self.a + self.b, self.b)

    def __iter__(self):
        return self


# f = FibNum()
# for i in f:
#     print(i)
#     if i > 100:
#         break

# Itertools

from itertools import *

# chain - spoi dve lista vo edna

print(list(chain([1, 2, 3], [4, 5, 6])))

# file management so with

# exceptions

# matrica so list comprehension
# matrica = [[0 for i in range(5)] for j in range(5)]
# print(matrica)

x = [1, 2, 3, 4, 5, 6, 6, 7]

y = "Wolrd" + "Hello"

for i in x:
    print(i)

print(y.split("o"))

l = """a`b"c"""
print(l.format())

# mutable and non-mutable types

# mutable - i can change the value of the variable
# non-mutable - i can't change the value of the variable


# tuples
t = ((1, 2, 3, 44, 2.2), ("Java", "Python", "Ruby"), ("John", "Doe", "Smith"))
print()
print(t[1][2])
print()
# list

l = [1, 2, 3, 4.5, "Java", [1, 23, 4.5, {"name": "John"}, (2, "Ho")], {"name": "John"}, "sadam", 1, 2]

print(l[-1])
print(l[1:-4])

# dictionary

d = {"name": "John", "age": 25, "city": "New York"}

# prekopiranje na nova adresa

a = [1, 2, 3]
b = a[:]

print(a + a)
print(a * 3)

a[0] = 100
print(a)

# radi nemutabilnost na tuples, moze da se heshira i da se koristi kako kluc vo dictionary
a.insert(0, 100)
a.append([1, 2, 3])
a.extend([1, 2, 3])

print(a)

di = {"name": "John", "age": 25, "city": "New York"}


# del a["name"]
# a.clear()


def f(a, b):
    """
    :param a:
    :param b:
    :return:
    """

    print(f'a = {a}, b = {b}')
    print("Hello")


f(1, 2)

# moze vaka
zbir = f
zbir(1, 2)

# lambda

mul = lambda cc: cc * 4


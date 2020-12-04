from itertools import count
from math import factorial


def factn():
    for el in count(1):
        yield factorial(el)


x = 1
for i in factn():
    print(f'Факториал числа {x} равен {i}')
    if x == 10:
        break
    x += 1

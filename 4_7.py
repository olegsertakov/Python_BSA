from itertools import count
from math import factorial

def fact():
    for i in count(1):
        yield factorial(i)

n = int(input("Введите целое число, равное основанию факториала - "))
gener = fact()
x = 0
for i in gener:
    if x == n: break
    else:
        x += 1
        print(f'Факториал {x} = {i}')

from functools import reduce
def func(x,y):
    print("({0}, {1})".format(x, y))
    return x * y


numeral = [i for i in range(100, 1001) if i % 2 == 0]
print(numeral)
multiplication = reduce(func, numeral)
print(multiplication)

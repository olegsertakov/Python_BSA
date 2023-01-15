'''Вариант №1'''


def my_func(x, y):
    x, y = int(x), int(y)
    degree = x ** y
    return degree


n_1 = input('Введите действительное положительное число (основание) -')
n_2 = input('Введите целое отрицательное число (степень) -')
print(f'Результат = {round(my_func(n_1, n_2),4)}')


''' Вариант №2 '''


def my_func(x, y):
    x, y = int(x), abs(int(y))
    i = 1
    degree = 1
    while i <= y:
        degree *= 1 / x
        i += 1
    return degree


n_1 = input('Введите действительное положительное число (основание) -')
n_2 = input('Введите целое отрицательное число (степень) -')
print(f'Результат = {round(my_func(n_1, n_2),4)}')


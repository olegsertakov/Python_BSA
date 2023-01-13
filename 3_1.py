'''Вариант №1'''


def test_division(num_1, num_2):
    num_1, num_2 = int(num_1), int(num_2)
    if num_2 == 0:
        print('На ноль делить нельзя')
        num_2 = int(input('Введите корректный делитель-'))
    div_num = num_1 / num_2
    return round(div_num,2)


n_1 = input('Введите число (делимое) -')
n_2 = input('Введите число (делитель) -')
print(f'Частное равно = {test_division(n_1, n_2)}')


''' Вариант №2 '''


def test_division(num_1, num_2):
    try:
        num_1, num_2 = int(num_1), int(num_2)
        div_num = num_1 / num_2
    except ValueError:
        return ('Некорректные данные')
    except ZeroDivisionError:
        return ('Деление на ноль')
    return round(div_num, 2)


n_1 = input('Введите число (делимое) -')
n_2 = input('Введите число (делитель) -')
print(f'Частное равно = {test_division(n_1, n_2)}')


def my_func(arg_1, arg_2, arg_3):
    my_list = [arg_1, arg_2, arg_3]
    return sum(sorted(my_list)[1:])


num_1 = int(input('Введите первый аргумент -'))
num_2 = int(input('Введите второй аргумент -'))
num_3 = int(input('Введите третий аргумент -'))
print(f'Сумма 2-х наибольших аргументов = {my_func(num_1, num_2, num_3)}')

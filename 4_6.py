'''Выводим целые числа, начиная с N_start, а при достижении числа N_finish завершаем цикл'''
from itertools import count
print('Выводим целые числа, начиная с N_start, а при достижении числа N_finish завершаем цикл.')
print('Для выхода из итераций нажмите <q>')
N_start = int(input('Введите целое число N_start -'))
N_finish = int(input('Введите целое число N_finish -'))
for i in count(N_start, 2):
    if i > N_finish: break
    print(i, end=' ')
    next_i = input()
    if next_i == 'q': break

'''Итератор, повторяющий элементы некоторого списка, определенного заранее'''
from itertools import cycle
test_list = input('ВВедите через пробел символы списка - ').split( )
print(test_list)
print('Для запуска итераций нажимайте <Enter>')
print('Для выхода из итераций нажмите <q>')
n = 0
for el in cycle(test_list):
    quit = input()
    if quit == 'q':
        print('Цикл итераций завершен')
        break
    print(el)
    n += 1


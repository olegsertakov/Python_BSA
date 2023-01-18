''' Задаем список '''
list_test = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
list_test = [0, 222, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123]

''' или вводим целые или дробные числа '''
list_test =list(map(float, input('Введите числа через пробел и нажмите Enter:').split()))
print(list_test)
list_new = [list_test[i] for i in range(1, len(list_test)) if list_test[i] > list_test[i-1]]
print(list_new)

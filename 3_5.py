def summa():
    s = 0
    while True:
        list_sum = list(input('Введите числа или символ "Q" через пробел и нажмите Enter:').split())
        print(list_sum)
        for i in range(len(list_sum)):
         if list_sum[i] == "Q":
            return s
            break
         else:
            s += int(list_sum[i])
            print(f'текущая сумма {s}')
    return s


print('Для выхода из процедуры подсчета суммы чисел введите символ "Q" ')
print('Сумма чисел =', summa())


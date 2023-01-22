'''
Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
'''

from random import randint

with open("test_5.txt", mode='w+', encoding="utf-8") as f_num:
    f_num.write(" ".join([str(randint(1, 100)) for _ in range(100)]))
    f_num.seek(0)
    print(sum(map(int, f_num.readline().split())))


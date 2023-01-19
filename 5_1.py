'''
Создать программно файл в текстовом формате, записать в него построчно данные,
вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка
'''

test_f = open("test_file.txt", "w")
while True:
    content = input('Введите строку -')
    test_f.write(f'{content}\n')
    if not content:
        break
test_f.close()


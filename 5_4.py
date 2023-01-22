'''Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
'''
dict_rus = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}
with open("test_4new.txt", 'w', encoding="utf-8") as f_new:
    with open("test_4.txt", 'r', encoding="utf-8") as f_old:
        f_new.write(str([line.replace(line.split()[0], dict_rus.get(line.split()[0])) for line in f_old]))



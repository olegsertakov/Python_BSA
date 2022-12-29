list_1 = input('Введите элементы списка через пробел:').split()
print(f'Введенный список {list_1}')
i = 0
while i+1 < len(list_1):
    if i % 2 == 0:
       list_1.insert(i, list_1.pop(i+1))
    i = i + 1
print(f'Новый список {list_1}')


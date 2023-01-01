string_1 = input('Введите слова через пробел: ').split()
for el, word in enumerate(string_1, 1):
    print(f'{el}  {word[:10]}')


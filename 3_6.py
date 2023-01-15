""" Вариант №1 """
def int_func():
    s = input('Введите слово из маленьких латинских букв:').title()
    return s


print('Слово с прописной первой буквой ', int_func())


""" Вариант №2"""

def int_func(word):
    s = word.title()
    return s


string_long = input('Введите строку из слов латинских букв в нижнем регистре:').split()
for i in range(len(string_long)):
    string_long[i] = int_func(string_long[i])
print('Строка из слов с прописной первой буквой ', ' '.join(string_long))

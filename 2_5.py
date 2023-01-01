rating_list = [8, 8, 7, 6, 6, 6, 5, 4, 3, 2, 1]
new_element = int(input('Введите новый элемент как натуральное число от 0 до 9: '))
i = 0
for n in rating_list:
    if new_element <= n:
        i = i + 1

    elif new_element > n:
        break
rating_list.insert(i, float(new_element))
print(rating_list)

'''  Вариант №1   '''


def users_par(name, surname, birthday, city, email, phone):
    return (f'Name - {name}; Surname - {surname}; Birthday - {birthday}; City - {city};'\
    f' Email - {email};  Phone - {phone}')


name = input('Введите имя -')
surname = input('Введите фамилию -')
birthday = input('Введите день рождения -')
city = input('Введите город -')
email = input('Введите email -')
phone = input('Введите телефон -')


print(users_par(name=name, surname=surname, birthday=birthday, city=city, email=email, phone=phone))


''' Вариант №2 '''


def users_par(**kwargs):
    return "___".join(kwargs.values())


params = {
    'name': input('Введите имя -'),
    'surname': input('Введите фамилию -'),
    'birthday': input('Введите день рождения -'),
    'city': input('Введите город -'),
    'email': input('Введите email -'),
    'phone': input('Введите телефон -')
}


print(users_par(**params))

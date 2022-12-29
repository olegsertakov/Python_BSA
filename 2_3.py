while True:
    month_number = int(input('Введите номер месяца от 1 до 12 = '))
    if (month_number > 0) and (month_number <= 12):
        season_year_l = ['зима', 'весна', 'лето', 'осень', 'зима']
        season_year_d = {0: 'зима', 1: 'весна', 2: 'лето', 3: 'осень', 4: 'зима'}
        print(f'Список сезонов - {season_year_l[month_number//3]}\nСловарь сезонов - {season_year_d[month_number//3]}')
        break
    else:
        print('Ошибка ввода')


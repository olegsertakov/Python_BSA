from sys import argv

def salary():
    try:
        time, rate, bonus = map(float, argv[1:])
        salary = time * rate + bonus
        print(f'Заработная плата - {salary}')
    except ValueError:
        print('Введите значения Времени, Ставки и Бонуса ')


salary()

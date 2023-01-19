'''
Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
'''

with open("test_3.txt", 'r', encoding="utf-8") as f_salary:
    dict_salary = {line.split()[0]: float(line.split()[1]) for line in f_salary}
    sum = 0.0
    salary_threshold = float(input('Введите пороговое значение зарплаты - '))
    print(f"Зарплату меньше {salary_threshold} получают:")
    for el in dict_salary.items():
        if el[1] < salary_threshold:
           print(f'{el[0]} - {el[1]}')
        sum += el[1]

    print(f'Средняя зарплата = {round((sum / len(dict_salary)), 2)}')

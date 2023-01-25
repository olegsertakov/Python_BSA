"""
Реализовать базовый класс Worker (работник), в котором определить атрибуты:
name, surname, position (должность), income (доход). Последний атрибут должен быть защищенным и ссылаться на
словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
Создать класс Position (должность) на базе класса Worker. В классе Position реализовать методы получения
полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные,
проверить значения атрибутов, вызвать методы экземпляров).
"""

'''
Предлагаю в качестве базового класса взять класс Position (должность), т.к. в организации существует
штатное расписание, где каждой должности соответствует оклад и премия.
А каждый работник (Worker) со своим именем и фамилией принимается на должность. 
'''
class Position:
    def __init__(self, position, wage, bonus):
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}

    def get_total_income(self):
        return (sum(self._income.values()))

class Worker(Position):

    def get_full_name(self, worker_name, worker_surname):
        self.name = worker_name
        self.surname = worker_surname
        print(f'Полное имя сотрудника {self.name} {self.surname}')

manager = Worker('sale-manager', 100000, 50000)
name = input('Введите имя сотрудника ')
surname = input('Введите фамилию сотрудника ')
print(manager.get_full_name(name, surname))
print(manager.position)
print(f'Полный доход {manager.get_total_income()}')




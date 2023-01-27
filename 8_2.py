'''
Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем
нуля в качестве делителя программа должна корректно обработать эту ситуацию и
не завершиться с ошибкой.
'''

class DivisionByZero:
    def __init__(self, dividend, divider):
        self.dividend = dividend
        self.divider = divider

    @staticmethod
    def division_by_zero(dividend, divider):
        try:
            return (dividend / divider)
        except:
            return (f"Делить на ноль недопустимо")

div = DivisionByZero(12, 60)
print(DivisionByZero.division_by_zero(15, 0))
print(DivisionByZero.division_by_zero(10, 0.0001))
print(div.division_by_zero(50, 0))

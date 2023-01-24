'''
Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет)
 и метод running (запуск). Атрибут реализовать как приватный. В рамках метода реализовать
переключение светофора в режимы: красный, желтый, зеленый. Продолжительность первого состояния
(красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) — 11.
Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
 Проверить работу примера, создав экземпляр и вызвав описанный метод.
'''

import random

class TrafficLight:
    # приватный атрибут класса
    __TrafficLight_color = 'str'

    # метод класса
    def running(self, time):
        print(time)
        if time <= 7:
            self.__TrafficLight_color = 'red'
        elif time > 7 and time <= 9:
            self.__TrafficLight_color = 'yellow'
        else:
            self.__TrafficLight_color = 'green'
        return (self.__TrafficLight_color)

# экземпляр класса
a_1 = TrafficLight()
print(a_1.running(random.randint(1, 20)))

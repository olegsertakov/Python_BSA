'''
 Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name,
is_police (булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала,
остановилась, повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
'''

class Car:
    # атрибуты класса
    def __init__(self, name, color, speed, is_police=False):
        self.car_name = name
        self.car_color = color
        self.car_speed = speed
        self.car_is_police = is_police
        print(f'Марка машины: {self.car_name}  Цвет: {self.car_color}  Скорость: {self.car_speed}')

    # методы класса
    def car_go(self):
        print(f"{self.car_name}: Машина движется")

    def car_stop(self):
        print(f"{self.car_name}: Машина остановилась")

    def turn(self, direction):
        print(f"{self.car_name}: Машина повернула {'налево' if direction <= 0 else 'направо'}")

    def show_speed(self):
        print(f"{self.car_name}: Скорость автомобиля - {self.car_speed }")

class TownCar(Car):
    def show_speed(self):
        print(f"{self.car_name}: Скорость автомобиля - \
        {self.car_speed if self.car_speed <= 60 else 'Скорость превышена'}")

class SportCar(Car):
    "Спортивный автомобиль"

class WorkCar(Car):
    def show_speed(self):
        print(f"{self.car_name}: Скорость автомобиля - \
        {self.car_speed if self.car_speed <= 40 else 'Скорость превышена'}")

class PoliceCar(Car):
    def __init__(self, name, color, speed, is_police=True):

        super(). __init__(name, color, speed, is_police=True)

car_TownCar = TownCar("Снегоуборщик", 'оранжевый', 70)
print(car_TownCar.show_speed())

car_PoliceCar = PoliceCar("ДПС", 'белый', 90)
print(car_PoliceCar.car_go())

car_SportCar = SportCar("Форд GT", 'оранжевый', 170 )
print(car_SportCar.turn(-1))

tractor = WorkCar("Кировец", 'синий', 50)
print(tractor.car_stop())

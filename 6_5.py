'''
 Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название)
 и метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка),
 Pencil (карандаш), Handle (маркер). В каждом из классов реализовать переопределение метода draw.
 Для каждого из классов методы должен выводить уникальное сообщение.
 Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
'''

# класс Stationery
class Stationery:
    def __init__(self, title="Название канцелярского инструмента"):
        self.title = title
    def draw(self):
        print(f"Запуск отрисовки. {self.title}")


# класс Pen, наследующий Stationery
class Pen(Stationery):
    def draw(self):
        print(f"Запуск отрисовки ручкой. {self.title}")


# класс Pencil, наследующий Stationery
class Pencil(Stationery):
    def draw(self):
        print(f"Запуск отрисовки карандашом. {self.title}")


# класс Handle, наследующий Stationery
class Handle(Stationery):
    def draw(self):
        print(f"Запуск отрисовки маркером. {self.title}")


stat = Stationery()
stat.draw()
pen = Pen()
pen.draw()
pencil = Pencil()
pencil.draw()


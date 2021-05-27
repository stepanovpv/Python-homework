# 5. Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и
# метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка),
# Pencil (карандаш), Handle (маркер). В каждом из классов реализовать переопределение метода draw. Для каждого
# из классов метод должен выводить уникальное сообщение. Создать экземпляры классов и проверить, что выведет
# описанный метод для каждого экземпляра.

class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        f'Запуск отрисовки.'


class Pen(Stationery):
    def draw(self):
        return f'Пишет в блокноте - {self.title}'


class Pencil(Stationery):
    def draw(self):
        return f'Пишет в альбоме - {self.title}'


class Handle(Stationery):
    def draw(self):
        return f'Пишет на чем угодно - {self.title}'


title1 = Stationery
pen = Pen("Ручка")
pencil = Pencil("Карандаш")
handle = Handle("Маркер")

print(pen.draw())
print(pencil.draw())
print(handle.draw())

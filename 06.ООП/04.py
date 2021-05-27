# 4.Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police
# (булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась,
# повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый
# класс метод show_speed, который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar
# переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение
# о превышении скорости. Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам,
# выведите результат. Выполните вызов методов и также покажите результат.

class Car:
    speed: int
    color: str
    name: str
    is_police: bool = False

    def __init__(self, name, speed, color, is_police=False):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = is_police

    def go(self):
        return f'Автомобиль {self.name} поехал.'

    def stop(self):
        return f'\nАвтомобиль {self.name} остановился.'

    def turn(self, direction):
        return f'\nАвтомобиль {self.name} повернул {direction}'

    def show_speed(self):
        return f'\nСкорость {self.name} = {self.speed} км/ч'


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return f'\nПревышение скорости! Скорость составляет {self.speed} км/ч.'
        else:
            return f'\nСкорость нормальная'


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return f'\nYПревышение скорости! Скорость составляет {self.speed} км/ч.'
        else:
            return f'\nСкорость нормальная'


class PoliceCar(Car):
    is_police: bool = True


town = TownCar('Жигули', 70, 'Чёрный', False)
print('\n' + town.go(), town.show_speed(), town.turn('налево'), town.turn('направо'), town.stop())

sport = SportCar('Лада 2109', 170, 'Красный', False)
print('\n' + sport.go(), sport.show_speed(), sport.turn('налево'), sport.stop())

work = WorkCar('Газель', 30, 'Серый', False)
print('\n' + work.go(), work.show_speed(), work.turn('направо'), work.stop())

police = PoliceCar('УАЗ', 100, 'Бело-синий', True)
print('\n' + police.go(), police.show_speed(), police.turn('направо'), police.stop())




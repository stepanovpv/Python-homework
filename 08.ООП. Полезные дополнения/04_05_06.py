# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
# который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
# уникальные для каждого типа оргтехники.
# 5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу в
# определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники, а также
# других данных, можно использовать любую подходящую структуру, например словарь.
# 6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных. Например,
# для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей, изученных
# на уроках по ООП.

class OfficeEquipmentWarehouse:
    print("Склад оргтехники")


class OfficeEquipment:
    def __init__(self, producer, color):
        self.producer = producer
        self.color = color


class Printer(OfficeEquipment):
    amount_pr = 0

    def __init__(self, producer, color, pr_type):
        super().__init__(producer, color)
        self.pr_type = pr_type
        Printer.amount_pr += 1

    @staticmethod
    def name():
        return "Принтер: "

    def type_printer(self):
        return self.pr_type

    def __str__(self):
        return "\tПроизводитель: {} \tЦвет: {}  \tТип принтера: {}".format(self.producer, self.color, self.pr_type)


class Scanner(OfficeEquipment):
    amount_sc = 0

    def __init__(self, producer, color, sc_sensor):
        super().__init__(producer, color)
        self.sc_sensor = sc_sensor
        Scanner.amount_sc += 1

    @staticmethod
    def name():
        return"Сканер: "

    def type_sensor(self):
        return self.sc_sensor

    def __str__(self):
        return "\tПроизводитель: {} \tЦвет: {} \tТип сенсора: {}".format(self.producer, self.color, self.sc_sensor)


class Xerox(OfficeEquipment):
    amount_x = 0

    def __init__(self, producer, color, xer_wi_fi):
        super().__init__(producer, color)
        self.xer_wi_fi = xer_wi_fi
        Xerox.amount_x += 1

    @staticmethod
    def name():
        return "Ксерокс: "

    def wi_fi_module(self):
        return self.xer_wi_fi

    def __str__(self):
        return "\tПроизводитель: {} \tцвет: {} \tWi-Fi модуль: {}".format(self.producer, self.color, self.xer_wi_fi)


p = Printer('Kyocera', 'Белый', 'струйный')
p2 = Printer('Brother', 'СИний', 'лазерный')
print(p.name(), p.amount_pr, "шт")
print(p.__str__())
print(p2.__str__())


s = Scanner('Epson', 'Белый', 'CIS')
s2 = Scanner('Avision', 'Белый', 'CCD')
s3 = Scanner('Kodak', 'Желтый', 'CMOS')
print(s.name(), s.amount_sc, "шт")
print(s.__str__())
print(s2.__str__())
print(s3.__str__())


x = Xerox('Hanp', 'Белый', 'есть')
x2 = Xerox('Phaser', 'Чёрный', 'есть')
x3 = Xerox('Xerox', 'Белый', 'есть')
x4 = Xerox('Pantum', 'Красный', 'отсутствует')
print(x.name(), x.amount_x, "шт")
print(x.__str__())
print(x2.__str__())
print(x3.__str__())
print(x4.__str__())
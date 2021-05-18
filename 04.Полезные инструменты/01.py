# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах*ставка в час) + премия. Для выполнения
# расчета для конкретных значений необходимо запускать скрипт с параметрами.

def salary(hours, value, bonus):
    """
    Функция расчета заработной платы сотрудника
    :param hours: Часты работы
    :param value: Ставка в час
    :param bonus: Премия
    :return: Вывод заработной платы
    """
    try:
        sal = (int(hours) * int(value)) + int(bonus)
        print(f"Заработная плата сотрудника: {sal}")
    except ValueError:
        return print("Вы должны задать целое число, попробуйте еще раз")

# Здесь идет задание параметров при запуске (в терминале или PyCharm в Edit Configuration).

import sys
name, hours, value, bonus = sys.argv
salary(hours, value, bonus)

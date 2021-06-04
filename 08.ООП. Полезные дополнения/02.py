# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных,
# вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту
# ситуацию и не завершиться с ошибкой.

class NullDiv(Exception):

    def division_func(self, numer, denom):
        try:
            result = round(numer / denom, 2)
        except ZeroDivisionError:
            print(f"На ноль делить нельзя!")
        else:
            print(f"{numer} / {denom} = {result} \n")


numer = int(input("Введите числитель: "))
denom = int(input("Введите знаменатель: "))
result = NullDiv()
result.division_func(numer, denom)

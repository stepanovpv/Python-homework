# 1. Поработайте с переменными, создайте несколько, выведите на экран, запросите у пользователя несколько чисел и строк и сохраните в переменные, выведите на экран.

a = int(10)
b = float(4.6)
c = str("Текстовая переменная")

print("Переменная а - это целое число: ", a)
print("Переменная b - это дробное число: ", b)
print("Переменная c - это текст: ", c)

d = int(input("Введите целое число: "))
e = float(input("Введите дробное число: "))
f = str(input("Введите текст: "))

print(d, "- это цельночисленная переменная, введенная пользователем")
print(e, "- это дробная переменная, введенная пользователем")
print(f, "- это текстовая переменная, введенная пользователем")

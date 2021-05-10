# 4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе. Для решения используйте цикл while и арифметические операции.

number = int(input("Введите целое положительное число: "))
max_num = 0

while number and max_num != 9:
    print(number)
    current = number % 10  # Остаток от деления, потом проверяем это число
    number = number // 10  # Новое число без последнего разряда
    if current > max_num:
        max_num = current
    else:
        max_num = max_num

print("Самая большая цифра в цисле: ", max_num)

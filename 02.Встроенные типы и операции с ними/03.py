# 3. Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года относится месяц (зима,
# весна, лето, осень). Напишите решения через list и через dict.

month = int(input("Введите месяц в виде целого числа: "))
print("Решение через list:\n")

times_list = ["Зима", "Весна", "Лето", "Осень"]

if month == 1 or month == 2 or month == 12:
    print(f"Время года - {times_list[0]}\n")
elif month == 3 or month == 4 or month == 5:
    print(f"Время года - {times_list[1]}\n")
elif month == 6 or month == 7 or month == 8:
    print(f"Время года - {times_list[2]}\n")
elif month == 9 or month == 10 or month == 11:
    print(f"Время года - {times_list[3]}\n")
else:
    print("Нет такого месяца")

print("Решение через dict:\n")

times_dict = {"Зима": (12, 1, 2), "Весна": (3, 4, 5), "Лето": (6, 7, 8),"Осень": (9, 10, 11)}

for season, months in times_dict.items():
    if month in months:
        print(f"Время года - {season}")
        break

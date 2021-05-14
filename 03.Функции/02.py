# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год
# рождения, город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

def user(name, surname, year, city, email, phone):
    """
    Функция принимает параметры от пользователя, а затем выводит их
    :param name: Имя
    :param surname: Фамилия
    :param year: Год
    :param city: Город
    :param email: Почта
    :param phone: Телефон
    :return: Вывод
    """
    return print(
        f"Имя: {name}, Фамилия: {surname}, Год рождения: {year}, Город: {city}, Почта: {email}, Телефон{phone}")

name = str(input("Введите имя: "))
surname = str(input("Введите фамилию: "))
year = int(input("Введите год рождения: "))
city = str(input("Введите город: "))
email = str(input("Введите email: "))
phone = int(input("Введите номер телефона: "))

print("")
user(name=name, surname=surname, year=year, city=city, email=email, phone=phone)

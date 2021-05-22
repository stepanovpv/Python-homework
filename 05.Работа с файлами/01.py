# 1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

import os

if os.path.exists('01.txt'):
    os.remove('01.txt')

strings = []

while True:
    with open('01.txt', 'a+') as file:
        string = input("Введите данные: ")
        file.write(string + '\n')
        if not string:
            break
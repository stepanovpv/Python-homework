# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
#
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные. При этом английские
# числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.

import  os

translations = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}

ru_rows = []

with open("04_1.txt") as input:
    for row in input:
        name, value = row.split(' - ')
        ru_rows.append(f"{translations[name]} - {value}")

if os.path.exists('04_2.txt'):
    os.remove('04_2.txt')

with open("04_2.txt", "w", encoding='utf_8') as output:
    output.writelines(ru_rows)

print("Коневертация завершена")

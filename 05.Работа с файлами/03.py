# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов
# (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.
# Пример файла:
#
# Иванов 23543.12
# Петров 13749.32

with open('03.txt', encoding='utf_8') as file:
    rows = file.readlines()
    poor = []
    mid_salary = []
    count = 0

    for line in rows:
        rows_lines = rows[count].split()
        count += 1
        mid_salary.append(rows_lines[1])
        if int(rows_lines[1]) < 20000:
            poor.append(rows_lines[0])

    print("Сотрудники с зарплатой менее 20000:", *poor)
    print(f"Средняя заработная плата: {(sum(map(int, mid_salary))) / len(mid_salary)}")

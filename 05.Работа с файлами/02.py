# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
# количества слов в каждой строке.

with open('02.txt', encoding='utf_8') as file:
    rows = file.readlines()
    count = 0
    print(f"Количество строк: {len(rows)}")

    for line in rows:
        rows_lines = rows[count].split()
        print(f"Количество слов в {count + 1}-й строке: {len(rows_lines)}")
        count += 1

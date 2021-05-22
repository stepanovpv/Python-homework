# 7. Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка должна содержать данные
# о фирме: название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
#
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма
# получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
#
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
#
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

import json

data = []

with open('07.txt', encoding='utf_8') as input:
    dict = {}
    profit_list = []

    for company_row in input:
        name, form, revenue, costs = company_row.split()

        profit = float(revenue) - float(costs)
        dict[name] = profit

        if profit:
            profit_list.append(profit)

    data.append(dict)
    data.append({"Average profit": round(sum(profit_list) / len(profit_list), 2)})

with open('07.json', 'w') as output:
    json.dump(data, output)

print("Программа упешно завершена, создан файл 07.json")
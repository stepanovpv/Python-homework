# 6. *Реализовать структуру данных «Товары». Она должна представлять собой список кортежей. Каждый кортеж хранит
# информацию об отдельном товаре. В кортеже должно быть два элемента — номер товара и словарь с параметрами
# (характеристиками товара: название, цена, количество, единица измерения). Структуру нужно сформировать программно,
# т.е. запрашивать все данные у пользователя.
# Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика товара,
# например название, а значение — список значений-характеристик, например список названий товаров.

goods = []
features = {'Наименование': '', 'Цена': '', 'Количество': '', 'Ед.Измерения': ''}
analytics = {'Наименование': [], 'Цена': [], 'Количество': [], 'Ед.Измерения': []}
num = 0
feature_ = None
control = None
while True:
    control = input(" Для выхода нажмите 'Q'\n Для продолжения нажмите 'Enter'\n для анализа нажмите 'A'").upper()
    if control == 'Q':
        break
    num += 1
    if control == 'A':
        print(f'\n Текущая аналитика \n {"-" * 30}')
        for key, value in analytics.items():
            print(f'{key[:25]:>30}: {value}')
            print("-" * 30)
    for f in features.keys():
        feature_ = input(f"Введите {f}: ")
        features[f] = int(feature_) if (f == "Цена" or f == "Количество") else feature_
        analytics[f].append(features[f])
    goods.append((num, features))
# 5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга. Если в рейтинге существуют элементы с одинаковыми
# значениями, то новый элемент с тем же значением должен разместиться после них.

exist_rating = [7, 5, 3, 3, 2]

while True:
    try:
        print(f"Существующий рейтинг - : {exist_rating}")
        user_rating = int(input("Введите новую оценку: "))
        exist_rating.append(user_rating)
        exist_rating.sort(reverse=True)
        print(f"Новый рейтинг - : {exist_rating}\n")
    except ValueError:
        print("Неверное число")
    except KeyboardInterrupt:
        exit()


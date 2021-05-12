# 2. Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы с индексами
# 0 и 1, 2 и 3 и т.д. При нечетном количестве элементов последний сохранить на своем месте. Для заполнения списка
# элементов необходимо использовать функцию input().

elements = input("Введите несколько значений. Разделитель - пробел: ").split()
final = []
idx = 1

while idx < len(elements):
    final.append(elements[idx])
    final.append(elements[idx - 1])
    idx += 2

# last_element = len(elements) // 2

if (len(elements) % 2) == 0:
    print(*final)
else:
    final.append(elements[-1])
    print(*final)




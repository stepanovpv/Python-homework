# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами. Программа
# должна подсчитывать сумму чисел в файле и выводить ее на экран.

with open("05.txt", "w+") as input:
    input.write(" ".join(map(str, [x for x in range(1, 30, 2)])))

with open('05.txt') as output:
    numbers = output.read().split()

print("Числа в файле:", *numbers)
print(f"Сумма числе в файле: {sum(int(x) for x in numbers)}")

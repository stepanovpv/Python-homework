# 6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же, но с
# прописной первой буквой. Например, print(int_func(‘text’)) -> Text.

# Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом. Каждое слово
# состоит из латинских букв в нижнем регистре. Сделать вывод исходной строки, но каждое слово должно начинаться с
# заглавной буквы. Необходимо использовать написанную ранее функцию int_func().

def int_func(*args):
    """
    Функция выводит введенные слова с заглавной буквы
    :param args: Принимает любое количество позиционных аргументов
    :return: Выводит слова с заглавной буквы
    """
    phrase = input("Введите несколько слов маленькими буквами: ")
    return print(phrase.title())

int_func()
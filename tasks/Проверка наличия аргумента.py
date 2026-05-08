import sys

try:
    argument_1 = sys.argv[1]
    print(f"Аргумент получен: {argument_1}")
except IndexError:
    print("Ошибка: Вы не ввели аргумент")
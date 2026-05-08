import sys

try:
    arg_1 = int(sys.argv[1])

    print(f"Аргумент преобразован в число: {arg_1}")
except ValueError, IndexError:
    print("Ошибка: Не удалось преобразовать аргумент в число")
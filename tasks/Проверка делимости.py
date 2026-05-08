import sys

try:
    arg_1 = int(sys.argv[1])
    arg_2 = int(sys.argv[2])

    if arg_1 % arg_2 == 0:
        print("Первое число делится на второе без остатка")
    else:
        print(f"Остаток: {int(arg_1 % arg_2)}")
except ValueError, IndexError:
    print("Ошибка: Должно быть числа, пример: python main.py 10 2")
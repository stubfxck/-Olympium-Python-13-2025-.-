import sys

try:
    arg_1 = int(sys.argv[1])
    arg_2 = int(sys.argv[2])

    if arg_1 < arg_2:
        print("Диапазон между числами:")
        for i in range(arg_1, arg_2+1):
            print(i)
    else:
        print("Первый аргумент должен быть меньше второго.")
except ValueError:
    print("Ошибка: Оба аргумента должны быть числовыми")
except IndexError:
    print("Ошибка: Должно быть 2 аргумента")
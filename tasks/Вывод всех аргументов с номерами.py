import sys

try:
    args = sys.argv[1:]

    if args:
        for num, argument in enumerate(args, 1):
            print(f"{num}.", argument)
    else:
        raise IndexError
except IndexError:
    print("Ошибка: Введите хотя бы 1 аргумент")
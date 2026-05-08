import sys

args = sys.argv[1:]

if args:
    print(f"Количество аргументов: {len(args)}")
else:
    print("Введите хотя бы 1 аргумент")

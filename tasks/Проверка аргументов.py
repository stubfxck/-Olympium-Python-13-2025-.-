import sys

args = len(sys.argv) - 1
if int(args) > 2:
    print(f"Количество аргументов: {args}")
else:
    print(f"Введите больше двух аргументов, сейчас их: {args}")
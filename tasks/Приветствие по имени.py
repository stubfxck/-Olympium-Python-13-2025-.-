import sys

try:
    name = sys.argv[1]
    print(f"Здравствуйте, {name}!")
except IndexError:
    print("Ошибка: Укажите имя. Пример: python main.py Дмитрий")
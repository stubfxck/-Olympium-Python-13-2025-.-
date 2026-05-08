import sys

try:
    input_name = sys.argv[1]
    input_age = sys.argv[2]

    print(f" - Имя: {input_name}\n - Возраст: {input_age}")
except IndexError:
    print("Вы не указали имя и возраст. Пример: python main.py Дмитрий 19")
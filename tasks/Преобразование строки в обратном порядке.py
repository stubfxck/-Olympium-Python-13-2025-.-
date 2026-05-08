import sys

try:
    input_string = sys.argv[1][::-1]

    print(input_string)
except IndexError:
    print("Ошибка: Введите фразу, пример: python main.py \"Длинная фраза\"")
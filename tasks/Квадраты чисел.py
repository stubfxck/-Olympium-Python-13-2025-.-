import sys

program_args = sys.argv[1:]

try:
    for num in program_args:
        print(int(num) ** 2)
except ValueError:
    print("Ошибка! Объект не является числом. Программа завершилась с ошибкой, проверьте ввод.")
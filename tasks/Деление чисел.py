import sys

try:
    input_num1 = int(sys.argv[1])
    input_num2 = int(sys.argv[2])

    if input_num2 != 0:
        print(f"Результат: {int(input_num1 / input_num2)}")
    else:
        print("Деление на ноль запрещено.")
except IndexError, ValueError:
    print("Вы не указали один из аргументов, или ввели некорректные данные. \n Пример: python main.py 10 2")
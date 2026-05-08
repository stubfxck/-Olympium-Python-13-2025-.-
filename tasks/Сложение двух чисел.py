import sys

try:
    num1 = int(sys.argv[1])
    num2 = int(sys.argv[2])
    print(f"Результат: {num1 + num2}")
except IndexError:
    print("Введите числа. Пример: python main.py 2 3")
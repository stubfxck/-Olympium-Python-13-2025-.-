import sys

try:
    user_input = sys.argv[1]

    print(f"Результат:", user_input.upper())
except IndexError:
    print("Пожалуйста, введите значение. Пример: python upper.py привет")
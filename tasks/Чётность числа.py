import sys

try:
    input_number = int(sys.argv[1])

    if input_number % 2 == 0:
        print("Число чётное")
    else:
        print("Число не чётное")
except ValueError, IndexError:
    print("Убедитесь в корректности ввода. Пример: python main.py 5")
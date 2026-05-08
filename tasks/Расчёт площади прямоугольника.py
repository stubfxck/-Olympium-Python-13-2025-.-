import sys

try:
    input_width = int(sys.argv[1])
    input_height = int(sys.argv[2])

    print(f"Площать прямоугольника: {input_width * input_height}")
except ValueError, IndexError:
    print("Проверьте правильность введенных данных. Пример: python main.py 5 4")
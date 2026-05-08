import sys

try:
    input_phrase = sys.argv[1]
    input_count = int(sys.argv[2])

    for i in range(0, input_count):
        print(input_phrase)
except ValueError, IndexError:
    print("Проверьте корректность ввода. Пример: python main.py <Фраза> <Кол-во повторений>")
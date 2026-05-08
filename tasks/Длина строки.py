import sys

try:
    input_string = sys.argv[1]

    print(f"Символов в строке: {len(input_string)}")
except IndexError:
    print("Пожалуйста, введите строку. Пример: 'Слово слово'")
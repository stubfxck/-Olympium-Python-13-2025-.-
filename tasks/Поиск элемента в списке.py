import sys

program_args = sys.argv[1:]

user_input = input("Введите искомое слово: ")

if user_input in program_args:
    print("Аргумент найден")
else:
    print("Аргумент не найден")
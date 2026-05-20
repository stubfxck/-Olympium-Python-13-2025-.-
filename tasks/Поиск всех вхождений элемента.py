import sys

program_args = sys.argv[1:]

user_input = input("Введите слово: ")

for arg in program_args:
    if arg == user_input:
        print("Индекс введенного элемента:", program_args.index(arg))

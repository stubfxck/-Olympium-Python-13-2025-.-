import sys

program_args = sys.argv[1:]

user_input = input("Введите букву: ")

result = [word for word in program_args if word.startswith(user_input)]

print(", ".join(result))
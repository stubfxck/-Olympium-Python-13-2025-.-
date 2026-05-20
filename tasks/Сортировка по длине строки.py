import sys

user_input = sys.argv[1:]
user_input.sort(key=len)

print("Сортировка по длинне:", ", ".join(user_input))
import sys

user_input = sys.argv[1:]

user_input.sort(key=lambda x: x[-1])

print(user_input)
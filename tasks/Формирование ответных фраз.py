import sys

program_args = sys.argv[1:]

str_list = [f"Привет, {name}!" for name in program_args]

for elem in str_list:
    print(elem)
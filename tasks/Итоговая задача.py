import sys

program_args = sys.argv[1:]

result = [int(num) for num in program_args if int(num) > 3]

print(sorted(result, reverse=True))
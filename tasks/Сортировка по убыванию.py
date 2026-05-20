import sys

input_nums = sys.argv[1:]

if input_nums:
    print(" ".join(sorted(input_nums, reverse=True)))
else:
    print("Введите хотя бы несколько чисел")
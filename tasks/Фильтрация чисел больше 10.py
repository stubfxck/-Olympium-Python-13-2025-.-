import sys

try:
    input_nums = sys.argv[1:]

    if input_nums:
        for num in input_nums:
            if int(num) > 10:
                print(num)
    else:
        raise IndexError
except ValueError:
    print("Ошибка: Убедитесь что все значения - числа")
except IndexError:
    print("Ошибка: Убедитесь что вы ввели хотя бы 1 аргумент")
import sys

result_list = []

try:
    nums_list = sys.argv[1:]

    if nums_list:
        for num in nums_list:
            if int(num) % 2 == 0:
                result_list.append(num)
        
        print(" ".join(result_list))
    else:
        raise IndexError
except IndexError:
    print("Ошибка: Проверьте ввод, должен быть хотя бы 1 аргумент")
except ValueError:
    print("Ошибка: Все аргументы должны быть числами")
import sys

example = "Пример: python main.py 5 / 10"

try:
    num_1 = int(sys.argv[1])
    arg = sys.argv[2]
    num_2 = int(sys.argv[3])

    match arg:
        case "+": result = num_1 + num_2
        case "-": result = num_1 - num_2
        case "*": result = num_1 * num_2
        case "/": 
            if num_2 != 0:
                result = num_1 / num_2
            else:
                raise ValueError
        case _: raise ValueError
    
    print(f"Результат: {result}")
except ValueError:
    print("Ошибка: Проверьте правильность итератора или введенных чисел.", example)
except IndexError:
    print("Ошибка: Убедитесь что вы ввели все три значения корректно.", example)
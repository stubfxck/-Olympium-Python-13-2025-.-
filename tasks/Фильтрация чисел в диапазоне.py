data = [1, 5, 10, 15, 20, 25]

start = int(input("Введите начало диапазона: "))
end = int(input("Введите конец диапазона: "))

print("Числа попадающие в диапазон: ")
for num in data:
    if start < num < end:
        print(num)
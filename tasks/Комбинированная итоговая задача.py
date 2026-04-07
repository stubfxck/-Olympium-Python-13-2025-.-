userinp = input("Введите список чисел через пробел (например: 5 2 9 1 7 3): ")
userinp = userinp.split()

for num in userinp:
    if int(num) < 3:
        userinp.pop(userinp.index(num))

userinp.sort(reverse=True)

print(userinp)
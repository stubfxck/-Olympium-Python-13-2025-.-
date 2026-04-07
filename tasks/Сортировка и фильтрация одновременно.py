data = [3, 7, 2, 8, 5, 9]

for item in data:
    if item < 4:
        data.remove(item)

data.sort(reverse=True)
print(f"Результат: {', '.join(map(str, data))}")
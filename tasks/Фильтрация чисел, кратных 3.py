nums = [3, 6, 9, 12, 15, 18, 20]

result = []

for num in nums:
    if num % 3 == 0:
        result.append(str(num))

print(f"Результат: {', '.join(result)}")
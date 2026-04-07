spisok = [12, 25, 37, 41, 53]

pairs = []
for num in spisok:
    last = num % 10
    pairs.append((last, num))

pairs.sort()

result = []
for pair in pairs:
    result.append(pair[1])

print(result)
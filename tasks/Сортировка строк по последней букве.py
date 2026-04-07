data = ["дом", "окно", "стол", "лист"]

for i in range(len(data)):
    data[i] = data[i][::-1]

data.sort()

for i in range(len(data)):
    data[i] = data[i][::-1]

print(data)
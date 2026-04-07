data = ["кот", "собака", "попугай", "слон"]
result_data = []

for item in data:
    if len(item) > 4:
        result_data.append(item)

print(result_data)
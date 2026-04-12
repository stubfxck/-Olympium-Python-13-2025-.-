result = []

with open("data.txt", "r", encoding="utf-8") as data_txt:
    for row in data_txt:
        if "файл" in row.lower():
            result.append(row)

with open("output.txt", "w", encoding="utf-8") as output_txt:
    output_txt.writelines(result)

# with open("output.txt", "r", encoding="utf-8") as output_txt:
#     print(output_txt.read())
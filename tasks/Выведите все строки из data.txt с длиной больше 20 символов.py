
with open("data.txt", "r", encoding="utf-8") as data_txt:
    data = data_txt.readlines()
    for row in data:
        if len(row) >= 20:
            print(row)
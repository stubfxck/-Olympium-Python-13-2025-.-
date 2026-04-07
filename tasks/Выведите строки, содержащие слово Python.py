with open("data.txt", "w", encoding="utf-8-sig") as data:
    print("Текст\nЕще текст\nЯ люблю python\nPytton is name of guild owner\n Python - высокоуровневый язык", file=data)

with open("data.txt", "r", encoding="utf-8-sig") as data:
    import re
    data_text = data.readlines()
    for data in data_text:
        if re.findall("Python", data, re.I):
            print(data.strip())
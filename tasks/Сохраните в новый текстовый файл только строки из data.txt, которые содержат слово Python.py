with open("python_lines.txt", "w", encoding="utf-8") as python_lines_txt:
    with open("data.txt", "r", encoding="utf-8") as data_txt:
        data = data_txt.readlines()
        for line in data:
            if "python" in line.lower():
                print(line, file=python_lines_txt)
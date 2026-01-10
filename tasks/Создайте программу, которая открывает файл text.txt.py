with open("text.txt", "r", encoding="utf-8-sig") as text_file:

    text_file = text_file.readlines()

    for line in text_file:
        line = line.split()

        for word in line:
            if word == "Python":
                print(" ".join(line))
                break
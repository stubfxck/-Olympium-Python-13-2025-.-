import re

with open("people.txt", "w", encoding="utf-8-sig") as people:
    print("Анна пошла в Школу. там она встретила Олега и катю.", file=people)

with open("people.txt", "r", encoding="utf-8-sig") as people:
    wordlist = people.read()
    final = re.findall(r"[А-Я]\w*", wordlist)
    for i in final:
        print(i)
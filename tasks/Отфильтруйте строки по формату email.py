import re

with open("list.txt", "w", encoding="utf-8-sig") as listfile:
    print("""contact@example.com
неверный email  
user@mail.ru  
hello world  
support@domain.org""", file=listfile)
    
with open("list.txt", "r", encoding="utf-8-sig") as listfile:

    pattern = r"^\w+[\.\w+]*@\w+\.\w+$"

    listfile = listfile.readlines()

    for line in listfile:
        line = line.strip()

        if re.match(pattern, line):
            print(line)
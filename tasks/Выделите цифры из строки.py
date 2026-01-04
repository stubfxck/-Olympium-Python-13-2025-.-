import re

userinput = input("Введите строку: ")

pattern = r"[0-9]"

matches = re.findall(pattern, userinput)
print(matches)
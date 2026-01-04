import re 

userinput = input("Введите строку: ")
pattern = r"\w{3,}"

matches = re.findall(pattern, userinput)
print("Найденные слова:", ' '.join(matches))
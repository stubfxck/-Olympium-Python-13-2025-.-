import re

with open("log.txt", "w", encoding="utf-8-sig") as logfile:
    print("""Информация: процесс завершён  
ОШИБКА: не найден файл  
Успешно  
Ошибка доступа""", file=logfile)
    
with open("log.txt", "r", encoding="utf-8-sig") as logfile:
    for line in logfile.readlines():
        if re.search("Ошибка", line, re.IGNORECASE):
            print(line, end="")
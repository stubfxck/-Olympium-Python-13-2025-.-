import re

passportinput = input("Введите паспорт в формате XXXX XXXXXX (серия номер):\n > ")

passportpattern = r"\d{4} \d{6}$"

if re.match(passportpattern, passportinput):
    print("Паспорт корректен")
else:
    print("Неверный формат")
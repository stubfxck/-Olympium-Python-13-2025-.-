import re

number = input("Введите номер телефона: ")
pattern = r"\+7\-\d{3}\-\d{3}-\d{2}-\d{2}"
if re.fullmatch(pattern, number):
    print("Номер корректен")
else:
    print("Ошибка формата")
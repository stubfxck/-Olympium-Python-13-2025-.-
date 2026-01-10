import re

date_pattern = r"\d{2}\.\d{2}\.\d{4}"

user_input = input("Введите данные: ")

dates = re.findall(date_pattern, user_input)

print(f"Найденные даты: {", ".join(dates)}")

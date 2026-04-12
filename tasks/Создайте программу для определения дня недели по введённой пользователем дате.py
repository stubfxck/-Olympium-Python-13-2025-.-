from datetime import datetime, date
import re

current_date = date.today()

user_input = input("Введите дату в формате ДД.ММ.ГГГГ: ")

date_pattern = r"\d{2}.\d{2}.\d{4}"

weekdays = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]

if re.fullmatch(date_pattern, user_input):
    date_object = datetime.strptime(user_input, "%d.%m.%Y")
    print(f"Введенная дата это {weekdays[date_object.weekday()]}")
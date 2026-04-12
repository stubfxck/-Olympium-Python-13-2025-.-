from datetime import datetime

today = datetime.now().weekday()
week_names = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]

print(f"Сегодня: {week_names[today]}")
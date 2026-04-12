from datetime import datetime

today = datetime.now().weekday()
week_names = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]

print("Даты начиная с текущей:")
for i in range(7):
    day_index = (today + i) % 7
    print(week_names[int(day_index)])
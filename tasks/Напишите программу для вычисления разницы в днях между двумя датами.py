from datetime import date

current_date = date.today()

target_date = date(2025, 1, 1)

result = (current_date - target_date).days

print(f"Прошло дней: {result}")
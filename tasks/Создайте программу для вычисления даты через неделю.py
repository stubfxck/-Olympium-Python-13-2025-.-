from datetime import date, timedelta

future_date = date.today() + timedelta(days=7)

print(f"Дата через 7 дней: {future_date.strftime('%d.%m.%Y')}")
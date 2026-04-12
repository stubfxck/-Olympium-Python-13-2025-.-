from datetime import date, timedelta

date_ago = date.today() - timedelta(days=30)

print(f"Дата 30 дней назад: {date_ago.strftime('%d.%m.%Y')}")
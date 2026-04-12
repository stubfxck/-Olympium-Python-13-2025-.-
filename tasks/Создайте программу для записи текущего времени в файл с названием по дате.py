from datetime import datetime

today = datetime.now()

file_name = "log_" + today.strftime('%d%m%Y') + ".txt"

with open(file_name, "w", encoding="utf-8") as log_file:
    print(today.strftime("%H:%M:%S"), file=log_file)
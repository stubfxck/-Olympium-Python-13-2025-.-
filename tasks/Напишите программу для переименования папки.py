import os

if os.path.exists("data"):
    os.rename("data", "data_backup")
    print("Готово")
else:
    print("Папки data не существует")
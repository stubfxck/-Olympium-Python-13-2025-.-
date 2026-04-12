import os

if os.path.exists("delete_me.txt"):
    os.remove("delete_me.txt")
    print("Файл удален")
else:
    print("Файла не существует")
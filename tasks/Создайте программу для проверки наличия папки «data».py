import os

# os.mkdir("data")

if os.path.exists("data"):
    print("Папка найдена")
else:
    print("Папка не найдена")
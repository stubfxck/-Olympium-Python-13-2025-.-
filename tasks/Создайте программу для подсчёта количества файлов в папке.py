import os

files_count = 0

for file in os.listdir('.'):
    if os.path.isfile(file):
        files_count += 1

print(f"Кол-во файлов в текущей папке: {files_count}")
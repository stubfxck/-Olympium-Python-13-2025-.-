import os

files_list = []

for item in os.listdir('.'):
    if item.endswith(".py"):
        files_list.append(item)

print(files_list)
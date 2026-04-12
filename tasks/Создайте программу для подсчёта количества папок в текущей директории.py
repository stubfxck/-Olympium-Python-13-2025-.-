import os 

folders_count = 0

for file in os.listdir('.'):
    if os.path.isdir(file):
        folders_count+=1

print(f"Кол-во папок: {folders_count}")
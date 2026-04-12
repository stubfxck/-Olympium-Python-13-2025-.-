import os

dir_list = []

for item in os.listdir('.'):
    if os.path.isdir(item):
        dir_list.append(item)


print(dir_list)
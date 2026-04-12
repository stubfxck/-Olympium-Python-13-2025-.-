# Сначала не понял задание и подумал что нужно вытащить с каждого .txt файла первые строки и записать их в 1 файл, оставил код мало ли скажут "Вот какой крутой ученик"

# import os

# strings = []

# for file in os.listdir('.'):
#     if file.endswith(".txt"):
#         with open(file, "r", encoding="utf-8") as file_opened:
#             readfilelines = file_opened.readlines()
#             strings.append(readfilelines[0])

# with open("txt_files.txt", "w", encoding="utf-8") as txt_files_txt:
#     for line in strings:
#         print(line, file=txt_files_txt)

import os

with open("txt_files.txt", "w", encoding="utf-8") as txt_files_txt:

    for file in os.listdir('.'):
        if file.endswith(".txt"):
            print(file, file=txt_files_txt)
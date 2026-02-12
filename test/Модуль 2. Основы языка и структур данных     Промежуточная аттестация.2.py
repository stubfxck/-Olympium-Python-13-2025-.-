
# Напишите код, который создаёт файл "output.txt" и записывает в него строку "Hello, file!"

with open("file.txt", "w") as file:
    print("Hello, file!", file=file)
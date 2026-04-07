# Пример содержания: 
#
# with open ("students.csv", "w", encoding="utf-8") as file:
#     print("Строка1 очень длинная строка с бессмысленным текстом\nА вот вторая строка с таким же бессмысленным текстом", file=file)

with open ("students.csv", "r", encoding="utf-8") as file:
    data = file.readlines()
    for num, string in enumerate(data, 1):
        print(f"Строка {num}:", string.split())
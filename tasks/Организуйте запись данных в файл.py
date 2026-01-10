
string_list = []

for i in range(3):
    user_string = input(f"Введите строку {i+1}: ")
    string_list.append(user_string)

with open("text.txt", "w", encoding="utf-8-sig") as listfile:
    for line in string_list:
        print(line, file=listfile)
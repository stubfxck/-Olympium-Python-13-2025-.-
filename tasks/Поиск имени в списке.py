db = ["Анна", "Борис", "Виктор", "Галина"]

input_name = input("Введите имя: ")

for name in db:

    if name == input_name:
        print("Имя найдено")
        break
    
    else:    
        print("Имя не найдено")
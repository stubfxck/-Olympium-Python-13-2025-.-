import json
import re

patterns = {
    "name": (r"^[А-ЯЁ][а-яё]+ [А-ЯЁ][а-яё]+ [А-ЯЁ][а-яё]+$", "ФИО (Фамилия Имя Отчество)"),
    "phone": (r"^(?:\+7|7|8)\d{10}$", "номер (79998887766)"),
    "email": (r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", "email (example@gmail.com)"),
    "date": (r"^\d{2}\.\d{2}\.\d{4}$", "дату (дд.мм.гггг)")
}

def isbase():
    try:
        with open("db.json", "r", encoding="utf-8-sig") as dbfile:
            db = json.load(dbfile)
            return bool(db)
    except (FileNotFoundError, json.JSONDecodeError):
        db = {}
        print("База данных пуста.")
        return False

def getinput(field, change):
    pattern, description = patterns[field]
    while True:
        user_input = input(f"Введите {description}: ")
        if re.match(pattern, user_input):
            if field == "phone":
                user_input = re.sub(r"^(?:\+7|8)", "7", user_input)
            return user_input
        elif user_input == "" and change:
            return "None"
        else:
            print(f"Некорректный ввод. Пожалуйста, введите правильную {description}.")

def db_create():

    name = getinput("name", False)
    phone = getinput("phone", False)
    email = getinput("email", False)
    date = getinput("date", False)

    record = {phone: {
            "name": name,
            "email": email,
            "date": date
        }
    }
    db = {}

    if isbase():
        with open("db.json", "r", encoding="utf-8-sig") as dbfile:
            db = json.load(dbfile)
            if phone in db:
                print("Запись с таким номером уже существует!")
                return

            for rec in db.values():
                if rec["email"] == email:
                    print("Запись с таким email уже существует!")
                    return
    
    with open("db.json", "w", encoding="utf-8-sig") as dbfile:
        db[phone] = record[phone]
        json.dump(db, dbfile, ensure_ascii=False, indent=4)
        print("Запись успешно создана!")

def db_view():
    if isbase():
        while True:
            mode = input("  Просмотреть все: 1\n  Поиск по данным: 2\n  Назад: 3\n > ")
            match mode:
                case "1":
                    with open("db.json", "r", encoding="utf-8-sig") as dbfile:
                        db = json.load(dbfile)
                        if not db:
                            print("База данных пуста.")
                            input("Нажмите Enter для продолжения...")
                            return
                        for phone, info in db.items():
                            print(f"Телефон: {phone}")
                            for key, value in info.items():
                                print(f"  {key.capitalize()}: {value}")
                            print("-" * 20)
                            input("Нажмите Enter для продолжения...")
                case "2":
                    with open("db.json", "r", encoding="utf-8-sig") as dbfile:
                        db = json.load(dbfile)
                        search_field = input("Введите ваш запрос:\n > ").strip()
                        if re.match(patterns["phone"][0], search_field):
                            key = search_field
                            key = re.sub(r"^(?:\+7|8)", "7", key)
                            if key in db:
                                print(f"Телефон: {key}")
                                for k, v in db[key].items():
                                    print(f"  {k.capitalize()}: {v}")
                            else:
                                print("Запись не найдена.")
                        else:
                            for phone, info in db.items():
                                if (search_field.lower() in info["name"].lower() or
                                    search_field.lower() in info["email"].lower() or
                                    search_field in info["date"]):
                                    print(f"Телефон: {phone}")
                                    for k, v in info.items():
                                        print(f"  {k.capitalize()}: {v}")
                                    print("-" * 20)
                    input("Нажмите Enter для продолжения...")
                case "3":
                    break
                case _:
                    print("Выбран неверный пункт меню.")

def db_edit():
    if isbase():
        editphone = getinput("phone", False)
        with open("db.json", "r", encoding="utf-8-sig") as dbfile:
            db = json.load(dbfile)
            if editphone not in db:
                print("Запись с таким номером не найдена.")
                return
            
            print("Введите новые данные (оставьте пустым для пропуска):")

            name = getinput("name", True)
            if name != "None":
                db[editphone]["name"] = name

            email = getinput("email", True)
            if email != "None":
                db[editphone]["email"] = email

            date = getinput("date", True)
            if date != "None":
                db[editphone]["date"] = date

        with open("db.json", "w", encoding="utf-8-sig") as dbfile:
            json.dump(db, dbfile, ensure_ascii=False, indent=4)
            print("Запись успешно обновлена!")

def db_delete():
    deletephone = getinput("phone", False)

    if isbase():
        with open("db.json", "r", encoding="utf-8-sig") as dbfile:

            db = json.load(dbfile)
            if deletephone not in db:
                print("Запись с таким номером не найдена.")
                return
            
            confirm = input(f"Вы уверены, что хотите удалить запись с номером {deletephone}? (y/n): ")

            if confirm.lower() != 'y':
                print("Удаление отменено.")
                return
            
            del db[deletephone]

        with open("db.json", "w", encoding="utf-8-sig") as dbfile:
            json.dump(db, dbfile, ensure_ascii=False, indent=4)
            print("Запись успешно удалена!")

def choice_menu(choice):
    match choice:
        case "1":
            db_create()
            input("Нажмите Enter для продолжения...")
        case "2":
            db_view()
            input("Нажмите Enter для продолжения...")
        case "3":
            db_edit()
            input("Нажмите Enter для продолжения...")
        case "4":
            db_delete()
            input("Нажмите Enter для продолжения...")
        case _:
            print("Выбран неверный пункт меню.")

while True:
    print("""
Добро пожаловать в редактор базы данных!

Выберите действие:
          1. Создать запись
          2. Просмотреть записи
          3. Отредактировать запись
          4. Удалить запись
          5. Выйти""")
    choice = input("\n > ")
    if choice == "5":
        break
    choice_menu(choice)
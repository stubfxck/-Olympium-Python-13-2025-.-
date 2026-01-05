import re

# Проект представляет собой удобный поисковик по базам данных.

def search_database(path, request):
    with open(path, "r", encoding="utf-8-sig") as dbfile:
        database = dbfile.readlines()
        results = []
        for entry in database:
            if re.search(request, entry, re.IGNORECASE):
                results.append(entry.strip())
        return results


path = input("Введите имя файла бд в формате txt (файл должен быть в той же папке что и программа):\n> ")

request = input("Введите поисковый запрос (Например фамилию или номер телефона):\n> ")

print("Результаты поиска:\n" + "\n".join(search_database(path, request)))

# Пример использования:
# Если в файле db.txt есть строки:
# Иванов Иван Иванович, +79991234567
# Петров Петр Петрович, +79876543210
# Запрос "Иванов" вернет:
# Иванов Иван Иванович, +79991234567 
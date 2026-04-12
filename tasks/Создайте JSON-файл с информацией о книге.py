import json

with open("book.json", "w", encoding="utf-8") as book_json:
    data = {
        "title": "Название книги",
        "author": "Автор книги",
        "year": "Год издания"
    }
    json.dump(data, book_json, ensure_ascii=False, indent=4)
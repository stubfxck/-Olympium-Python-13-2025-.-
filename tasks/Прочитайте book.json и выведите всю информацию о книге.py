import json

with open("book.json", "r", encoding="utf-8") as book_json:
    data = json.load(book_json)
    print(f"Название: {data['title']}, Автор: {data['author']}, Год издания: {data['year']}")
import re

with open("event.txt", "w", encoding="utf-8-sig") as eventfile:
    print("Мероприятие 01.06.2024, следующее 05.07.2024", file=eventfile)

with open("event.txt", "r", encoding="utf-8-sig") as eventfile:
    pattern = r"\d{2}\.\d{2}\.\d{4}"
    content = eventfile.read()
    finishcontent = re.sub(pattern, "ДАТА", content)
    print(finishcontent)

with open("event.txt", "w", encoding="utf-8-sig") as eventfile:
    print(finishcontent, file=eventfile)
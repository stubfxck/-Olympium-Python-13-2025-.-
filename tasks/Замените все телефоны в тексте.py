import re

with open("phones.txt", "w", encoding="utf-8-sig") as phonesfile:
    print("Позвоните +7-111-222-33-44 или +7-999-888-77-66.", "Этот номер +7-000-000-00-00 больше не используется.", sep="\n", file=phonesfile)

with open("phones.txt", "r", encoding="utf-8-sig") as phonesfile:
    phonesfile = phonesfile.read()
    pattern = r"\+7\-\d{3}\-\d{3}-\d{2}-\d{2}"
    finaltext = re.sub(pattern, "Скрыто", phonesfile)
    print(finaltext)
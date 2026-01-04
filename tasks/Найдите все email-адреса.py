import re

with open("emails.txt", "w", encoding="utf-8-sig") as emails:
    print("info@example.com", "user123@mail.ru", "текст без email", "test.email@domain.org", sep="\n", file=emails)

with open("emails.txt", "r", encoding="utf-8-sig") as emails:
    pattern = r"^\w+[\.\w+]*@\w+\.\w+$"
    for mail in emails:
        mail = mail.strip()
        if re.fullmatch(pattern, mail): 
            print(mail)
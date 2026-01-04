import re

with open("mails.txt", "w", encoding="utf-8-sig") as mailsfile:
    mailsfile.write("""user1@site.com
admin@domain.ru
hello@mail.org""")
    
with open("mails.txt", "r", encoding="utf-8-sig") as mailsfile:
    pattern = r".+@"
    mails = mailsfile.read().split()
    for mail in mails:
        clearly = re.sub(pattern, "", mail)
        print(clearly)
import re

with open("page.txt", "w", encoding="utf-8-sig") as pagefile:
    print("""<h1>Заголовок</h1>
<p>Текст</p>""", file=pagefile)
    

with open("page.txt", "r", encoding="utf-8-sig") as pagefile:
    pattern = r"<.+?>"
    pagefile_content = pagefile.read()
    result = re.sub(pattern, "", pagefile_content)
    print(result)
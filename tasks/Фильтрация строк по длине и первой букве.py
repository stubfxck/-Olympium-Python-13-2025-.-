spisok = ["Арбуз", "Ананас", "Яблоко", "Абрикос"]
result = []

for word in spisok:
    if word[0] == "А" and len(word) > 5:
        result.append(word)

print(result)
userinp = input("Введите предложение: ")
finallist = []
userinp = userinp.split()

for word in userinp:
    if word[0] == word[-1]:
        finallist.append(word)
print(finallist)
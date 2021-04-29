dic = {}
fff = 1
while 1:
    acommad = input("Add or look up a word (a/l)")
    if acommad == "a":
        word = input("Type the word:")
        ming = input("Type the definition:")
        dic[word] = ming  # dic = {word:ming}
        print("Word added!")
    if acommad == "l":
        look = input("Type the word:")
        if look in list(dic.keys()):
            print(dic[look])
        else:
            print("That word isn't in the dictionary yet.")
    elif acommad == "q":
        break

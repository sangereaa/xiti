a = int(input("Which multiplication table would you like?"))
print("Here is your table:")
for i in range(1, 11):
    b = i * a
    print(a, "X", i, "=", b)

a = int(input("Which multiplication table would you like?"))
print("Here is your table:")
b = 1
while b <= 10:
    c = b * a
    print(a, "X", b, "=", c)
    b += 1

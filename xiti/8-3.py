a = int(input("Which multiplication table would you like?"))
b = int(input("How high do you want to go?"))
c = 1
print("Here is your table:")
while c <= b:
    d = c * a
    print(a, "X", c, "=", d)
    c += 1

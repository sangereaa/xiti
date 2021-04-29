print("please enter 5 names")
names = []
for i in range(5):
    names.append(input())
names_ = names[:]
names_.sort()
print("The names are", names, "\n", names_)

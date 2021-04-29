print("please enter 5 names")
names = []
for i in range(5):
    names.append(input())
j = int(input("Replace one name. Which one? (1-5):")) - 1
k = input("New name:")
names[j] = k
print("The names are", names)

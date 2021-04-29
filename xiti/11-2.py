import time
a = int(input("when do you want"))
for i in range(a, 0, -1):
    print(i, end="")
    print("*"*i)
    time.sleep(1)

print("BLAST OFF!")

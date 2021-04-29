a = int(input("油箱有多大（单位是升）？"))
b = float(input("现在油箱有多满（按百分比算，例如半满就是50%）？"))
c = a*0.01*b-5
d = float(input("每升油可以走多少千米？"))
e = d * c
if e <= 200:
    print("油箱容量是：", a \n"油箱百分比：", b)

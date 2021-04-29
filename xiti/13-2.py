def mon(fen, jiao, yuan):
    total = float(fen)*0.01+float(jiao)*0.1+float(yuan)
    return total


yuan_ = input("how much yuan")
jiao_ = input("how much jiao")
fen_ = input("how much fen")
print("1 fen:", fen_)
print("1 jiao:", jiao_)
print("1 yuan", yuan_)
totalmoney = mon(fen_, jiao_, yuan_)
print("total is ¥:", totalmoney)

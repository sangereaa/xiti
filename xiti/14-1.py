class BankAccount:
    def __init__(self):
        self.zhanghuming = " "  # 字符串
        self.zhanghao = 0  # 字符串或整数
        self.yue = 0.0  # 浮点数

    def zhanghu(self, zhanghuming, zhanghao, yue):
        self.zhanghuming = zhanghuming
        self.zhanghao = zhanghao
        self.yue = global yue

    def xianshi(self, yue):
        print(yue)

    def tiqu():
        yue = yue - input("ni yao tiqu de qianshu")
        print(yue)
# class BankAccount:
# def __init__(self, acct_number, acct_name):


#self.acct_number = acct_number
#self.acct_name = acct_name
#self.balance = 0.0
# def displayBalance(self):


#print("The account balance is:", self.balance)
# def deposit(self, amount):


#self.balance = self.balance + amount
#print("You deposited", amount)
#print("The new balance is:", self.balance)
# def withdraw(self, amount):


# if self.balance >= amount:
#self.balance = self.balance - amount
#print("You withdrew", amount)
#print("The new balance is:", self.balance)
# else:
#print("You tried to withdraw", amount)
#print("The account balance is:", self.balance)
#print("Withdrawal denied. Not enough funds.")

money = float(input('please enter your money'))
print("购买金额小于或等于 10 元享 9 折优惠，购买金额大于 10 元享 8 折优惠。")
if money <= 10:
    fin_money = money * 0.9
else:
    fin_money = money * 0.8
print("你的最终钱数是:", fin_money)

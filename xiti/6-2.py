import easygui
name = easygui.enterbox("please enter your name")
adress = easygui.enterbox("please enter your adress")
city = easygui.enterbox("please enter your city")
number = easygui.enterbox("please enter your number")
infomation = name + "\n" + adress + "\n" + city + "\n" + number
easygui.msgbox(infomation, "here is your infomation")

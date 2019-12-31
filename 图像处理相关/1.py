# coding=utf8
import random
print "游戏开始！"
print "石头，剪刀，布"
# 获取用户选择
# 提示用户输入选择
your_choice=input("请输入你的选择:")
# 随机生成计算机的选择
computer_choice=random.choice(("石头","剪刀","布"))
#提示用户计算机的选择
print"电脑出了:", computer_choice
#对比用户和计算机的选择
if computer_choice=="剪刀"and your_choice=="石头":
    print "你赢了！"
elif computer_choice=="剪刀"and your_choice=="布":
    print "你输了！"
elif computer_choice=="布"and your_choice=="剪刀":
    print "你赢了！"
elif computer_choice=="布"and your_choice=="石头":
    print "你输了！"
elif computer_choice=="石头"and your_choice=="布":
    print "你赢了！"
elif computer_choice=="石头"and your_choice=="剪刀":
    print "你输了！"
else:
    print "平局"
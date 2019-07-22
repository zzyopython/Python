import random

# 从控制台输入要出的拳头 -- 石头 剪刀 布
player = int(input("请出拳（1-石头，2-剪刀，3-布）： "))

# 电脑随机出拳
computer = random.randint(1,3)


print("玩家出的是%d,电脑出的是%d" % (player,computer))

if ((player == 1 and computer == 2)
        or (player == 2 and computer == 3)
        or (player == 3 and computer == 1)):

    print("欧耶，电脑不行呀，轻松获胜！")

elif player == computer:
    print("心有灵犀呀，再来一局！")

else:
    print("电脑可以呀，我不服，决战到天明！")

'''
    猜数字：
    需求：
        1.猜的数字是系统产生，不是自己定义
            使用random随机数技术来获取随机数
        2.键盘输入
            input("提示")
        3.循环
            while条件循环
            开始，结束，自增，任务
        4.判断
            if 判断条件  elif 判断条件.......else
    范围：0~150
    猜10次！
    如果输入大了：温馨提示：大了
    如果输入小了：温馨提示：小了
    正好猜中，恭喜您，猜中，本次猜的数字为xxxx。
    起始：5000金币，每猜错一次，减去500金币，一直扣完为止。15次没猜中，系统锁定。猜中加3000。
'''
import random
# 1. 让系统产生一个随机数
num = random.randint(0,1000)
a = random.randint(0,399)
b = random.randint(0,199)
c = random.randint(0,99)
d = random.randint(601,1000)
e = random.randint(801,1000)
f = random.randint(901,1000)


money = 5000
money = int(money)
print("欢迎来到猜数字游戏（数值设定0~1000）。温馨提示：您现在持有的金币数量为：",money," 请开始您的表演(〃'▽'〃)")

i = 1
while i < 21:
    # 任务：输入数据并比对数据
    number = input("☞请输入您要猜的数：")
    number = int(number)  # "56"  -->  56

    # 判断
    if number > num:
        money = money - 500
        print("抱歉亲，猜大了！扣您 500 金币 ┭┮﹏┭┮。您现在持有的金币为：",money,"。已瞎猜",i,"次")
        if i >= 0.5 and i <= 1:
            print(      "头一次猜不中很正常嘛，加油！！ヾ(◍°∇°◍)ﾉﾞ。要不试试",a,"?")
        elif i >= 1.5 and i <= 2:
            print(      "第二次也没猜中，可恶！！(〃＞皿＜)。告诉你吧，是：",b,"!")
        elif i >= 3 and i <= 3.5:
            print(     "还没猜中，这·····o(￣ヘ￣o＃)。相信我，绝不是：",c,"!")
        elif i >= 20 and i <= 21.5:
            print("老哥答案是",num,"!")
        else:
            print(     "还猜不中，不会吧？不会吧？ヽ(*￣▽￣*)ノ")

    elif number < num:
        money = money - 500
        print("抱歉亲，猜小了！扣您 500 金币 ┭┮﹏┭┮。您现在持有的金币为：",money,"。已瞎猜",i,"次")
        if i >= 0.5 and i <= 1:
            print("头一次猜不中很正常嘛，加油！！ヾ(◍°∇°◍)ﾉﾞ。要不试试",d,"?")
        elif i >= 1.5 and i <= 2:
            print("第二次也没猜中，可恶！！(〃＞皿＜)。告诉你吧，是：",e,"!")
        elif i >= 3 and i <= 3.5:
            print(     "还没猜中，这·····o(￣ヘ￣o＃)。相信我，绝不是：",f,"!")
        elif i >= 20 and i <= 21.5:
            print("老哥答案是",num,"!")
        else:
            print("还猜不中，不会吧？不会吧？ヽ(*￣▽￣*)ノ")

    else:
        money = money + 3000
        print("恭喜猜中！(づ￣3￣)づ 3000 金币请笑纳 ヾ(◍°∇°◍)ﾉﾞ，您现在持有的金币为：",money,"本次的幸运数字是：☺",number,"☺")
        rich=""
        if money >= 8000 and money <= 8100:
            rich = "（荣誉称号:赌怪）兄弟你开挂了吗，这么准？"
        elif money >= 7400 and money <= 7500:
            rich = "（荣誉称号:榜眼二次猿）"
        elif money >= 6600 and money <= 7000:
            rich = "（荣誉称号:探花三板斧）"
        elif money >= 5500 and money <= 6500:
            rich = "（荣誉称号:赌场高手）"
        elif money >= 5000 and money <= 5400:
            rich = "（荣誉称号:玩了个寂寞）"
        elif money >= 2500 and money <= 4500:
            rich = "（荣誉称号:菜的真实）"
        elif money >= 0 and money <= 2100:
            rich = "（荣誉称号:这游戏对您来说可能有点难）"
        else:
            rich = "（荣誉称号:赔了夫人又折兵）"
        print("尝试次数：",i,rich)
        # 跳出训话
        break # 跳出循环
    i= i + 1  # 每次加1

























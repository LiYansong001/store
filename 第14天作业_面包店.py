'''
任务：实现生产销售模型
    有一个面包店，只能存储500个面包。
    有3个厨师正在做面包，每隔3秒钟做一个面包。若面包满了，停3秒再做。
    有5名顾客，来买面包。每个人手中有1000钱，每个面包2钱；如果篮子没面包，等2秒再买。
'''
import threading
import time
bread = 0
cost = 2

class Cook(threading.Thread):
    cookname = ""
    def run(self) -> None:
        global bread
        while bread < 502:
            if bread >= 0 and bread < 500:
                bread = bread + 1
                print(self.cookname,"做一面包,")
                time.sleep(3)
            elif bread == 500:
                time.sleep(3)
            else:
                break

class buyer(threading.Thread):
    money = ""
    buyername = ""
    def run(self) -> None:
        global bread
        global money
        while self.money >= -0.5:
            if bread > 0:
                bread = bread - 1
                self.money = self.money - cost
                print(self.buyername,"买了一个！")

            elif bread == 0:
                time.sleep(2)
                if self.money == 0:
                    print(self.buyername,"没钱了")
                    break
            else:
                break

class saler(threading.Thread):
    salername = ""
    def run(self) -> None:
        global bread
        while True:
            if bread > 0 or bread < 500:
                print(self.salername,"说：面包还有",bread,"个！！！")
                time.sleep(4)
                if bread >= 500:
                    print(self.salername, "说：终于凑齐", bread, "个面包！可以召唤神龙了")
                    break


c1 = Cook()
c2 = Cook()
c3 = Cook()
c1.cookname = "厨师A,"
c2.cookname = "厨师B,"
c3.cookname = "厨师C,"

b1 = buyer()
b2 = buyer()
b3 = buyer()
b4 = buyer()
b5 = buyer()
b1.buyername = "高阳,"
b2.buyername = "李进富,"
b3.buyername = "王也,"
b4.buyername = "张佳敬,"
b5.buyername = "张阔,"
b1.money = 1000
b2.money = 1000
b3.money = 1000
b4.money = 1000
b5.money = 1000

s1 = saler()
s1.salername = "售货员尤威,"

c1.start()
c2.start()
c3.start()
b1.start()
b2.start()
b3.start()
b4.start()
b5.start()
s1.start()














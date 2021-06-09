#实现输入10个数字，并打印10个数的求和结果

# a = input("输入数字a:")
# a = int(a)
# b = input("输入数字b:")
# b = int(b)
# c = input("输入数字c:")
# c = int(c)
# d = input("输入数字d:")
# d = int(d)
# e = input("输入数字e:")
# e = int(e)
# f = input("输入数字f:")
# f = int(f)
# g = input("输入数字g:")
# g = int(g)
# h = input("输入数字h:")
# h = int(h)
# i = input("输入数字i:")
# i = int(i)
# j = input("输入数字j:")
# j = int(j)
# print("十数字之和为：",a+b+c+d+e+f+g+h+i+j)


#从键盘依次输入10个数，最后打印最大的数、10个数的和、和平均数。
# a = input("输入数字a:")
# a = int(a)
# b = input("输入数字b:")
# b = int(b)
# c = input("输入数字c:")
# c = int(c)
# d = input("输入数字d:")
# d = int(d)
# e = input("输入数字e:")
# e = int(e)
# f = input("输入数字f:")
# f = int(f)
# g = input("输入数字g:")
# g = int(g)
# h = input("输入数字h:")
# h = int(h)
# i = input("输入数字i:")
# i = int(i)
# j = input("输入数字j:")
# j = int(j)
# if a > b and a > c and a > d and a > e and a > f and a > g and a > h and a > i and a > j:
#     print("十个输入的最大数字是",a)
# elif b > a and b > c and b > d and b > e and b > f and b > g and b > h and b > i and b > j:
#     print("十个输入的最大数字是",b)
# elif c > a and c > b and c > d and c > e and c > f and c > g and c > h and c > i and c > j:
#     print("十个输入的最大数字是",c)
# elif d > a and d > b and d > c and d > e and d > f and d > g and d > h and d > i and d > j:
#     print("十个输入的最大数字是",d)
# elif e > a and e > b and e > c and e > d and e > f and e > g and e > h and e > i and e > j:
#     print("十个输入的最大数字是",e)
# elif f > a and f > b and f > c and f > d and f > e and f > g and f > h and f > i and f > j:
#     print("十个输入的最大数字是",f)
# elif g > a and g > b and g > c and g > d and g > e and g > f and g > h and g > i and g > j:
#     print("十个输入的最大数字是",g)
# elif h > a and h > b and h > c and h > d and h > e and h > f and h > g and h > i and h > j:
#     print("十个输入的最大数字是",h)
# elif i > a and i > b and i > c and i > d and i > e and i > f and i > g and i > h and i > j:
#     print("十个输入的最大数字是",i)
# else:
#      print("十个输入的最大数字是", j)
# print("十数字之和为：",a+b+c+d+e+f+g+h+i+j)
# print("十数字平均数为：",(a+b+c+d+e+f+g+h+i+j)/10)


# 使用random模块，如何产生 50~150之间的数？

# import random
# a = random.randint(50,150)
# a = int(a)
# print(a)

#从键盘输入任意三边，判断是否能形成三角形，若可以，则判断形成什么三角形（结果判断：等腰，等边，直角，普通，不能形成三角形。）

# a = input("输入边长a：")
# a = int(a)
# b = input("输入边长b：")
# b = int(b)
# c = input("输入边长c：")
# c = int(c)
#
# if a == b and a == c and a + b > c and a + c > b and b + c > a and a - b < c and b - a < c and a - c < b and c - a < b and b - c < a and c - b < a:
#     print("这是等边三角形")
# elif a == b and c > b and c > a and a + b > c and a + c > b and b + c > a and a - b < c and b - a < c and a - c < b and c - a < b and b - c < a and c - b < a:
#     print("这是等腰三角形")
# elif a == b and  c < b and c < a and a + b > c and a + c > b and b + c > a and a - b < c and b - a < c and a - c < b and c - a < b and b - c < a and c - b < a:
#     print("这是等腰三角形")
# elif a == c and b > a and b > c and a + b > c and a + c > b and b + c > a and a - b < c and b - a < c and a - c < b and c - a < b and b - c < a and c - b < a:
#     print("这是等腰三角形")
# elif a == c and b < a and b < c and a + b > c and a + c > b and b + c > a and a - b < c and b - a < c and a - c < b and c - a < b and b - c < a and c - b < a:
#     print("这是等腰三角形")
# elif b == c and a > b and a > c and a + b > c and a + c > b and b + c > a and a - b < c and b - a < c and a - c < b and c - a < b and b - c < a and c - b < a:
#     print("这是等腰三角形")
# elif b == c and a < b and a < c and a + b > c and a + c > b and b + c > a and a - b < c and b - a < c and a - c < b and c - a < b and b - c < a and c - b < a:
#     print("这是等腰三角形")
# elif a*a + b*b == c*c and a + b > c and a + c > b and b + c > a and a - b < c and b - a < c and a - c < b and c - a < b and b - c < a and c - b < a:
#     print("这是直角三角形")
# elif a*a + c*c == b*b and a + b > c and a + c > b and b + c > a and a - b < c and b - a < c and a - c < b and c - a < b and b - c < a and c - b < a:
#     print("这是直角三角形")
# elif c*c + b*b == a*a and a + b > c and a + c > b and b + c > a and a - b < c and b - a < c and a - c < b and c - a < b and b - c < a and c - b < a:
#     print("这是直角三角形")
# elif a + b > c and a + c > b and b + c > a and a - b < c and b - a < c and a - c < b and c - a < b and b - c < a and c - b < a:
#     print("这是个普通三角形")
# else:
#     print("这不是三角形")


# 有以下两个数，使用+，-号实现两个数的调换。
# A=56
# B=78
# 实现效果：
# A=78
# B=56


# A=56
# B=78
# C = A + B
# C = int(C)
#
# print("A=",A)
# print("B=",B)
#
# chose = ""
# chose = input("请输入+或->>>:")
# if chose == "+":
#     print("A=", C - A)
#     print("B=", C - B)
# elif chose == "-":
#     print("A=", C - B)
#     print("B=", C - A)
# else:
#     print("输入有误")


# 实现登陆系统的三次密码输入错误锁定功能（用户名：root,密码：admin）

# i = 3
# while i > 0:
#     print("")
#     print("--------------欢迎使用本系统----------------")
#     print("")
#     id = input("请输入用户名：")
#     password = input("请输入密码：")
#     if id == "root" and password == "admin":
#         print("")
#         print("-------------登录成功！欢迎！！--------------")
#         break
#     elif id == "root" and password != "admin" and password != "":
#         i = i - 1
#         print("密码错误！输入限制：",i,"次。")
#     elif id == "" and password != "":
#         i = i - 1
#         print("用户名不能为空！请重新输入！输入限制：",i,"次。")
#     elif id =="root" and password == "" :
#         i = i - 1
#         print("密码不能为空！请重新输入！输入限制：",i,"次。")
#     elif id =="" and password == "":
#         i = i - 1
#         print("用户名和密码不能为空！请重新输入！输入限制：",i,"次。")
#     elif id != "root":
#         i = i - 1
#         print("用户名错误！输入限制：",i,"次。")
#     else:
#         i = i - 1
#         print("密码输入错误！输入限制", i, "次")


# 使用while编程实现求1~100以内的数的和！

# a = 0
# i = 0
# while i < 100 :
#     i = i + 1
#     a = i + a
# print("1~100之和:",a)

# 一只青蛙掉在井里了，井高20米，青蛙白天往上爬3米，晚上下滑2米，问第几天能出来？请编程求出。

# pa = 0
# i = 0
# up = 3
# down = 2
# day = 0
# while i < 21:
#     day = day + 1
#     pa = pa + up - down
#     i = pa + up
# print("第",day,"天,青蛙爬出井")


# 有一个列表，[“北京”,”上海”,”广东”]
# 1)	将中国所有省会城市添加到上述列表中
#
#
# 2)	广东成为第二大发达城市，将广东排在上海前面
#
#
# 3)	[36710.36,35427.10,29863.23,29667.39,27665.36,27650.45,27620.38,25369.20]这是中国GDP排名前8的城市的GDP数值，请统计前8城市的GDP总和，平均GDP。

# city = ["北京","上海","广东"]
#
# city.append("济南")
# city.append("石家庄")
# city.append("长春")
# city.append("哈尔滨")
# city.append("沈阳")
# city.append("呼和浩特")
# city.append("乌鲁木齐")
# city.append("兰州")
# city.append("银川")
# city.append("太原")
# city.append("西安")
# city.append("郑州")
# city.append("合肥")
# city.append("南京")
# city.append("杭州")
# city.append("福州")
# city.append("广州")
# city.append("南昌")
# city.append("海口")
# city.append("南宁")
# city.append("贵阳")
# city.append("长沙")
# city.append("武汉")
# city.append("成都")
# city.append("昆明")
# city.append("拉萨")
# city.append("西宁")
# city.append("天津")
# city.append("重庆")
# city.append("台北")
#
# city[1] = "广东"
# city[2] = "上海"
#
# print(city)
#
# gdp = [36710.36,35427.10,29863.23,29667.39,27665.36,27650.45,27620.38,25369.20]
#
# print("前八城市GDP总和为：",round(gdp[0]+gdp[1]+gdp[2]+gdp[3]+gdp[4]+gdp[5]+gdp[6]+gdp[7],2))
# print("前八城市GDP平均值为：",round((gdp[0]+gdp[1]+gdp[2]+gdp[3]+gdp[4]+gdp[5]+gdp[6]+gdp[7])/8,2))

# 有以下一个列表，求其中是5的倍数的和
a = [1,5,21,30,15,9,30,24]












import random

#准备数据库和开户行名称
users = {}
bank_name = "中国工商银行昌平支行"

# 银行开户逻辑
def bank_addUser(account,username,password,country,province,street,doornum):
    # 1、 看银行是否已满，满了返回3
    if len(users) > 100:
        return 3

    # 2、 用户名是否存在，若存在返回2
    if username in users.keys():
        return 2
    # 3、 正常开户，将用户信息存在数据库
    users[username] = {
        "account":account,
        "password":password,
        "country":country,
        "province":province,
        "street":street,
        "doornum":doornum,
        "money":0,
        "bank_name":bank_name
 }
    return 1

# 用户操作逻辑
def addUser():
    username = input("请输入姓名")
    password = input("请创建密码")
    country = input("请输入国籍")
    province = input("请输入省份")
    street = input("请输入所在街道")
    doornum = input("请输入门牌号")
    account = str(random.randint(10000000,99999999))
    # 架构数据传输给银行
    status = bank_addUser(account, username, password, country, province, street, doornum)

    if status == 1:
        print("开户成功！个人信息如下：")
        info = '''
——————————————————————————
姓名：%s,             
密码：%s,         
账号：%s,       
国家：%s,       
省份：%s,       
街道：%s,       
门牌：%s,       
余额：%s,       
开户行：%s,  
——————————————————————————    
'''
        print(info % (username,password,account,country,province,street,doornum,users[username]["money"],bank_name))
        fd = open('D:/list.txt','a+') # a+ :如果文件不存在就创建，如果文件存在内容后面继续追加内容
        print(info % (username, password, account, country, province, street, doornum, users[username]["money"], bank_name),file= fd)
        fd.close()

    elif status == 2:
        print("该用户已存在！")
    elif status == 3:
        print("数据库已满！")
    else:
        print("发生未知错误！")

# 用户存款逻辑
def access():
    chose1 = input("请输入姓名")
    if chose1 in users.keys():
        chose2 = input("请输入存款金额：")
        if chose2.isdigit(): #
            chose2 = int(chose2)
            users[chose1]['money'] = int(users[chose1]['money']) + chose2
            print("您的余额为：",users[chose1]['money'])
        else:
            print("输入格式错误！")
    else:
        print("账号不存在！")

# 用户取款逻辑
def takemoney():
    chose3 = input("请输入姓名")
    if chose3 in users.keys():
        chose4 = input('请输入密码：')
        if chose4 == users[chose3]['password']:
            chose5 = input("请输入取款金额：")
            if chose5.isdigit(): #
                chose5 = int(chose5)
                if int(users[chose3]['money']) - chose5 < 0:
                    print("您输入的取款额度超出余额！")
                else:
                    users[chose3]['money'] = int(users[chose3]['money']) - chose5
                    print("您的余额为：",users[chose3]['money'])
            else:
                print("输入格式错误！")
        else:
            print("密码错误！")
    else:
        print("账号不存在！")

# 用户转账逻辑
def transfermoney():
    chose8 = input("请输入姓名")
    if chose8 in users.keys():
        chose9 = input('请输入密码：')
        if chose9 == users[chose8]['password']:
            chose10 = input("请输入转账者姓名：")
            if chose10 in users.keys():
                chose11 = input("请输入转账金额：")
                if chose11.isdigit(): #
                    chose11 = int(chose11)
                    if int(users[chose8]['money']) - chose11 < 0:
                        print("您输入的取款额度超出余额！")
                    else:
                        users[chose8]['money'] = int(users[chose8]['money']) - chose11
                        users[chose10]['money'] = int(users[chose10]['money']) + chose11
                        print("转账成功，您的余额为：",users[chose8]['money'])
                else:
                    print("输入格式错误！")
            else:
                print("账号不存在！")
        else:
            print("密码错误！")
    else:
        print("账号不存在！")

# 用户查询逻辑
def check():
    chose6 = input("请输入姓名")
    if chose6 in users.keys():
        chose7 = input('请输入密码：')
        if chose7 == users[chose6]['password']:
            print("您的余额为：",users[chose6]['money'])
        else:
            print("密码错误！")
    else:
        print("账号不存在！")

# 界面
def welcome():
    print(" —————————————————————————————")
    print("丨", "\t","\t","中国工商银行", "\t","\t","丨")
    print("丨", "\t","\t","账户管理系统", "\t","\t","丨")
    print(" —————————————————————————————")
    print("丨", "\t","\t"," 1、开  户   ", "\t","\t","丨")
    print("丨", "\t","\t"," 2、存  钱   ", "\t","\t","丨")
    print("丨", "\t","\t"," 3、取  钱   ", "\t","\t","丨")
    print("丨", "\t","\t"," 4、转  账   ", "\t","\t","丨")
    print("丨", "\t","\t"," 5、查  询   ", "\t","\t","丨")
    print("丨", "\t","\t"," 6、退  出   ", "\t","\t","丨")
    print(" —————————————————————————————")

# 界面操作逻辑
while True:
    welcome() # 打印页面
    chose = input("请输入您的业务编号：")
    if chose == '1':
        addUser()
    elif chose == '2':
        access()
    elif chose == '3':
        takemoney()
    elif chose == '4':
        transfermoney()
    elif chose == '5':
        check()
    elif chose == '6':
        print("再见！")
        break
    else:
        print("输入格式错误，请重新输入。")




















































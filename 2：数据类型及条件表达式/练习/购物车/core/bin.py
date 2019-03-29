#--*-- coding:utf-8 --*--
# @Time   ： 2019/3/29 15:59
# @Author : Wesley
# @File   : core.py

def read_user():
    '''read user info from user.db'''
    user_dict = {}
    with open('user.db','r',encoding='utf-8') as user_info:
        for line in user_info:
            username,password = line.strip().split(':')
            user_dict[username] = password
    return user_dict

def login():
    '''user login'''
    number = 0
    user_dict = read_user()
    while True:
        username = input("please input username: ").strip()
        if username in user_dict.keys():
            password = input("please input password: ").strip()
            if password == user_dict[username]:
                print("user login succeed!")
            else:
                print("passwrod error , please enter again")
                number = number + 1
                if number == 3:
                    print("input error number is %d" % number)
                    break
        else:
            print("username is not found, please enter again")
            number = number + 1
            if number == 3:
                print("input error number is %d" % number)
                break

def input_salary():
    '''input user salary'''
    pass

def shopping():
    '''user shopping'''
    product_list = [['牛肉汤', 15],
                    ['大排饭', 18],
                    ['鸡腿饭', 15],
                    ['小馄饨', 10],
                    ['大馄饨', 16],
                    ['炒面加肉丝', 15],]
    salary = input("please input salary: ").strip()
    while True:
        shopping_cart = []
        for index,product in enumerate(product_list):
            print(index,product)
        choice = input('输入商品编号购物，输入q:>> ').strip()
        if choice.isdigit():
            choice = int(choice)
            if choice < 0 or choice >= len(product_list):
                continue
            pname = product_list[choice][0]
            pprice = product_list[choice][1]
            if salary > pprice:
                if pname in

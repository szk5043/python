# --*-- coding:utf-8 --*--
# @Time   ： 2019/5/10 14:22
# @Author : Wesley
# @File   : src.py

from interface import user, shopping, bank
from lib import common

user_info = {'name': None}


def login():
    '''用户登录'''
    while True:
        username = input('请输入用户名: ').strip()
        password = input('请输入密码：').strip()
        flag, msg = user.login_interface(username, password)
        if flag:
            print(msg)
            user_info['name'] = username
            break
        else:
            print(msg)


def register():
    '''用户注册'''
    while True:
        username = input('请输入用户名: ').strip()
        password = input('请输入密码：').strip()
        conf_password = input('请再输入一次密码：').strip()
        if password == conf_password:
            flag, msg = user.register_interface(username, password)
            if flag:
                print(msg)
                break
            else:
                print(msg)


@common.auth
def check_balance():
    '''查看余额'''
    balance = user.check_balance_interface(user_info['name'])
    print(balance)


@common.auth
def transfer():
    '''转账'''
    to_user = input('请输入转账的用户名: ').strip()
    balance = input('请输入转账的金额: ').strip()
    if not balance.isdigit():
        print('请输入数字')
    balance = int(balance)
    flag, msg = bank.transfer_interface(user_info['name'], to_user, balance)
    if flag:
        print(msg)
    else:
        print(msg)


@common.auth
def repay():
    '''还款'''
    balance = input('请输入还款金额: ').strip()
    if not balance.isdigit():
        print('请输入数字')
    balance = int(balance)
    msg = bank.repay_interface(user_info['name'], balance)
    print(msg)


@common.auth
def withdraw():
    '''取款'''
    balance = input('请输入取款金额: ').strip()
    if not balance.isdigit():
        print('请输入数字')
    balance = int(balance)
    flag, msg = bank.withdraw_interface(user_info['name'], balance)
    if flag:
        print(msg)
    else:
        print(msg)


@common.auth
def check_record():
    '''查看流水'''
    flag, msg = bank.check_record_interface(user_info['name'])
    if flag:
        for bankflow in msg:
            print(bankflow)
    else:
        print(msg)


@common.auth
def shop():
    '''购物车'''
    shop_list = [
        ['office', 15],
        ['肠粉', 20],
        ['地锅鸡', 80],
        ['南非干鲍', 480],
        ['血燕', 1080],
        ['MacBook Pro', 16800],
        ['特斯拉', 980000]
    ]

    shopping_cart = {}  # 购物车
    while True:
        for i, shops in enumerate(shop_list):
            print(i, shops)
        chioce = input('请选择商品编号：').strip()
        if not chioce.isdigit():
            print('请输入正确的商品编号')
        if int(chioce) > len(shop_list) and int(chioce) < 0:
            print('您输入的商品编号不存在')
        shop, price = shop_list[int(chioce)]
        sure = input('立即付款or添加进购物车，请输入 F|J:').strip()
        if sure == 'F':
            # 选中商品，直接付款
            if not shop in shopping_cart:
                shopping_cart[shop] = {'price': price, 'number': 1}
            shopping_cart[shop]['number'] += 1
            flag, msg = shopping.pay_interface(user_info['name'], shopping_cart)
            # 调用结账接口购买商品
            if flag:
                print(msg)
                break
            else:
                print(msg)
        elif sure == 'J':
            # 加入购物车，稍后选择是否付款
            if not shop in shopping_cart:
                shopping_cart[shop] = {'price': price, 'number': 1}
            shopping_cart[shop]['number'] += 1
            msg = shopping.shopping_cart_interface(user_info['name'], shopping_cart)
            # 调用购物车接口进行添加进购物车
            print(msg)
            sure2 = input('是否对购物车的商品进行结算Y ,返回上级菜单按q/Q').strip()
            if sure2 == 'Y':
                flag, msg = shopping.pay_interface(user_info['name'], shopping_cart)
                if flag:
                    print(msg)
                    break
                else:
                    print(msg)
            elif sure2 == 'Q' or sure2 == 'q':
                break


@common.auth
def check_shopping_cart():
    '''查看已购买商品'''
    reticule = shopping.check_shop_cart_interface(user_info['name'])
    if reticule:
        for shop, shop_dic in reticule.items():
            price = shop_dic['price']
            number = shop_dic['number']
            print('品名：%s ，价格：%s，数量：%s ' % (shop, price, number))
    else:
        print('您的口袋空空如也，赶紧去购物吧')


@common.auth
def logout():
    '''用户注销'''
    user_info['name'] = None


func_dic = {

    '1': login,
    '2': register,
    '3': check_balance,
    '4': transfer,
    '5': repay,
    '6': withdraw,
    '7': check_record,
    '8': shop,
    '9': check_shopping_cart,
    '10': logout
}


def run():
    '''主函数'''
    while True:
        print('''
         1、登录
         2、注册
         3、查看余额
         4、转账
         5、还款
         6、取款
         7、查看流水
         8、购物
         9、查看购买商品        
         10、注销        
         ''')
        choice = input('请选择:').strip()
        if choice == 'q': break
        if choice not in func_dic: continue
        func_dic[choice]()

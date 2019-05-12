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
    flag , msg = bank.withdraw_interface(user_info['name'], balance)
    if flag:
        print(msg)
    else:
        print(msg)


@common.auth
def check_record():
    '''查看流水'''
    bankflow_list = bank.check_record_interface(user_info['name'])
    for bankflow in bankflow_list:
        print(bankflow)

@common.auth
def shop():
    '''
      1 先循环打印出商品
      2 用户输入数字选择商品（判断是否是数字，判断输入的数字是否在范围内）
      3 取出商品名，商品价格
      4 判断用户余额是否大于商品价格
      5 余额大于商品价格时，判断此商品是否在购物车里
          5.1 在购物车里，个数加1
          5.1 不在购物车里，拼出字典放入（｛‘car’：｛‘price’：1000，‘count’：2｝,‘iphone’：｛‘price’：10，‘count’：1｝｝）
      6 用户余额减掉商品价格
      7 花费加上商品价格
      8 当输入 q时，购买商品
          8.1 消费为0 ，直接退出
          8.2 打印购物车
          8.3 接受用户输入，是否购买 当输入y，直接调购物接口实现购物
      :return:
      '''
    pass


@common.auth
def check_shopping_cart():
    '''查看购物车'''
    pass


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

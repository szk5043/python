import time
from bin import user_manage


def shopping(user_config_file, user_dict, user_login_status):
    # def shopping():
    '''购物'''
    shopping_list = [
        ['coffee', 10],
        ['chicken', 20],
        ['iphone', 8000],
        ['macPro', 15000],
        ['car', 100000]
    ]
    shopping_car = []
    if not user_login_status:
        print('跳转至登录页面!\n')
        user_login_status = user_manage.user_login(user_config_file, user_dict)
    while True:
        for i, list in enumerate(shopping_list):
            print(i, list)
        num = input('请输入要购买的商品编号：').strip()
        if num == 'Q' or num == 'q': break
        for username in user_login_status.keys():
            if user_login_status[username]['balance'] >= shopping_list[int(num)][1]:
                choice = input('这款商品%s元，确认购买Y/y: ' % shopping_list[int(num)][1]).strip()
                if choice == 'Y' or choice == 'y':
                    user_login_status[username]['balance'] -= shopping_list[int(num)][1]
                    shopping_car.append(shopping_list[int(num)][0])
                    print('这款商品%s已成功加入购物车，是否继续购买？Q/q退出： ' % shopping_list[int(num)][0])
            else:
                choice = input('您的余额不足，是否充值Y/y: ').strip()
                if choice == 'Y' or choice == 'y':
                    recharge(user_dict, user_login_status)
        print(user_login_status, shopping_car)
    return user_login_status, shopping_car


def recharge(user_dict, user_login_status):
    '''充值'''
    for username in user_login_status.keys():
        if username:
            balance = int(input("请输入充值的金额：").strip())
            user_login_status[username]['balance'] += balance
            return user_login_status
        else:
            print('请先登录!\n')
            time.sleep(1)
            return user_login_status

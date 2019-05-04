import os
import sys

BASE_DIR = (os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(BASE_DIR)
# 添加环境变量

from bin import user_manage
from bin import shopping
# 导入模块

def main():
    '''主程序'''
    user_config_file = '/Users/zhengkaishen/PycharmProjects/untitled/模块作业/ATM/db/user.info.txt'
    user_dict = user_manage.user_read(user_config_file)
    user_login_status = {}
    menu = """'1': '用户登录',
'2': '用户注册',
'3': '用户注销',
'4': '购物',
'5': '充值',
'6': '退出系统'"""

    while True:
        print(menu)
        num = int(input("Please input num: ").strip())
        if num == 1:
            user_login_status = user_manage.user_login(user_config_file, user_dict)
        elif num == 2:
            user_manage.user_register(user_config_file, user_dict)
        elif num == 3:
            user_login_status = user_manage.user_logout(user_config_file, user_dict, user_login_status)
        elif num == 4:
            user_login_status, shopping_car = shopping.shopping(user_config_file, user_dict, user_login_status)
        elif num == 5:
            user_login_status = shopping.recharge(user_dict, user_login_status)
        elif num == 6:
            user_manage.user_write(user_config_file, user_login_status)
            sys.exit(0)


if __name__ == '__main__':
    main()

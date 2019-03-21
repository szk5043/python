#--*-- coding:utf-8 --*--
# @Time   ： 2019/3/18 16:17
# @Author : Wesley
# @File   : main.py
import os
import sys
BASE_DIR = (os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
#获取文件夹根目录
sys.path.append(BASE_DIR)
#添加环境变量

from core import bin
#导入模块

def main():
    '''主程序'''
    user_dict = bin.read_user()
    # 获取已注册用户信息
    lock_user_list = bin.read_blocklist()
    # # 获取黑名单用户
    menu = '''Usage:
    -r : regiset new user
    -g : user login
    -h : help
    '''
    choice = input("Input Option or -h see help: ").strip()
    if choice == "-r":
        bin.regiset_user(user_dict)
        # 注册用户
    elif choice == "-g":
        bin.login(user_dict,lock_user_list)
        # 登录用户
    else:
        print(menu)
        # 打印菜单

if __name__ == '__main__':
    main()



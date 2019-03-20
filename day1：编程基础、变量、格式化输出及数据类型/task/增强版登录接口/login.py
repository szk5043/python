#--*-- coding:utf-8 --*--
# @Time   ： 2019/3/18 16:17
# @Author : Wesley
# @File   : login.py
import os
import sys
BASE_DIR = (os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
#获取文件夹根目录
sys.path.append(BASE_DIR)
#添加环境变量

from core import main
#导入模块

def login():
    '''用户登录主程序'''
    user_dict = main.read_user()
    # 获取已注册用户信息
    lock_user_list = main.read_blocklist()
    print(lock_user_list)
    # 获取黑名单用户信息
#     choice = input('''Options:
# -u: user login
# -r: user registration
# Please input: ''').strip()
#     #用户登录或者注册新用户
#     input_number = 0
#     if choice == "-r":
#         while True:
#             username = input("Please input registered user: ").strip()
#             for user in user_dict.keys():
#                 if username != user:
#                     # 若用户名没有被使用
#                     passwd = input("Please input password: ").strip()
#                     print('%s is registered successful !' % username )
#                     main.regiset_user(username,passwd)
#                     exit(0)
#                 if username == user:
#                     # 若用户名已经被使用
#                     print("The user %s already exists. Please enter again " % username )
#                     main.write_blocklist(input_number,username)
#                     # 输错三次，锁定用户
#     elif choice == "-u":
#         username = input("Please input user name: ").strip()
#         passwd = input("Please input user passwd: ").strip()
#         for user in lock_user_list:
#             if username == user:
#                 #若用户在黑名单中
#                 print('The %s is lockd! exit...' % username )
#                 exit(1)
#                 while True:
#                     for user in user_dict.keys():
#                         if username != user:
#                         # 若用户名不存在
#                             print('The %s is not found ! Please enter again')
#                             main.write_blocklist(input_number, username)
#                             # 输错三次，锁定用户
#                         elif username == user:
#                         #若用户名存在
#                             if passwd == user_dict[username]:
#                                 #若密码在user.db中
#                                 print('%s login successful !')
#                             elif passwd != user_dict[username]:
#                                 print('Passwd error，Please enter again !')
#                                 main.write_blocklist(input_number, username)
#     else:
#         print('''Options:
# -u: user login
# -r: user registration''')

login()




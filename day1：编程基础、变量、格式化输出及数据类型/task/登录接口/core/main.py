#--*-- coding:utf-8 --*--
# @Time   ： 2019/3/18 15:51
# @Author : Wesley
# @File   : loggin.py
import sys
import os
BASE_DIR = os.path.dirname( os.path.dirname( os.path.abspath(__file__) ) )
sys.path.append(BASE_DIR)

def say_hello():
    print('hello')

# def read_blocklist():
#     with open('blocklist.db','r',encoding='utf-8') as lock_user :
#         data = lock_user.read()
#         print(date)
#
# read_blocklist()

if __name__ == '__main__':
    print("this is main")
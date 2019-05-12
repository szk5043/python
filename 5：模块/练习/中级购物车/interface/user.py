# --*-- coding:utf-8 --*--
# @Time   ： 2019/5/10 14:52
# @Author : Wesley
# @File   : user.py

import sys
import hashlib
import time
from conf import settings
from db import db_handler

sys.path.append(settings.BASE_PATH)


def register_interface(username, password):
    user_dic = db_handler.select(username)
    if not user_dic:
        password = hashlib.md5(password.encode('utf-8'))
        register_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        # 增加注册时间为密码哈希参数
        password.update(register_time.encode())
        user_dic = {'name': username,
                    'password': password.hexdigest(),
                    'balance': 15000,
                    'bankflow': [],
                    'shoppingcart': {},
                    'register_time': register_time}
        db_handler.save(user_dic)
        return True, '注册成功'
    else:
        return False, '用户已存在'


def login_interface(username, password):
    user_dic = db_handler.select(username)
    if not user_dic:
        return False, '用户不存在'
    password = hashlib.md5(password.encode('utf-8'))
    password.update(user_dic['register_time'].encode())
    # 获取注册时间为密码哈希参数
    if password.hexdigest() == user_dic['password']:
        return True, '登录成功'


def check_balance_interface(username):
    user_dic = db_handler.select(username)
    balance = user_dic['balance']
    return balance

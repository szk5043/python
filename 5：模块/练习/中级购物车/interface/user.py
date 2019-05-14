# --*-- coding:utf-8 --*--
# @Time   ： 2019/5/10 14:52
# @Author : Wesley
# @File   : user.py

import sys
import hashlib
import time
from conf import settings
from db import db_handler
from lib import common

sys.path.append(settings.BASE_PATH)
user_logger = common.get_logger('user')


def register_interface(username, password):
    user_dic = db_handler.select(username)
    if not user_dic:
        password = hashlib.md5(password.encode('utf-8'))
        register_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        # 增加注册时间为密码哈希参数
        password.update(register_time.encode('utf-8'))
        user_dic = {'name': username,
                    'password': password.hexdigest(),
                    'balance': 15000,
                    'bankflow': [],
                    'shopping_cart': {},  # 购物车：存放未结账商品
                    'reticule': {},  # 手提袋：存放已购买商品
                    'locked': False,
                    'register_time': register_time}
        db_handler.save(user_dic)
        user_logger.info('%s注册成功!' % username)
        return True
    else:
        user_logger.info('%s用户已存在!' % username)
        return False


def login_interface(username, password):
    user_dic = db_handler.select(username)
    if not user_dic:
        user_logger.info('%s用户不存在!' % username)
        return False
    password = hashlib.md5(password.encode('utf-8'))
    password.update(user_dic['register_time'].encode())
    # 获取注册时间为密码哈希参数
    if password.hexdigest() == user_dic['password']:
        user_logger.info('%s用户登录成功!' % username)
        return True


def check_balance_interface(username):
    user_dic = db_handler.select(username)
    balance = user_dic['balance']
    return balance

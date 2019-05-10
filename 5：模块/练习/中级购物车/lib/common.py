#--*-- coding:utf-8 --*--
# @Time   ： 2019/5/10 15:37
# @Author : Wesley
# @File   : common.py

from core import src


def auth(func):
    def inner(*args, **kwargs):
        if src.user_info['name']:
            res = func(*args, **kwargs)
            return res
        else:
            src.login()
    return inner

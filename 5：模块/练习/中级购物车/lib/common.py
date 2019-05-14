#--*-- coding:utf-8 --*--
# @Time   ： 2019/5/10 15:37
# @Author : Wesley
# @File   : common.py
import logging.config
from core import src
from conf import settings

def auth(func):
    '''登录认证装饰器'''
    def inner(*args, **kwargs):
        if src.user_info['name']:
            res = func(*args, **kwargs)
            return res
        else:
            src.login()
    return inner

def get_logger(name):
    logging.config.dictConfig(settings.LOGGING_DIC)
    logger = logging.getLogger(name)
    return logger

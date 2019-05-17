#--*-- coding:utf-8 --*--
# @Time   ： 2019/5/16 16:53
# @Author : Wesley
# @File   : db_handler.py

import shelve
from conf import settings


shv_tool = shelve.open(settings.DB_PATH)

def select():
    '''查询中奖纪录'''
    res = shv_tool['bingo']
    shv_tool.close()
    return res

def save(bingo):
    '''保存中奖纪录'''
    shv_tool['bingo'] = bingo
    #shv_tool.close()



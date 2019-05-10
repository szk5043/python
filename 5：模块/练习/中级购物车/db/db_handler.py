# --*-- coding:utf-8 --*--
# @Time   ： 2019/5/10 15:02
# @Author : Wesley
# @File   : db_handler.py
import json
import os
from conf import settings


def save(user_dict):
    path = os.path.join(settings.DIR_DB, '%s.json' % user_dict['name'])
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(user_dict, f)


def select(name):
    path = os.path.join(settings.DIR_DB, '%s.json' % name)
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as f:
            user_dic = json.load(f)
            return user_dic
    else:
        return False
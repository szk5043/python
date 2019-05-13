# --*-- coding:utf-8 --*--
# @Time   ： 2019/5/10 15:02
# @Author : Wesley
# @File   : db_handler.py
import json
import os
import json
from conf import settings


def select(username):
    json_path = os.path.join(settings.DB_PATH, '%s.json' % username)
    if os.path.exists(json_path):
        with open(json_path, 'r', encoding='utf-8') as f:
            user_dic = json.load(f)
            return user_dic


def save(user_dic):
    username = user_dic['name']
    json_path = os.path.join(settings.DB_PATH, '%s.json' % username)
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(user_dic, f, ensure_ascii=False)

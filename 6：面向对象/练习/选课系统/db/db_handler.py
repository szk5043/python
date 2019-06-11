#--*-- coding:utf-8 --*--
# @Time   ： 2019/5/28 15:17
# @Author : Wesley
# @File   : db_handler.py
import os
import pickle
from conf import settings


def save(obj):
    '''将对象保存进文件'''
    obj_dir = os.path.join(settings.DB_PATH,obj.__class__.__name__.lower())
    # 对象拼接，找到具体的文件夹路径，如 `选课系统/db/school`
    obj_file = os.path.join(obj_dir,obj.name)
    # 对象名拼接，找到具体的文件名路径，如`选课系统/db/school/szk`
    if not os.path.exists(obj_dir):
    # 如果没有则创建，并且将对象写入文件
        os.mkdir(obj_dir)
    with open(obj_file,'wb') as f:
        pickle.dump(obj,f)
        f.flush()


def select(name,type):
    '''从文件读取对象'''
    obj_file = os.path.join(settings.DB_PATH,type,name)
    # 对象名拼接，找到具体的文件名路径。如`选课系统/db/school/szk`
    if os.path.exists(obj_file):
    # 如果有，则从文件中读取对象
        with open(obj_file,'rb') as f:
            return pickle.load(f)

#--*-- coding:utf-8 --*--
# @Time   ： 2019/5/28 15:17
# @Author : Wesley
# @File   : db_handler.py
import os
import pickle
from conf import settings


def save(obj):
    '''将对象保存进文件'''
    path_obj = os.path.join(settings.DB_PATH,obj.__class__.__name__.lower())
    path_file = os.path.join(path_obj,obj.name)
    if not os.path.exists(path_obj):
        os.mkdir(path_obj)
    with open(path_file,'wb') as f:
        pickle.dump(obj,f)
        f.flush()


def select(name,type):
    '''从文件读取对象'''
    path_obj = os.path.join(settings.DB_PATH,type)
    path_file = os.path.join(path_obj,name)
    if not os.path.exists(path_obj):
        os.mkdir(path_obj)
    if os.path.exists(path_file):
        with open(path_obj,'rb') as f:
            return pickle.load(f)
    else:
        return False
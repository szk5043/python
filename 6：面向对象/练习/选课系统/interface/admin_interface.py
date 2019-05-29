#--*-- coding:utf-8 --*--
# @Time   ： 2019/5/28 15:15
# @Author : Wesley
# @File   : admin_interface.py
from db.modles import Admin
from lib import common

def register_interface(user,passwd):
    '''管理员注册接口'''
    file_names = common.get_all_fileName(Admin.__name__.lower())
    # 获取已经创建的用户名，如果存在，则返回空
    if user in file_names:
        return
    admin = Admin(user,passwd)
    return admin

def login_interface(user,passwd):
    obj = Admin.select(user)
    if obj and obj.passwd == passwd:
        return obj

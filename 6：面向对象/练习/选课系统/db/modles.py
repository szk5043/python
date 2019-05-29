#--*-- coding:utf-8 --*--
# @Time   ： 2019/5/29 13:56
# @Author : Wesley
# @File   : modles.py
from db import db_handler

class People():
    '''公共方法基类'''

    def save(self):
        db_handler.save(self)

    @classmethod
    def select(cls,name):
        return db_handler.select(name,cls.__name__.lower())

class Admin(People):
    '''管理员类'''
    def __init__(self,name,passwd):
        self.name = name
        self.passwd = passwd
        self.save()

    def __str__(self):
        return "name:%s password:%s " % (self.name,self.passwd)


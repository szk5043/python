#--*-- coding:utf-8 --*--
# @Time   ： 2019/5/29 13:56
# @Author : Wesley
# @File   : modles.py
from db import db_handler

class BaseClass():
    '''公共方法基类'''

    def save(self):
    # 将对象自身调用save函数进行保存
        db_handler.save(self)

    @classmethod
    def select(cls,name):
    # 将类自身和对象名字调用select函数进行查询
        return db_handler.select(name,cls.__name__.lower())

class Admin(BaseClass):
    '''管理员类，属性： 姓名、密码
    '''
    def __init__(self,name,passwd):
        self.name = name
        self.passwd = passwd
        self.save()

    def __str__(self):
        return "name:%s password:%s " % (self.name,self.passwd)

class School(BaseClass):
    '''学校类，属性：名称、地址、课程'''
    def __init__(self,name,address):
        self.name = name
        self.address = address
        self.courses = []
        self.save()

    def __str__(self):
        return 'name:%s address:%s' % (self.name,self.address)

class Teacher(BaseClass):
    '''老师类，属性：名字、密码、校区、课程'''
    def __init__(self,name,passwd,schoolName):
        self.name = name
        self.passwd = passwd
        self.schoolName = schoolName
        self.courses = []
        self.save()

    def __str__(self):
        return "name:%s courses:%s school:%s" %(self.name,self.courses,self.schoolName)

class Course(BaseClass):
    '''课程类，属性：名字、价格、课程周期、学习的学生'''
    def __init__(self,name,price,period):
        self.name = name
        self.price = price
        self.period = period
        self.students = []
        self.save()

    def __str__(self):
        return "name:%s price:%s period:%s students:%s" % (self.name,self.price,self.period,self.students)

class Student(BaseClass):
    '''学生类，属性：姓名、密码、校区、课程、成绩'''
    def __init__(self,name,passwd,schoolName,courses,scorer):
        self.name = name
        self.passwd = passwd
        self.schoolName = schoolName
        self.courses = courses
        self.scorer = scorer
        self .save()

    def __str__(self):
        return "name:%s passwd:%s schoolName:%s courses:%s scorer:%s" % (self.name,self.passwd,self.schoolName,self.courses,self.scorer)
#--*-- coding:utf-8 --*--
# @Time   ： 2019/5/28 15:15
# @Author : Wesley
# @File   : admin_interface.py
from db.modles import *
from lib import common

def register_interface(user,passwd):
    '''管理员注册接口'''
    obj = Admin.select(user)
    # 获取已经创建的用户名，如果存在，则返回空
    if obj:
        return
    admin = Admin(user,passwd)
    return admin

def login_interface(user,passwd):
    '''管理员登录接口'''
    obj = Admin.select(user)
    if obj and obj.passwd == passwd:
        return obj

def create_school(name,address):
    '''创建学校接口，如果学校存在，则返回None；不存在，则创建'''
    obj = School.select(name)
    if obj:
        return
    sc = School(name,address)
    return sc

def get_school():
    '''查询所有学校接口'''
    return common.get_all_fileName('school')

def create_teacher(name,scName,pwd):
    '''创建老师接口：如果老师存在，则返回None；不存在，则创建'''
    obj = Teacher.select(name)
    if obj:
        return
    t = Teacher(name,pwd,scName)
    return t

def create_course(scName, cname, price, period):
    '''创建课程接口：课程包含 校区、课程名、课程价格、课程周期 相关属性'''
    sc = School.select(scName)
    if cname in sc.courses:
        '''如果课程已经在学校课程属性中，则返回空'''
        return
    c = Course(cname,price,period)
    # 创建新课程，并加入到学校中
    sc.courses.append(cname)
    # 关联学校
    sc.save()
    return c



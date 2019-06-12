#--*-- coding:utf-8 --*--
# @Time   ： 2019/5/28 15:17
# @Author : Wesley
# @File   : teacher_interface.py

from db.modles import *
from lib import common

def login_interface(user, passwd):
    '''老师登录接口'''
    obj = Teacher.select(user)
    print('------老师对象',obj)
    if obj and obj.passwd == passwd:
        return obj

def check_course_interface(teacher):
    '''查看教授课程接口,直接查看类中属性'''
    if not teacher.courses:
        return
    return teacher.courses

def check_all_course_interface():
    '''查看所有课程'''
    coures =  common.get_all_fileName('course')
    if not coures:
        return
    return coures

def bind_to_course_interface(teacher,course):
    '''给老师绑定课程'''
    teacher.bind_to_course(course)

def check_student_interface(coure):
    '''查看课程下学生接口，查看老师类中学生属性'''
    if not coure.students:
        return
    return coure.students


def modify_score_interface():
    '''修改学生成绩接口，查看老师类中的课程，查看课程下的学生，选择学生打分，打完分  保存老师、学生、课程类'''
    pass
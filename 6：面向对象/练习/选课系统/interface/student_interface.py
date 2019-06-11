#--*-- coding:utf-8 --*--
# @Time   ： 2019/5/28 15:16
# @Author : Wesley
# @File   : student_interface.py
from db.modles import *
from lib import common

def register_interface(user,passwd):
    '''学生注册接口'''
    obj = Student.select(user)
    # 获取已经创建的用户名，如果存在，则返回空；如果不存在，则创建
    if obj:
        return
    student = Student(user,passwd)
    return student

def login_interface(user, passwd):
    '''学生登录接口'''
    obj = Student.select(user)
    if obj and obj.passwd == passwd:
        return obj

def select_school(user,scName):
    '''选择学校接口'''
    user.schoolName = scName
    user.save()

def select_coures(student,course_name):
    if course_name in student.courses:
        return False
    else:
        # 学生的课程列表中添加课程
        student.courses.append(course_name)
        student.save()
        # 课程的学员列表中添加学生
        c = Course.select(course_name)
        c.students.append(student.name)
        c.save()
        return True

def get_course_name(schoolName):
    # 获取学校类中的课程属性
    return School.select(schoolName).courses



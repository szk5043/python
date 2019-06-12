#--*-- coding:utf-8 --*--
# @Time   ： 2019/5/28 15:15
# @Author : Wesley
# @File   : common.py
import os
from conf import settings


def login_status(auth_type):
    '''带参装饰器'''
    from core import student, teacher, admin
    def auth(func):
        def inner(*args,**kwargs):
            if auth_type == 'student':
                if student.student_status['user'] is None:
                    print('请先登录！')
                    student.student_login()
                else:
                    return func(*args,**kwargs)
            elif auth_type == 'teacher':
                if teacher.teacher_status['user'] is None:
                    print('请先登录！')
                    teacher.teacher_login()
                else:
                    return func(*args,**kwargs)
            elif auth_type == 'admin':
                if admin.admin_status['user'] is None:
                    print('请先登录！')
                    admin.admin_login()
                else:
                    return func(*args, **kwargs)
        return inner
    return auth

def get_all_fileName(dirName):
    '''获取所有文件列表'''
    dir_path = os.path.join(settings.DB_PATH,dirName)
    if os.path.exists(dir_path):
        return os.listdir(dir_path)

def select_school():
    '''查询学校'''
    from interface import admin_interface
    schoolNames = admin_interface.get_school()
    if not schoolNames:
        print('暂时没有校区')
        return
    i = 0
    for i,school in enumerate(schoolNames):
        print(i,':',school)
    while True:
        num = input('请选择学校编号: ').strip()
        if num  == 'q':
            return
        if num.isdigit() and int(num) <= len(schoolNames):
            scName = schoolNames[int(num)]
            return scName
        else:
            print('输入不正确，请重试')



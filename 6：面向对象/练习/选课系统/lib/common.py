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
                if student.student_status['name'] is None:
                    print('请先登录！')
                    student.student_login()
                else:
                    return func(*args,**kwargs)
            elif auth_type == 'teacher':
                if teacher.teacher_status['name'] is None:
                    print('请先登录！')
                    teacher.teacher_login()
                else:
                    return func(*args,**kwargs)
            elif auth_type == 'admin':
                if admin.admin_status['name'] is None:
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
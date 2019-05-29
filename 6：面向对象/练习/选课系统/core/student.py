#--*-- coding:utf-8 --*--
# @Time   ： 2019/5/28 16:21
# @Author : Wesley
# @File   : student.py

from interface import student_interface
from lib import common

student_status = {
    'user':None
}

def student_register():
    '''学生注册'''
    while True:
        user = input('请输入注册的用户名：').strip()
        passwd = input('请输入注册的密码：').strip()
        conf_passwd = input('请再输入一次密码：').strip()
        if user == 'q' or passwd == 'q':break
        if user is None or passwd is None:
            print('用户名或密码不能为空！')
            continue
        if passwd != conf_passwd:
            print('两次密码输入不同，请重新输入!')
            continue
        is_flag,msg = student_interface.register_interface(user,passwd)
        if is_flag:
            print(msg)
        else:
            print(msg)

def student_login():
    '''学生登录'''
    user = input('请输入登录的用户名：').strip()
    passwd = input('请输入登录的密码：').strip()
    is_flag, msg = student_interface.login_interface(user, passwd)
    if is_flag:
        print(msg)
        student_status['user'] = user
    else:
        print(msg)

@common.login_status(auth_type = 'student')
def choose_school():
    '''选择校区'''
    print('选择校区')
    # while True:
    #     school_name_list = school_interface.check_all_school()
    #     if not

@common.login_status(auth_type = 'student')
def choose_course():
    '''选择课程'''
    pass

@common.login_status(auth_type = 'student')
def check_score():
    '''查看成绩'''
    pass

def student_view():
    '''学生视图'''
    pass
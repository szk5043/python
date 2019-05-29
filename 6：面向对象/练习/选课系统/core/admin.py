#--*-- coding:utf-8 --*--
# @Time   ： 2019/5/28 16:21
# @Author : Wesley
# @File   : admin.py
from interface import admin_interface

admin_status = {
    'user':None
}

def admin_register():
    '''管理员注册'''
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
        obj = admin_interface.register_interface(user,passwd)
        # 调用接口层处理业务逻辑
        if obj:
            print('注册成功')
            return
        else:
            print('用户已存在，请重新输入')


def admin_login():
    '''管理员登录'''
    while True:
        user = input('请输入用户名：').strip()
        passwd = input('请输入密码：').strip()
        if user == 'q' or passwd == 'q':break
        obj = admin_interface.login_interface(user,passwd)
        # 调用接口层处理业务逻辑
        if obj:
            print('登录成功')
            admin_status['user'] = user
            return
        else:
            print('用户名或密码错误')


def creat_school():
    '''创建学校'''
    pass


def creat_teacher():
    '''创建老师'''
    pass


def creat_course():
    '''创建课程'''
    pass

def admin_view():
    '''管理员视图'''
    menu_dic = {
        '1': admin_register,
        '2': admin_login,
        '3': creat_school,
        '4': creat_teacher,
        '5': creat_course
    }
    while True:
        print('''
          1、管理员注册
          2、管理员登录
          3、创建学校
          4、创建老师
          5、创建课程
          ''')
        chioce = input('请选择相应的视图：').strip()
        if chioce == 'q':
            admin_status['user'] = None
            break
        if not chioce.isdigit():
            print('请输入正确的视图编号！')
        if chioce not in menu_dic:
            print('您输入的视图编号不存在，请重新输入！')
        menu_dic[chioce]()
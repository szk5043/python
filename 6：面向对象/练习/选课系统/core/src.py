#--*-- coding:utf-8 --*--
# @Time   ： 2019/5/28 15:15
# @Author : Wesley
# @File   : src.py
from core import admin,student,teacher

def start():
    menu_dic = {
        '1': student.student_view,
        '2': teacher.teacher_view,
        '3': admin.admin_view
    }
    while True:
        print('''
        1、学生视图
        2、老师视图
        3、管理员视图
        ''')
        chioce = input('请选择相应的视图：').strip()
        if chioce == 'q': break
        if not chioce.isdigit():
            print('请输入正确的视图编号！')
        if chioce not in menu_dic:
            print('您输入的视图编号不存在，请重新输入！')
        menu_dic[chioce]()

#--*-- coding:utf-8 --*--
# @Time   ： 2019/5/28 16:21
# @Author : Wesley
# @File   : teacher.py

from interface import teacher_interface
from lib import common

teacher_status = {
    'user':None
}


def teacher_login():
    '''老师登录'''
    while True:
        if teacher_status['user'] is not None:
            print('您已经登录')
            break
        else:
            user = input('请输入登录的用户名：').strip()
            passwd = input('请输入登录的密码：').strip()
            obj = teacher_interface.login_interface(user, passwd)
            if obj:
                print('登录成功')
                teacher_status['user'] = obj
                break
            else:
                print('登录失败')


@common.login_status(auth_type = 'teacher')
def check_course():
    '''查看教授课程'''
    courses = teacher_interface.check_course_interface(teacher_status['user'])
    if courses:
        for i,coures in enumerate(courses):
            print(i,':',coures)
    else:
        print('目前没有教授的课程')

@common.login_status(auth_type = 'teacher')
def choose_course():
    '''选择教授课程'''
    coures = teacher_interface.check_all_course_interface()
    if not coures:
        print('暂无课程')
    while True:
        for i,coure in enumerate(coures):
            print(i,':',coure)
            num = input('请输入课程序号：').strip()
            if num == 'q':return
            if num.isdigit() and int(num) <= len(coures):
                if teacher_interface.bind_to_course_interface(teacher_status['user'],coures[int(num)]):
                    print('您已成功加入%s大家庭' % coures[int(num)])
                    return
                else:
                    print('您已经是该班的老师，请重新选择！')
            else:
                print('输入有误，请重试')


@common.login_status(auth_type = 'teacher')
def check_student():
    '''查看课程下的学生'''
    coures = teacher_interface.check_all_course_interface()
    if not coures:
        print('暂无课程')
    while True:
        for i,coure in enumerate(coures):
            print(i,':',coure)
            num = input('请输入课程序号：').strip()
            if num == 'q':return
            if num.isdigit() and int(num) <= len(coures):
                students = teacher_interface.check_student_interface(coures[int(num)])
                for student in students:
                    print(student)
            else:
                print('输入有误，请重试')


@common.login_status(auth_type = 'teacher')
def modify_score():
    '''修改学生成绩'''
    pass

def teacher_view():
    '''老师视图'''
    menu_dic = {
        '1': teacher_login,
        '2': check_course,
        '3': choose_course,
        '4': check_student,
        '5': modify_score
    }
    while True:
        print('''
            1、老师登录
            2、查看教授课程
            3、选择教授课程
            4、查看课程下的学生
            5、修改学生成绩
            ''')
        chioce = input('请选择相应的视图：').strip()
        if chioce == 'q':
            teacher_status['user'] = None
            break
        if not chioce.isdigit():
            print('请输入正确的视图编号！')
        if chioce not in menu_dic:
            print('您输入的视图编号不存在，请重新输入！')
        menu_dic[chioce]()
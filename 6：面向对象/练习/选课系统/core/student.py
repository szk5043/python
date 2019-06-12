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
        obj = student_interface.register_interface(user,passwd)
        if obj:
            print('注册成功')
        else:
            print('该用户已经注册')

def student_login():
    '''学生登录'''
    while True:
        if student_status['user'] is not None:
            print('您已经登录')
            break
        else:
            user = input('请输入登录的用户名：').strip()
            passwd = input('请输入登录的密码：').strip()
            obj = student_interface.login_interface(user, passwd)
            if obj:
                print('登录成功')
                student_status['user'] = obj
                break
            else:
                print('登录失败')

@common.login_status(auth_type = 'student')
def choose_school():
    '''选择校区'''
    if student_status['user'].schoolName:
        # 如果学生对象中有学校属性，则返回空
        print('您可已经是%s的学员了，不能更改' % (student_status['user'].schoolName))
        return
    scName = common.select_school()
    # 选择学校
    if scName is None:
        print('取消选择！')
    student_interface.select_school(student_status['user'],scName)
    print('您光荣的成为了%s的一份子' % scName)


@common.login_status(auth_type = 'student')
def choose_course():
    '''选择课程'''
    if not student_status['user'].schoolName:
    # 是否已经选择学校，如果没有先选择学校
        print('请先选择校区')
        choose_school()
        if not student_status['user'].schoolName:
            return

    cnames = student_interface.get_course_names(student_status['user'].schoolName)
    if not cnames:
        print('该校区暂无课程！')
    while True:
        for i,cname in enumerate(cnames):
            print(i,':',cname)
            num = input('请输入课程序号：').strip()
            if num == 'q':return
            if num.isdigit() and int(num) <= len(cnames):
                if student_interface.select_coures(student_status['user'],cnames[int(num)]):
                    print('您已成功加入%s大家庭' % cnames[int(num)])
                    return
                else:
                    print('您已经是该班的学员，请重新选择！')
            else:
                print('输入有误，请重试')


@common.login_status(auth_type = 'student')
def check_score():
    '''查看成绩'''
    if not student_status['user'].scorer:
        print('暂无成绩！')
        return
    print('您的成绩如下：')
    for k in student_status['user'].scorer:
        print("%-10s:%3s" % (k, student_status['user'].scorer[k]))
    input('输入任意内容继续')

def student_view():
    '''学生视图'''
    menu_dic = {
        '1': student_register,
        '2': student_login,
        '3': choose_school,
        '4': choose_course,
        '5': check_score
    }
    while True:
        print('''
          1、学生注册
          2、学生登录
          3、选择学校
          4、选择课程
          5、查看成绩
          ''')
        chioce = input('请选择相应的视图：').strip()
        if chioce == 'q':
            student_status['user'] = None
            break
        if not chioce.isdigit():
            print('请输入正确的视图编号！')
        if chioce not in menu_dic:
            print('您输入的视图编号不存在，请重新输入！')
        menu_dic[chioce]()
#--*-- coding:utf-8 --*--
# @Time   ： 2019/5/28 16:21
# @Author : Wesley
# @File   : admin.py
from interface import admin_interface
from lib import common

admin_status = {
    'user':None
}

def admin_register():
    '''管理员注册'''
    while True:
        user = input('请输入注册的用户名：').strip()
        passwd = input('请输入注册的密码：').strip()
        if user == 'q' or passwd == 'q':break
        conf_passwd = input('请再输入一次密码：').strip()
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
        if admin_status['user'] is not None:
            print('您已经登录')
            break
        else:
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

@common.login_status(auth_type = 'admin')
def creat_school():
    '''创建学校'''
    while True:
        name = input('请输入学校名: ').strip()
        address = input('请输入学校地址: ').strip()
        if name == 'q':break
        if name is None:
            print('学校名不能为空！')
            continue
        if address is None:
            print('学校地址不能为空！')
            continue
        obj = admin_interface.create_school(name,address)
        if obj:
            print('创建成功')
            break
        else:
            print('该校区已经存在！')



@common.login_status(auth_type = 'admin')
def creat_teacher():
    '''创建老师：输入教师姓名，列出校区列表，选择一个校区，得到校区名字，将名字和校区名给接口'''
    while True:
        name = input('请输入教师的姓名: ').strip()
        if name == 'q':return
        if name is None:
            print('姓名不能为空！')
            continue
        scName = common.select_school()
        obj = admin_interface.create_teacher(name,scName,'123')
        if obj:
            print('创建成功')
            break
        else:
            print('教师已经存在')


@common.login_status(auth_type = 'admin')
def creat_course():
    '''创建课程：课程应该属于某个校区，先选择为哪个校区创建课程，课程名不能为空、不能重复，包含价格和时间周期'''
    while True:
        scName = common.select_school()
        if scName is None:
            print('必须先选择一个学校！')
            continue
        while True:
            cname = input('请输入课程名称: ').strip()
            if cname == 'q':
                return
            if cname is None:
                print('课程名称不能为空')
                continue
            price = input('请输入价格: ').strip()
            if not price.isdigit():
                print('价格必须是整数')
            else:
                period = input('请输入课程周期：').strip()
                obj = admin_interface.create_course(scName, cname, price, period)
                if obj:
                    print('课程创建成功')
                    return
                else:
                    print('该小区已经存在该课程')



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
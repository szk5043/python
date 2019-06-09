'''
Ftp_server核心代码
'''
import os
import configparser
from conf import settings

user_info = {
    'user':None
}

def login():
    '''用户登录'''
    name = input('请输入用户名: ').strip()
    passwd = input('请输入密码: ').strip()
    if name is None or passwd is None:
        print('用户名或密码不能为空！')
    config = configparser.ConfigParser()
    config.read(settings.ACCOUNTS_FILE)
    if not name in config.sections():
        print('%s :用户不存在!' % name)
    if passwd != config[name]['password']:
        print('%s :用户密码错误!' %name)
    print('%s: 用户登录成功!' % name)
    user_info['user'] = name

def file_ls():
    '''文件查看'''
    user_path = os.path.join(settings.USER_HOME,user_info['user'])
    if not os.path.exists(user_path):
        os.mkdir(user_path)
        print('%s: 用户目录为空！' % user_info['user'])
    else:
        print(os.listdir(user_path))

def file_get():
    '''文件上传'''
    user_path = os.path.join(settings.USER_HOME, user_info['user'])
    file_path = input('请输入需要上传的文件路径: ').strip()
    file_name = file_path.rsplit('/',1)
    user_file_path = os.path.join(user_path,file_name)
    with open(user_file_path,'wb') as f_w:
        with open(file_path,'rb') as f_r:
            for line in f_r:
                f_w.write(line)

def file_put():
    '''文件下载'''
    user_path = os.path.join(settings.USER_HOME, user_info['user'])
    file_name = input('请输入需要下载的文件名称: ').strip()
    file_path = input('请输入需要下载的文件路径: ').strip()
    user_file_path = os.path.join(user_path,file_name)
    put_file = os.path.join(file_path,file_name)
    with open(user_file_path,'rb') as f_r:
        with open(put_file,'wb') as f_w:
            for line in f_r:
                f_w.write(line)

def run():

    menu_dic = {
        '1':file_ls,
        '2':file_get,
        '3':file_put,
    }

    while True:
        if user_info['user'] is None:
            login()
        else:
            print('''
            1、查看文件
            2、上传文件
            3、下载文件
            4、退出程序
            ''')
            choose = input('请输入相应的功能选项: ').strip()
            if choose == '4':break
            if not choose .isdigit():
                print('您输入的选项不合法！')
            if choose  not in menu_dic:
                print('您输入的选项不存在')
            menu_dic[choose]()


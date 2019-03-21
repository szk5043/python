#--*-- coding:utf-8 --*--
# @Time   ： 2019/3/18 16:17
# @Author : Wesley
# @File   : bin.py
def read_user():
    '''读取用户账号密码'''
    user_dict = {}
    with open('user.db', 'r', encoding='utf-8') as read_user:
        for line in read_user:
            (username,userpasswd) = line.strip().split(':')
            user_dict[username] = userpasswd
    return user_dict

def read_blocklist():
    '''读取黑名单用户'''
    lock_user_list = []
    with open('blocklist.db','r',encoding='utf-8') as read_lock_user :
        for line in read_lock_user:
            lock_user_list.append(line.strip())
    return lock_user_list

def write_blocklist(error_number,username):
    '''将输入密码三次用户写入黑名单'''
    if error_number == 3:
        print("Input error is %d，%s is lockd !" % (error_number,username))
        with open('blocklist.db','a',encoding='utf-8') as write_lock_user:
            write_lock_user.write('\n'+username)
            exit(1)

def login():
    '''用户登录程序'''
    user_dict = read_user()
    #获取用户信息{'szk': '123', 'wesley': '123'}
    lock_user_list = read_blocklist()
    #获取黑名单用户 ['qwe', 'sss']
    error_number = 0
    while True:
        username = input('Please input your name: ').strip()
        if username in lock_user_list:
            print('%s is locking' % username)
            exit(1)
        elif username in user_dict.keys():
            userpasswd = input('Please input you passwd: ').strip()
            if userpasswd == user_dict[username]:
                #通过用户名取的在字典中对应的密码，user_dict[keys]=values
                print("%s is logging succeed!" % username)
                exit(0)
            else:
                print("Your %s password is error!" % username)
                error_number = int(error_number) + 1
                write_blocklist(error_number,username)
                #启用黑名单程序判断
        else:
            print('%s user not found!' % username)
            error_number = int(error_number) + 1
            write_blocklist(error_number, username)
login()


#--*-- coding:utf-8 --*--
# @Time   ： 2019/3/19 11:29
# @Author : Wesley
# @File   : bin.py
def read_user():
    '''读取用户账号密码'''
    user_dict = {}
    with open('db/user.db', 'r', encoding='utf-8') as read_user:
        for line in read_user:
            (username, userpasswd) = line.strip().split(':')
            user_dict[username] = userpasswd
    return user_dict

def read_blocklist():
    '''读取黑名单用户'''
    lock_user_list = []
    with open('db/blocklist.db','r',encoding='utf-8') as read_lock_user :
        for line in read_lock_user:
            lock_user_list.append(line.strip())
    return lock_user_list

def regiset_user(user_dict):
    '''注册用户并写入user.db'''
    username = input('Please input your name: ').strip()
    error_number = 0
    while True:
        if username in user_dict.keys():
            print("%s is register, Please enter another user name !" %username)
            error_number = int(error_number) +1
            if error_number == 3:
                print('Warning, your input error number is %d !' % error_number)
                exit(1)
        else:
            userpasswd = input('Please input you passwd: ').strip()
            with open('db/user.db', 'a', encoding='utf-8') as write_user:
                write_user.write('\n' +username+':'+userpasswd)
                print("%s is regiset succeed!" % username)

def write_blocklist(error_number,username):
    '''判断用户输错次数，大于三次写入黑名单'''
    if error_number == 3:
        print('Warning, your input number is %d , %s status is locked !' % (error_number,username))
        with open('db/blocklist.db', 'a', encoding='utf-8') as write_lock_user:
            write_lock_user.write('\n' + username)
            exit(1)

def login(user_dict,lock_user_list):
    '''用户登录程序'''
    error_number = 0
    while True:
        username = input('Please input your name: ').strip()
        if username in lock_user_list:
            print('%s is locking' % username)
            exit(1)
        elif username in user_dict.keys():
            userpasswd = input('Please input you passwd: ').strip()
            if userpasswd == user_dict[username]:
                # 通过用户名取的在字典中对应的密码，user_dict[keys]=values
                print("%s is logging succeed!" % username)
            else:
                print("Your %s password is error!" % username)
                error_number = int(error_number) + 1
                write_blocklist(error_number, username)
                # 启用黑名单程序判断
        else:
            print('%s user not found!' % username)
            error_number = int(error_number) + 1
            write_blocklist(error_number, username)

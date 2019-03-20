#--*-- coding:utf-8 --*--
# @Time   ： 2019/3/18 16:17
# @Author : Wesley
# @File   : login.py

def read_user():
    '''读取用户账号密码，测试仅支持单个用户'''
    user_dict = {}
    with open('user.db', 'r', encoding='utf-8') as read_user:
        for line in read_user:
            (username,userpasswd) = line.strip().split(':')
        user_dict[username] = userpasswd
        print(user_dict)
    return user_dict
read_user()

def read_blocklist():
    '''读取黑名单用户'''
    with open('blocklist.db','r',encoding='utf-8') as read_lock_user :
        lock_user_data = read_lock_user.read()
        return lock_user_data

def write_blocklist(username):
    '''将输入密码三次用户写入黑名单'''
    with open('blocklist.db','a',encoding='utf-8') as write_lock_user:
        write_lock_user.write('\n'+username)

def login():
    error_number = 0
    lock_user_data = read_blocklist()
    user_dict = read_user()
    while True:
        username = input('Please input your name: ').strip()
        for lock_user in lock_user_data:
            if username == lock_user.strip():
                print('%s is locking' % username)
                exit(1)
            for user in user_dict.keys():
                if username == user:
                    userpasswd = input('Please input you passwd: ').strip()
                    for passwd in user_dict.values():
                        if userpasswd == passwd:
                            print("%s is logging succeed!" % username)
                            exit(0)
                        if userpasswd != passwd:
                            print("Your %s passwd is error!" % username)
                            error_number = int(error_number) + 1
                            break
                            if error_number == 3:
                                print('Your error number is %d' % error_number)
                                write_blocklist(username)
                                exit(1)
                if username != user:
                    print('%s user not found!' % username)
                    error_number = int(error_number) + 1
                    continue
                    if error_number == 3:
                        print('Your error number is %d' % error_number)
                        write_blocklist(username)
                        exit(1)

# login()

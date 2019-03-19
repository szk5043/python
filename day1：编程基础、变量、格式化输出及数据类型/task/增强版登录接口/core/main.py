#--*-- coding:utf-8 --*--
# @Time   ： 2019/3/19 11:29
# @Author : Wesley
# @File   : main.py
def read_user():
    '''读取已注册用户'''
    user_dict = {}
    with open('db/user.db','r', encoding='utf-8') as read_user:
        for line in read_user:
            (username, userpasswd) = line.strip().split(':')
        user_dict[username] = userpasswd
    return user_dict

def read_blocklist():
    '''读取黑名单用户'''
    with open('db/blocklist.db','r',encoding='utf-8') as read_lock_user :
        lock_user_list = read_lock_user.readline().split('\n')
        return lock_user_list

def regiset_user(username,passwd):
    '''注册用户并写入user.db'''
    with open('db/user.db', 'a', encoding='utf-8') as write_user:
        write_user.write(username+':'+passwd+'\n')

def write_blocklist(input_number,username):
    '''判断用户输错次数，大于三次写入黑名单'''
    input_number = int(input_number) + 1
    if input_number == 3:
        print('Warning, your input number is %d , %s status is locked !' % (input_number,username))
        with open('db/blocklist.db', 'a', encoding='utf-8') as write_lock_user:
            write_lock_user.write('\n' + username)
            exit(1)

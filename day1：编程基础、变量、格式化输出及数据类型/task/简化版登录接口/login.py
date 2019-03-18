#--*-- coding:utf-8 --*--
# @Time   ： 2019/3/18 16:17
# @Author : Wesley
# @File   : login.py
# block_list = ['admin','root','123' ]
# user_dict = {
#     "name":"szk",
#     "passwd":"123"
# }

def read_user():
    with open('user.db','r',encoding='utf-8') as read_user:
        user_dict=dict(read_user)
        for k,v in user_dict.items():
            print(k,v)
            username = k
            userpasswd = v
            return username,userpasswd


def read_blocklist():
    with open('blocklist.db','r',encoding='utf-8') as read_lock_user :
        lock_user_data = read_lock_user.read()
        return lock_user_data

def write_blocklist(username):
    with open('blocklist.db','a',encoding='utf-8') as write_lock_user:
        write_lock_user.write('\n'+username)

def loggin():
    error_number = 0
    username,userpasswd = read_user()
    lock_user_data=read_blocklist()
    while True:
        username = input('Please input your name: ')
        if username in lock_user_data:
            print('%s is locking' % username)
            exit(1)
        elif username == user_dict["name"]:
            userpasswd = input('Please input you passwd: ')
            if userpasswd == user_dict["passwd"]:
                print("%s is logging succeed!" % username)
                exit(0)
            else:
                print("Your %s passwd is error!" % username)
                error_number = int(error_number) + 1
                if error_number == 3:
                    print('Your error number is %d' % error_number)
                    write_blocklist(username)
                    exit(1)
        else:
            print('%s user not found!' % username)
            error_number = int(error_number) + 1
            if error_number == 3:
                print('Your error number is %d' % error_number)
                write_blocklist(username)
                exit(1)

# loggin()

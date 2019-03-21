#--*-- coding:utf-8 --*--
# @Time   ： 2019/3/18 16:17
# @Author : Wesley
# @File   : bin.py

user_dict = {
    "name":"szk",
    "passwd":"123"
}

def read_blocklist():
    '''读取黑名单中的用户信息'''
    with open('blocklist.db','r',encoding='utf-8') as lock_user :
        lock_user_data = lock_user.read()
        return lock_user_data

def write_blocklist(username):
    '''将输入密码三次用户写入黑名单'''
    with open('blocklist.db','a',encoding='utf-8') as write_lock_user:
        write_lock_user.write('\n'+username)

def main():
    '''主程序'''
    error_number = 0
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

if __name__ == '__main__':
    main()
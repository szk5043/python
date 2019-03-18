#--*-- coding:utf-8 --*--
# @Time   ： 2019/3/18 17:11
# @Author : Wesley
# @File   : loggin2.py

#--*-- coding:utf-8 --*--
# @Time   ： 2019/3/18 16:17
# @Author : Wesley
# @File   : loggin.py

class loggin():
    block_list = ['admin', 'root', '123']
    user_dict = {
        "name": "szk",
        "passwd": "123"
    }
    error_number = 0

    def error_exit():
        error_number = int(error_number)+1
        if error_number == 3:
            print('Your error number is %d' %error_number)
            exit(1)

    def bin():
        error_number = 0
        while True:
            username = input('Please input your name: ')
            userpasswd = input('Please input you passwd: ')
            if username == user_dict["name"]:
                if userpasswd == user_dict["passwd"]:
                    print("%s is logging succeed!" % username)
                    exit(0)
                else:
                    print("Your %s passwd is error!" % username)
                    error_exit()
            else:
                print('%s user not found!' % username)
                error_exit()

loggin()

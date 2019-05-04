def user_read(file):
    '''读取用户信息'''
    user_dict = {}
    try:
        with open(file, 'r', encoding='utf-8') as f:
            user_list = f.readline().split(',')
            for user in user_list:
                username, userpasswd, balance = user.split('|')
                user_dict[username] = {'userpasswd': userpasswd, 'balance': int(balance)}
            return user_dict
    except ValueError:
        return user_dict


def user_write(file, user_dict):
    '''写入用户信息'''
    for k in user_dict.keys():
        username = k
        userpasswd = user_dict[username]['userpasswd']
        balance = user_dict[username]['balance']
        with open(file, 'w', encoding='utf-8') as f:
            write_data = str(username) + '|' + str(userpasswd) + '|' + str(balance) + ','
            f.write(write_data)


def user_register(file, user_dict):
    '''用户注册'''
    username = input("请输入用户名： ").strip()
    if username not in user_dict:
        userpasswd1 = input("请输入密码: ").strip()
        userpasswd2 = input("请再输入一次密码: ").strip()
        if userpasswd1 == userpasswd2:
            userpasswd = userpasswd1
            balance = 0
            if len(userpasswd) > 3:
                user_dict[username] = {'userpasswd': userpasswd, 'balance': balance}
                user_write(file, user_dict)
            else:
                print("密码不符合复杂度要求！")
        else:
            print('两次输入的密码不一致，请重新输入')
    else:
        print('用户名已经被使用，请换个试试')


def user_login(file, user_dict):
    # def user_login():
    '''用户登录'''
    count = 0
    user_login_status = {}
    while True:
        username = input("请输入用户名： ").strip()
        if username in user_dict:
            userpasswd = input("请输入密码: ").strip()
            if userpasswd == user_dict[username]['userpasswd']:
                balance = user_dict[username]['balance']
                user_login_status[username] = {'userpasswd': userpasswd, 'balance': balance}
                print('登录成功!\n')
                return user_login_status
            else:
                print('密码输入错误，请重新输入')
                count += 1
                if count == 3:
                    print('密码输错超过三次，程序退出')
                    break
        else:
            chioce = input('该用户不存在，是否注册Y/y: ')
            if chioce == 'Y' or chioce == 'y':
                user_register(file, user_dict)


def user_logout(file, user_dict, user_login_status):
    '''用户注销'''
    user_dict.update(user_login_status)
    user_write(file, user_dict)
    user_login_status = {}
    return user_login_status

#--*-- coding:utf-8 --*--
# @Time   ： 2019/4/3 13:57
# @Author : Wesley
# @File   : 作业.py

# 1.统计⽂件数据中字⺟e出现的次数(不区分⼤⼩写)
# ⽂件内容： hello friend, can you speak English!
# 结果： 4
# 分析：将⽂件内容读出，然后统计读出的字符串中字符e的个数(字符串count功能)
with open('1.txt','r',encoding='utf-8') as f:
    str_1 = f.read()
    print(str_1.lower().count('e'))

# 2.统计⽂件数据中出现的的所有字符与该字符出现的个数(不区分⼤⼩写,标点与空格也算)
# ⽂件内容： hello friend, can you speak English!
# 结果：
# {
# 'h': 1,
# 'e': 4,
# 'l': 3,
# 'o': 2,
# ' ': 5,
# ...
# }
# 分析：将⽂件内容读出，然后统计读出的字符串中每个字符的个数，形成字段(for遍历读取的字符串)
count = {}
with open('1.txt','r',encoding='utf-8') as f:
    str_1 = f.read()
    for i in str_1:
        if i not in count:
            count[i] = 1
        else:
            count[i] += 1
print(count)

# 3.读取⽂件内容，分析出所有的账号及对应的密码
# ⽂件内容： owen:123456|egon:123qwe|liuxx:000000
# 结果：
# {
# 'owen': '123456',
# 'egon': '123qwe',
# 'liuxx': '000000'
# }
# 分析：将⽂件内容读出，然后按|拆分出 账号:密码 格式的⼦字符串，再按:拆分成 账号及密码，存放到字典中
user_dict = {}
with open('2.txt','r',encoding='utf-8') as f:
    for i in f.readlines():
        list_1 = i.split('|')
        for str_1 in list_1:
            k,v = str_1.strip().split(':')
            user_dict[k] = v
print(user_dict)
# 4.在题3的基础上，账号密码已经被存储在⽂件中，完成⽤户登录成功或失败(只做⼀次性判断)
# ⽂件内容： owen:123456|egon:123qwe|liuxx:000000
# 需求：输⼊账号、密码，然后进⾏登录判断，账号密码均正确打印登录成功，否则打印登录失败
# 分析：先完成题3，分析出账号密码字典，然后拿输⼊的账号密码与字典中数据进⾏校验
def read_user_info():
    user_dict = {}
    with open('2.txt', 'r', encoding='utf-8') as f:
        for i in f.readlines():
            list_1 = i.split('|')
            for str_1 in list_1:
                k, v = str_1.strip().split(':')
                user_dict[k] = v
    return user_dict

def user_login():
    user = input("please input user name: ").strip()
    user_dict = read_user_info()
    if user in user_dict.keys():
        passwd = input("please input user password: ").strip()
        if passwd == user_dict[user]:
            print("user %s is login succeed" % user)
        else:
            print("password error!")
    else:
        print("user %s is not found!" % user)

user_login()

# 5.在题3的基础上，完成⽤户注册的功能(只做⼀次性判断)
# ⽂件内容： owen:123456|egon:123qwe|liuxx:000000
# 需求：输⼊注册的账号、密码，账号已存在的打印账号已存在，注册失败，反正打印注册成功，并将新账号密码录⼊⽂件
# 结果：如果输⼊mac、 123123 => owen:123456|egon:123qwe|liuxx:000000|mac:123123
# 分析：先完成题3，分析出账号密码字典，然后拿输⼊的注册账号与字典中数据进⾏校验，如果校验没有新账号
# -- 1.采⽤ w 模式写⽂件，可以在读取⽂件的内容后拼接 |mac:123123 字符串，将拼接后的总字符串⼀次性写⼊
# -- 2.采⽤ a 模式写⽂件，可以直接追加写⼊ |mac:123123 字符串# -------------------------------------------
def read_user_info():
    user_dict = {}
    with open('2.txt', 'r', encoding='utf-8') as f:
        for i in f.readlines():
            list_1 = i.split('|')
            for str_1 in list_1:
                k, v = str_1.strip().split(':')
                user_dict[k] = v
    return user_dict

def write_user_info(user,passwd):
    with open('2.txt', 'r', encoding='utf-8') as f_read:
        user_str = f_read.readline()
    with open('2.txt', 'w', encoding='utf-8') as f_write:
        f_write.write(user_str+'|'+user+':'+'passwd')

def user_register():
    user = input("please input register user name: ").strip()
    user_dict = read_user_info()
    if user in user_dict.keys():
        print('user %s already exist!' % user)
        exit(1)
    else:
        passwd = input("please input user password: ").strip()
        write_user_info(user,passwd)
        print('user %s is register succeed !' % user)

user_register()

# -- 2.采⽤ a 模式写⽂件
def read_user_info():
    user_dict = {}
    with open('2.txt', 'r', encoding='utf-8') as f:
        for i in f.readlines():
            list_1 = i.split('|')
            for str_1 in list_1:
                k, v = str_1.strip().split(':')
                user_dict[k] = v
    return user_dict

def write_user_info(user,passwd):
    with open('2.txt', 'a', encoding='utf-8') as f:
        f.write('|'+user+':'+'passwd')

def user_register():
    user = input("please input register user name: ").strip()
    user_dict = read_user_info()
    if user in user_dict.keys():
        print('user %s already exist!' % user)
        exit(1)
    else:
        passwd = input("please input user password: ").strip()
        write_user_info(user,passwd)
        print('user %s is register succeed !' % user)

user_register()

# 拓展1.统计⽂件中⼤写字⺟、⼩写字⺟、数字及其他字符出现的次数
# ⽂件内容： Abc123,-+XYZopq000.?/
# 结果：
# {
# '⼤写字⺟': 4,
# '⼩写字⺟': 5,
# '数字': 6,
# '其他字符': 6
# }
# 分析：利⽤ASCII表， for循环遍历每⼀个字符value， eg： 'a' <= value <= 'z'就代表是⼩写字⺟
dict_count = {'⼤写字⺟': 0,'⼩写字⺟': 0,'数字': 0,'其他字符': 0}
with open ('3.txt','r',encoding='utf-8') as f:
    for i in f.readline():
        if i.isalpha() and i.isupper():  #若是字母，且大写
            dict_count['⼤写字⺟'] += 1
        elif i.isalpha() and i.islower(): #若是字母，且小写
            dict_count['⼩写字⺟'] += 1
        elif i.isdigit():    #若是数字
            dict_count['数字'] += 1
        else:    #若都不是
            dict_count['其他字符'] += 1
print(dict_count)

# 拓展2.完成登录注册系统(从空⽂件开始做)
# 需求分析：
'''
1.可以循环登录注册，输⼊1代表选择登录功能，输⼊2代表注册功能，输⼊0代表退出，其他输⼊代表
输⼊有误，重输
2.⽤户的账号密码信息存放在usr.txt⽂件中，保证⽤户注册成功后，重启系统，⽤户信息仍然保存
3.登录在账号验证通过才输⼊密码验证登录，账号验证三次失败⾃动进⼊注册功能，登录三次验证失败
⾃动退出系统
4.第⼀次注册，⽂件写⼊ 账号:密码 信息，再次注册追加写⼊ |账号:密码 信息
分析过程：略
'''
def read_user_info():
    '''读取用户信息'''
    user_dict = {}
    with open('user.txt', 'r', encoding='utf-8') as f:
        for i in f.readlines():
            list_1 = i.split('|')
            for str_1 in list_1:
                k, v = str_1.strip().split(':')
                user_dict[k] = v
    return user_dict

def write_user_info(user_dict,user,passwd):
    '''写入用户信息'''
    with open('user.txt', 'a', encoding='utf-8') as f:
        if user_dict:
            f.write('|'+user+':'+'passwd')
        elif not user_dict:
            f.write(user + ':' + 'passwd')

def user_register(user_dict):
    '''用户注册'''
    user = input("please input register user name: ").strip()
    if user in user_dict.keys():
        print('user %s already exist!' % user)
        exit(1)
    else:
        passwd = input("please input user password: ").strip()
        write_user_info(user_dict,user,passwd)
        print('user %s is register succeed !' % user)
        exit(0)

def user_login(user_dict):
    '''用户登陆'''
    count = 0
    while True:
        user = input("please input user name: ").strip()
        if user in user_dict.keys():
            passwd = input("please input user password: ").strip()
            if passwd == user_dict[user]:
                print("user %s is login succeed" % user)
            else:
                print("password error!")
                count += 1
                if count == 3:
                    exit(1)
        else:
            print("user %s is not found!" % user)
            count += 1
            if count == 3:
                user_register(user_dict)

def main():
    '''主程序'''
    user_dict = read_user_info()
    print(user_dict)
    # 获取已注册用户信息
    menu = '''Usage:
 1 : user login
 2 : regiset new user 
 0 : quit'''
    while True:
        print(menu)
        choice = input('Input :').strip()
        if choice == "1":
            user_login(user_dict)
            # 登录用户
        elif choice == "2":
            user_register(user_dict)
            # 注册用户
        elif choice == "0":
            exit(0)
        else:
            print(menu)

if __name__ == '__main__':
    main()
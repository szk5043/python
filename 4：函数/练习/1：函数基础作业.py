# 1.定义⼀个函数，该函数可以实现控制台输⼊，最终返回⼀个int类型的正整数
# 解析：如何将字符串转换为int类型的正整数

def intput_int():
    while True:
        int_num = input("please input number: ").strip()
        if not int_num.isdigit():
            print("error , please input number!\n")
        else:
            return int_num

res = intput_int()
print(res)

# 2.定义⼀个函数，该函数可以实现⽤户录⼊，最终返回⼀个int类型的负整数
# 解析： 1.只能有⼀个'-'且以它开头； 2.按'-'拆分得到的⼀定是⻓度为2的列表，且后⾯的数是正整数
def input_int():
    while True:
        num = input("please input number: ").strip()
        if num.isalpha():
            #判断是否为字母
            print("error , please input number!\n")
        elif num.isdigit():
            #判断是否为数字
            num = '-'+str(num)
            return int(num)
        elif num.startswith('-') and num.count('-') == 1:
            # 判断是否为负数
            inside_num = num.replace('-','')
            if not inside_num.isdigit():
                print("error , please input number!\n")
            else:
                return num
        else:
            #特殊符号在这儿
            print("error , please input number!\n")

print(input_int())


# 3.定义⼀个函数，实现传⼊⼀个数或是字符串，返回值是 是否 是可转换为整数类型的数据
# 解析：运⽤1， 2的逻辑判断
def input_int(num):
    while True:
        num = str(num)
        if num.isalpha():
            #判断是否为字母
            return False
        elif num.isdigit():
            #判断是否为数字
            return True
        elif num.startswith('-') and num.count('-') == 1:
            # 判断是否为负数
            inside_num = num.replace('-','')
            if not inside_num.isdigit():
                return False
            else:
                return True
        else:
            #特殊符号在这儿
            return False
print(input_int('23'))

# 4.定义⼀个函数，实现传⼊⼀个整型数字，判断并直接打印该数字是否是奇数还是偶数
# 解析：解决奇数、偶数的概念即可
def input_int(num):
    if isinstance(num,int):
        if num % 2 == 1:
            print("奇数")
        else:
            print("偶数")
    else:
        print("plase input a num!")

input_int(1)

# 5.定义⼀个函数，实现判断传⼊数据的类型，并直接打印其类型
# 解析：如何判断数据的类型
type_map = {
    'int': '整型',
    'str': '字符串',
    'float': '浮点型',
    'complex': '复数',
    'list': '列表',
    'dict': '字典',
    'set': '集合',
    'tuple': '元组',
    'bool':'布尔值',
}

def data_type(data):
    if isinstance(data,int):
        print(type_map['int'])
    elif isinstance(data,str):
        print(type_map['str'])
    elif isinstance(data,float):
        print(type_map['float'])
    elif isinstance(data,complex):
        print(type_map['complex'])
    elif isinstance(data,list):
        print(type_map['list'])
    elif isinstance(data,dict):
        print(type_map['dict'])
    elif isinstance(data,set):
        print(type_map['set'])
    elif isinstance(data,tuple):
        print(type_map['tuple'])
    elif isinstance(data,bool):
        print(type_map['bool'])
    else:
        print("unkonw data type!")

ls = [1, '1', 3.14, True, [], {}, {1,}, (1,), 4+5j]
for v in ls:
    data_type(v)

# 6.定义⼀个函数，实现可以重复录⼊键盘信息，当⽤户输⼊q或Q时退出，否则判断是否为可转换为整数类型的数据，可以的话输出该数是奇数还是偶数，否则直接输出该字符串
# 解析：要调⽤3， 4题结果
def input_int():
    while True:
        data= input("plase input data: ").strip()
        data = str(data)
        if data == 'Q' or data == 'q':
            print("exit...")
            break
        elif data.isalpha():
            #判断是否为字母
            print(data)
        elif data.isdigit():
            #判断是否为数字
            data = int(data)
            if data % 2 == 1:
                print("奇数")
            else:
                print("偶数")
        else:
            #特殊符号在这儿
            print(data)
print(input_int())

# 7.定义⼀个函数，只要传⼊ "k1:v1,...,kn:vn" 格式的字符串，都可以将其转换为{'k1':'v1',...,'kn':'vn'}
# 解析：字符串拆分与for循环迭代
def str_to_dic(data):
    dic = {}
    data_list = data.split(',')
    for line in data_list:
        k,v = line.strip().split(':')
        dic[k] = v
        return dic

data = "name:szk"
print(str_to_dic(data))

# 8.定义⼀个函数，实现列表与元组类型的反转功能
# 解析：传⼊列表返回元组，传⼊元组返回列表
def data_reverse(data):
    if isinstance(data,tuple):
        data = list(data)
        return data
    elif isinstance(data,list):
        data = tuple(data)
        return data
    else:
        print("unkone data type!")

data1 = [1,2,3]
data2 = (1,2,3)

print(data_reverse(data1))
print(data_reverse(data2))

# 9.定义⼀个函数，可以完成对list、 tuple、 dict、 set四种类型数据的循环变量打印，不是这四种，则打印 "暂不⽀持该数据遍历"
# 解析：对数据类型做判断
def for_data(data):
    if isinstance(data,list) or isinstance(data,tuple) or isinstance(data,dict) or isinstance(data,set):
        for i in data:
            print(i)
    else:
        print("暂不⽀持该数据遍历")

data1 = [1,2,3]
data2 = (1,2,3)
data3 = {"name":'szk'}
for_data(data1)
for_data(data2)
for_data(data3)

# 10.定义⼀个函数，实现对单列集合进⾏去重的功能
# 解析：单列集合有list、 tuple、 set，传⼊list、 tuple、 set，返回去重后的list、 tuple、set，考虑可变与不可变类型的不同处理
def clear_data(data):
    list_1 = []
    if isinstance(data,list):
        for i in data:
            if i not in list_1:
                list_1.append(i)
        return list_1
    elif isinstance(data,tuple):
        for i in data:
            if i not in list_1:
                list_1.append(i)
        return tuple(list_1)
    elif isinstance(data,set):
        for i in data:
            if i not in list_1:
                list_1.append(i)
        return set(list_1)

data1 = [1,2,2,3]
data2 = (1,2,2,3)
data3 = {1,2,3,3}
print(clear_data(data1))
print(clear_data(data2))
print(clear_data(data3))

# 11.定义⼀个函数，实现⽂件(不⼀定是⽂本⽂件)的跨⽂件夹的裁剪
# 解析： 1.传⼊要读取的⽬标⽂件夹中的⽬标⽂件;2.在被告知的⽬标⽂件夹下复制成同名⽂件； 3.调⽤os中删除⽂件的功能将原⽂件删除
import os

def move_file(file,des_path):
    filename = file.rsplit('/',1)[1]
    des_full_path = des_path+'/'+filename
    with open(file, 'r', encoding='utf-8') as f, \
            open(des_full_path, 'w', encoding='utf-8') as f_new:
        for line in f:
            f_new.write(line)

    os.remove(file)

move_file('/Users/zhengkaishen/PycharmProjects/untitled/int.py','/Users/zhengkaishen/PycharmProjects/untitled/day4')

# 拓展1：⽤函数实现判断⼀个字符串数据能否转换为正负⼩数
# 先考虑正⼩数，再在基础上考虑负⼩数，可以形成多个⽅法，形成函数的嵌套
# 正⼩数：只包含⼀个⼩数点，左右都是正整数
# 负⼩数：参考普通题的第2题结合正⼩数
def is_float(str_list):
    '''判断是否为小数'''
    if len(str_list) == 2 and str_list[1].isdigit():
        return True
    return False

def data_type(data):
    '''判断输入的数据类型'''
    if isinstance(data,str):
        str_list = data.split('.')
        if not str_list[0].startswith('-'):
            '''如果是正小数'''
            res = is_float(str_list)
        elif str_list[0].startswith('-'):
            '''如果是负小数'''
            res = is_float(str_list)
    else:
        print("数据类型错误")
    return res

print(data_type('0.1'))

# 拓展2：实现汽⻋销售系统
'''
1）具有进货功能1，销售⻋辆功能2，展示所有库存功能3，展示销售总业绩功能4
2）⽤户输⼊0退出系统，输⼊提供的功能编号，完成对应的功能，否则重新输⼊， eg： 2就进⼊销售⻋
功能
3）⻋辆信息具有持久化(⽂件永久)存储功能，⻋辆有奔驰|宝⻢|奥迪三款
⽂件信息：
total.txt: 就是记录了总销售额
car.txt:
宝⻢ 120000 9
奔驰 150000 7
奥迪 100000 8
4）进货功能：选择进货的⻋型与数量，完成进货
5）售⻋功能：选择售出的⻋，有库存售出，更新销售总业绩，没有则进⼊进货功能
6）展示库存：显示所有⻋与库存两条信息即可
7）总业绩：显示总业绩⾦额即可
分析：要将total.txt与car.txt转换为合适的数据类型，操作完毕后同步到⽂件中即可
'''
import os
car_type = {
    '1': "奥迪",
    '2': "宝马",
    '3': "奔驰",
}

def read_car():
    '''读取库存信息'''
    car_database = {}
    with open('car.txt', 'r', encoding='utf-8') as read:
        for i in read:
            car, price, num = i.strip().split(' ')
            car_database[car] = {'price': int(price), 'num': int(num)}
        return car_database

def write_car(car_database):
    '''写入库存信息'''
    for car,car_info in car_database.items():
        price = car_database[car]['price']
        num = car_database[car]['num']
        write_data = str(car) + ' ' + str(price) + ' ' + str(num) + '\n'
        with open ('car.txt.swap','a',encoding='utf-8') as write:
             write.write(write_data)
    os.remove('car.txt')
    os.rename('car.txt.swap','car.txt')

def read_total():
    '''读取销售额'''
    with open('total.txt', 'r', encoding='utf-8') as read:
        total = read.readline().strip('\n')
        if not total:
            total = 0
        return int(total)

def  write_total(total):
    '''写入销售额'''
    with open('total.txt', 'w', encoding='utf-8') as write:
        write.write(total)

def buy_car():
    '''进货'''
    while True:
        print(car_type)
        car_type_num = input("请输入要进货的车型对应的编号,Q/q退出： ").strip()
        if car_type_num == 'q' or car_type == 'Q': break
        num = input("请输入要进货的车型数量： ").strip()
        car = car_type[car_type_num]
        car_database = read_car()
        car_database[car]['num'] = car_database[car]['num'] + int(num)
        write_car(car_database)

def shopping_car():
    '''销售'''
    print(car_type)
    car_database = read_car()
    total = read_total()
    num = input("请输入要购买的汽车编号：").strip()
    if num in car_type.keys():
        car = car_type[num]
        price = car_database[car]['price']
        res = input("%s 需要 %d 元，确认购买y/Y: " % (car, price)).strip()
        if res == 'y' or res == 'Y':
            # 销售业绩增加，并写入
            total += int(price)
            write_total(str(total))
            # 汽车库存减少，并写入
            car_database[car]['num'] -= 1
            write_car(car_database)
            print("%s 购买成功！！！" %car)
    else:
        print("您所要的汽车太高端了，小店没有！")

def inventory_car():
    '''库存'''
    car_database = read_car()
    for k in car_database:
        print(k, ':', car_database[k]['num'])

def sale_car():
    '''销售额'''
    total = read_total()
    print(total)

def main():
    dict_map = {
        '1': buy_car,
        '2': shopping_car,
        '3': inventory_car,
        '4': sale_car,
    }
    while True:
        num = input('''
1:进货功能
2:销售车辆功能
3:展示所有库存功能
4:展示销售业绩
0:退出
Please input num: ''').strip()
        if num in dict_map:
            dict_map[num]()
        elif num == '0':
            break

if __name__ == "__main__":
    main()

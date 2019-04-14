# 1.定义⼀个函数，该函数可以实现控制台输⼊，最终返回⼀个int类型的正整数
# 解析：如何将字符串转换为int类型的正整数

# def intput_int():
#     while True:
#         int_num = input("please input number: ").strip()
#         if not int_num.isdigit():
#             print("error , please input number!\n")
#         else:
#             return int_num
#
# res = intput_int()
# print(res)

# 2.定义⼀个函数，该函数可以实现⽤户录⼊，最终返回⼀个int类型的负整数
# 解析： 1.只能有⼀个'-'且以它开头； 2.按'-'拆分得到的⼀定是⻓度为2的列表，且后⾯的数是正整数
# def input_int():
#     while True:
#         num = input("please input number: ").strip()
#         if num.isalpha():
#             #判断是否为字母
#             print("error , please input number!\n")
#         elif num.isdigit():
#             #判断是否为数字
#             num = '-'+str(num)
#             return int(num)
#         elif num.startswith('-') and num.count('-') == 1:
#             # 判断是否为负数
#             inside_num = num.replace('-','')
#             if not inside_num.isdigit():
#                 print("error , please input number!\n")
#             else:
#                 return num
#         else:
#             #特殊符号在这儿
#             print("error , please input number!\n")
#
# print(input_int())


# 3.定义⼀个函数，实现传⼊⼀个数或是字符串，返回值是 是否 是可转换为整数类型的数据
# 解析：运⽤1， 2的逻辑判断
# def input_int(num):
#     while True:
#         num = str(num)
#         if num.isalpha():
#             #判断是否为字母
#             return False
#         elif num.isdigit():
#             #判断是否为数字
#             return True
#         elif num.startswith('-') and num.count('-') == 1:
#             # 判断是否为负数
#             inside_num = num.replace('-','')
#             if not inside_num.isdigit():
#                 return False
#             else:
#                 return True
#         else:
#             #特殊符号在这儿
#             return False
# print(input_int('23'))

# 4.定义⼀个函数，实现传⼊⼀个整型数字，判断并直接打印该数字是否是奇数还是偶数
# 解析：解决奇数、偶数的概念即可
# def input_int(num):
#     if isinstance(num,int):
#         if num % 2 == 1:
#             print("奇数")
#         else:
#             print("偶数")
#     else:
#         print("plase input a num!")
#
# input_int(1)

# 5.定义⼀个函数，实现判断传⼊数据的类型，并直接打印其类型
# 解析：如何判断数据的类型
# type_map = {
#     'int': '整型',
#     'str': '字符串',
#     'float': '浮点型',
#     'complex': '复数',
#     'list': '列表',
#     'dict': '字典',
#     'set': '集合',
#     'tuple': '元组',
#     'bool':'布尔值',
# }
#
# def data_type(data):
#     if isinstance(data,int):
#         print(type_map['int'])
#     elif isinstance(data,str):
#         print(type_map['str'])
#     elif isinstance(data,float):
#         print(type_map['float'])
#     elif isinstance(data,complex):
#         print(type_map['complex'])
#     elif isinstance(data,list):
#         print(type_map['list'])
#     elif isinstance(data,dict):
#         print(type_map['dict'])
#     elif isinstance(data,set):
#         print(type_map['set'])
#     elif isinstance(data,tuple):
#         print(type_map['tuple'])
#     elif isinstance(data,bool):
#         print(type_map['bool'])
#     else:
#         print("unkonw data type!")
#
# ls = [1, '1', 3.14, True, [], {}, {1,}, (1,), 4+5j]
# for v in ls:
#     data_type(v)

# 6.定义⼀个函数，实现可以重复录⼊键盘信息，当⽤户输⼊q或Q时退出，否则判断是否为可转换为整数类型的数据，可以的话输出该数是奇数还是偶数，否则直接输出该字符串
# 解析：要调⽤3， 4题结果
# def input_int():
#     while True:
#         data= input("plase input data: ").strip()
#         data = str(data)
#         if data == 'Q' or data == 'q':
#             print("exit...")
#             break
#         elif data.isalpha():
#             #判断是否为字母
#             print(data)
#         elif data.isdigit():
#             #判断是否为数字
#             data = int(data)
#             if data % 2 == 1:
#                 print("奇数")
#             else:
#                 print("偶数")
#         else:
#             #特殊符号在这儿
#             print(data)
# print(input_int())

# 7.定义⼀个函数，只要传⼊ "k1:v1,...,kn:vn" 格式的字符串，都可以将其转换为{'k1':'v1',...,'kn':'vn'}
# 解析：字符串拆分与for循环迭代
# def str_to_dic(data):
#     dic = {}
#     data_list = data.split(',')
#     for line in data_list:
#         k,v = line.strip().split(':')
#         dic[k] = v
#         return dic
#
# data = "name:szk"
# print(str_to_dic(data))

# 8.定义⼀个函数，实现列表与元组类型的反转功能
# 解析：传⼊列表返回元组，传⼊元组返回列表
# def data_reverse(data):
#     if isinstance(data,tuple):
#         data = list(data)
#         return data
#     elif isinstance(data,list):
#         data = tuple(data)
#         return data
#     else:
#         print("unkone data type!")
#
# data1 = [1,2,3]
# data2 = (1,2,3)
#
# print(data_reverse(data1))
# print(data_reverse(data2))

# 9.定义⼀个函数，可以完成对list、 tuple、 dict、 set四种类型数据的循环变量打印，不是这四种，则打印 "暂不⽀持该数据遍历"
# 解析：对数据类型做判断
# def for_data(data):
#     if isinstance(data,list) or isinstance(data,tuple) or isinstance(data,dict) or isinstance(data,set):
#         for i in data:
#             print(i)
#     else:
#         print("暂不⽀持该数据遍历")
#
# data1 = [1,2,3]
# data2 = (1,2,3)
# data3 = {"name":'szk'}
# for_data(data1)
# for_data(data2)
# for_data(data3)

# 10.定义⼀个函数，实现对单列集合进⾏去重的功能
# 解析：单列集合有list、 tuple、 set，传⼊list、 tuple、 set，返回去重后的list、 tuple、set，考虑可变与不可变类型的不同处理
# def clear_data(data):
#     list_1 = []
#     if isinstance(data,list):
#         for i in data:
#             if i not in list_1:
#                 list_1.append(i)
#         return list_1
#     elif isinstance(data,tuple):
#         for i in data:
#             if i not in list_1:
#                 list_1.append(i)
#         return tuple(list_1)
#     elif isinstance(data,set):
#         for i in data:
#             if i not in list_1:
#                 list_1.append(i)
#         return set(list_1)
#
# data1 = [1,2,2,3]
# data2 = (1,2,2,3)
# data3 = {1,2,3,3}
# print(clear_data(data1))
# print(clear_data(data2))
# print(clear_data(data3))

# 11.定义⼀个函数，实现⽂件(不⼀定是⽂本⽂件)的跨⽂件夹的裁剪
# 解析： 1.传⼊要读取的⽬标⽂件夹中的⽬标⽂件;2.在被告知的⽬标⽂件夹下复制成同名⽂件； 3.调⽤os中删除⽂件的功能将原⽂件删除
# import os
#
# def move_file(file,des_path):
#     filename = file.rsplit('/',1)[1]
#     des_full_path = des_path+'/'+filename
#     with open(file, 'r', encoding='utf-8') as f, \
#             open(des_full_path, 'w', encoding='utf-8') as f_new:
#         for line in f:
#             f_new.write(line)
#
#     os.remove(file)
#
# move_file('/Users/zhengkaishen/PycharmProjects/untitled/int.py','/Users/zhengkaishen/PycharmProjects/untitled/day4')

# 拓展1：⽤函数实现判断⼀个字符串数据能否转换为正负⼩数
# 先考虑正⼩数，再在基础上考虑负⼩数，可以形成多个⽅法，形成函数的嵌套
# 正⼩数：只包含⼀个⼩数点，左右都是正整数
# 负⼩数：参考普通题的第2题结合正⼩数
def data_type(data):
    '''判断输入的数据类型'''
    if isinstance(data,str):
        pass
    else:
        print("数据类型错误")

def is_l_float():
    '''判断正小数类型'''
    pass

def is_r_float():
    '''判断负小数类型'''
    pass


#--*-- coding:utf-8 --*--
# @Time   ： 2019/3/28 16:05
# @Author : Wesley
# @File   : 作业.py

# 1.统计元组中所有数据属于字符串的个数
t1 = (1, 2, '3', '4', 5, '6')
number=0
for i in t1:
    if isinstance(i,str):
        number += 1
print(number)

# 2.将以下数据存储为字典类型
# 数据：info = "name:Owen|age:18|gender:男"
# 结果：{'name': 'Owen', 'age': 18, 'gender': '男'}
# 注：年龄存储为数字类型
info = "name:Owen|age:18|gender:男"
dict_1 = {}
data= info.split('|')
for y in data:
   k,v  = y.split(':')
   if v.isdigit():
       v = int(v)
   dict_1[k] = v
print(dict_1)

# 3.完成数据的去重
# 数据：t3 = (1, 2, 1, 2, 3, 5, 9)
# 结果：t3 = (1, 2, 3, 5, 9)
# 注：从不考虑顺序、考虑顺序两方面完成
t3 = (1, 2, 1, 2, 3, 5, 9)
list_1 = []
for i in t3:
    if i not in list_1:
        list_1.append(i)
        list_1.sort()   #增加排序
t3 = tuple(list_1)
print(t3)

# 4.计算元组中所有可以转换为数字的数据的总和
# 数据：t4 = (10, 'abc', '100', '3')
# 运算结果：113
t4 = (10, 'abc', '100', '3')
list_2 = []
for i in t4:
    if isinstance(i, int):
        list_2.append(i)
    elif isinstance(i ,str):
        if i.isdigit():
            list_2.append(int(i))
print(sum(list_2))

# 5.将数据转换类型存储
# 原数据：dic = {'name': 'Owen', 'age': 18, 'gender': '男'}
# 处理后：info = [('name', 'Owen'), ('age', 18), ('gender', '男')]
dic = {'name': 'Owen', 'age': 18, 'gender': '男'}
info = []
for k,v in dic.items():
    info.append((k,v))
print(info)

# 拓展：选做
# 1.计算元组中所有可以转换为数字的数据的总和
# 数据：t4 = (10, 'abc', '100', '3', '壹', '肆', [1000], (10000,))
# 运算结果：11118
# 提示：
#   -- 利用字符串isnumeric()判断汉字
# 	-- 利用字典{'壹': 1 ...}将汉字转换为数字
#	-- 利用isinstance()将list和tuple中数据取出来
#	-- 先将所有转化为数字的数据存放在一个单列集合中，在做运算
t4 = (10, 'abc', '100', '3', '壹', '肆', [1000], (10000,))
number_dict = {'壹': 1,'贰': 2,'叁': 3,'肆': 4,'伍': 5,'陆': 6,'柒': 7,'捌': 8,'玖': 9,'拾': 10}
list_1 = []
for i in t4:
    if str(i).isdigit():
        list_1.append(int(i))
    elif isinstance(i,list) or isinstance(i,tuple):
        for x in i:
            list_1.append(int(x))
    elif i.isnumeric():
        list_1.append(number_dict[i])
print(sum(list_1))

# 2.完成录入电话本
# 需求：
'''
-- 从键盘中录入姓名(不区分大小写)：
	-- 姓名必须是全英文组成，不是则重新录入姓名，如果是q，代表退出
-- 从键盘中再录入电话：
	-- 电话必须为数字且长度必须是11位(不能转换为数字)
-- 如果出现姓名相同，则保留最后一次电话号码
-- 形成的数据是有电话分组的，如：第一次录入Owen，13355667788，则会形成
	-- {
    	'O': {
    		'Owen': '13355667788'
    	}
	}

最终数据，分组名一定大写：
{
    'E': {
		'egon': '17788990000',
		'engo': '16633445566'
    },
    'O': {
    	'Owen': '13355667788'
    }
}
'''
phone_dict = {}
while True:
    name = input("Please input name: ").strip()
    if name == 'q':
        break
    if name.isalpha():
        phone_group = name[0:1].upper()
        phone_dict.setdefault(phone_group, {})
        phone_number = input("Please input phone number: ").strip()
        if len(phone_number) == 11 and phone_number.isdigit():
            phone_dict[phone_group][name] = phone_number
            name = ''
            phone_number = ''
            print('phone is save! ')
        else:
            name = ''
            print("phone number is error")
print(phone_dict)
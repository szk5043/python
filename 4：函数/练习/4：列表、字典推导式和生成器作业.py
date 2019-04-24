#--*-- coding:utf-8 --*--
# @Time   ： 2019/4/24 9:08
# @Author : Wesley
# @File   : 4：列表、字典推导式和生成器作业.py

# 1、利用字典推导式和列表推导式完成数据的相互转化：
dic = {'name': 'Owen', 'age': 18, 'gender': '男'}
ls = [('name', 'Owen'), ('age', 18), ('gender', '男')]
ls1 = [ v for v in dic.items() ]
print(ls1)
dic1 = { k:v for k,v in ls }
print(dic1)

# 2、写出for迭代器迭代字符串、列表、元组、集合、字典(三种情况)的代码实现
# 字符串
for i in 'abc'.__iter__():
    print(i)

# 列表
for i in [1,2,3].__iter__():
    print(i)

# 元组
for i in (1,2,3).__iter__():
    print(i)

# 集合
for i in {1,2,3}.__iter__():
    print(i)

# 字典：示例1
for i in {'a':1}.__iter__():
    print(i)
# 字典：示例2
dic_box = {'a':1}.__iter__()
while True:
    try:
        print(dic_box.__next__())
    except StopIteration:
        print("over...")
        break
# 字典：示例3
for v in {'a':1}:
     print(v)
# 3、用生成器实现可以无限取值的生成器对象，第一次取值得到1，第二次取值得到3，第三次取值得到6，第四次取值得到10，依次类推
def fn2():
    total = 1
    count = 2
    while True:
        total += count
        yield total
        count += 1

obj =fn2()
print(obj.__next__())
print(obj.__next__())
print(obj.__next__())
print(obj.__next__())
print(obj.__next__())

# 4、利用枚举enumerate为迭代字符串、列表、元组、集合、字典(三种情况)的对象提供迭代索引
def my_enumerate(object):
    if isinstance(object,str) or isinstance(object,list) or isinstance(object,tuple) or isinstance(object,set):
        for i,v in enumerate(object):
            print(i,v)
    elif isinstance(object,dict):
        for i,k in enumerate(object.keys()):
            print(i,k)

str1 = 'abc'
list1 = [1,2,3]
tuple1 = (1,2,3)
set1 = {1,2,3}
dict1 = {'a':1,'b':2,'c':3}
my_enumerate(str1)
my_enumerate(list1)
my_enumerate(tuple1)
my_enumerate(set1)
my_enumerate(dict1)

# 5、利用递归完成斐波那契数列案例：1、1、2、3、5、8、13、21、34、55、89、144、233
# 	初始1只兔子，1个月成熟，次月往后每月可以生出1只，每只兔子成熟后都具有繁殖能力，问一年半后一共有多少只兔子
# 1 + 1 + ... 18
# 1 + 1 + ... 17
# 1 + 1 + ... 16

def get_rabbit(month,rabbit=1):
    if month == 1 or month == 2:
        return rabbit
    rabbit = get_rabbit(month - 1,rabbit) + get_rabbit(month - 2,rabbit)
    return rabbit

print(get_rabbit(18))
# 6、{'Owen': (1, 13366778899, 88888), 'Zero': (2, 18855446789, 66666), 'Egon': (3, 13000668899, 77777)}
# 借助内置函数：
# 	1）求薪资最高人的名字
# 	2）求薪资最低人的电话
# 	3）按薪资进行排序
dic = {'Owen': (1, 13366778899, 88888), 'Zero': (2, 18855446789, 66666), 'Egon': (3, 13000668899, 77777)}

res = sorted(dic,key=lambda k:dic[k][2],reverse=True)
print(res[0])   #求薪资最高人的名字

res = sorted(dic,key=lambda k:dic[k][2],reverse=False)
print(dic[res[0]][1])   #求薪资最低人的电话

res = sorted(dic,key=lambda k:dic[k][2],reverse=True)
for k in res:
    print(k,dic[k][2])   # 按薪资进行排序

# 7、利用map函数完成成绩映射
#   [58, 78, 98] => ['不通过', '通过', '通过']
# 	用到匿名函数，匿名函数的返回值用三元运算符处理
res = map(lambda x: "通过"if x > 60 else "不通过" ,[58, 78, 98])
print(list(res))

# 8、利用reduce求[58, 78, 98]的总成绩
from functools import reduce
res = reduce(lambda x,y : x + y ,[58, 78, 98])
print(res)
# 9、打印数字128的二进制、八进制、十六进制数
print(bin(128))
print(oct(128))
print(hex(128))
#10、解决第7题求总成绩还可以用什么内置函数，输出13的7次幂的结果用什么内置函数，判断一个变量是否是函数对象的内置函数，原义字符串的内置函数
print(sum([58, 78, 98]))
print(pow(13,7))
def fn():pass
print(callable(fn))
print(repr('a\nb'))
# 拓展题：
# 1、用生成器完成自定义的my_range方法，可以实现和range类似的功能：
# 	my_range(5) => 能迭代出0，1，2，3，4
# 	my_range(5, 10) => 能迭代出5，6，7，8，9
# 	my_range(5, 10，2) => 能迭代出5，7，9
# 	my_range(10, 5, -2) => 能迭代出10, 8, 6
# 	my_range(10, 5) => 没结果
# 	my_range(5, 10, -1) => 没结果

def my_range(start,end=None,step=1):
    if end is None:
        start,end = 0,start
    count = start
    while True:
        b1 = count >= end and step > 0
        b2 = count <= end and step < 0
        if b1 or b2:
            break
        yield count
        count += step

for i in my_range(10,5,-2):
    print(i)
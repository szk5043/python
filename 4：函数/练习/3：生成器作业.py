#--*-- coding:utf-8 --*--
# @Time   ： 2019/4/19 10:00
# @Author : Wesley
# @File   : 3：生成器作业.py

'''
1.⽤⽣成器完成⾃定义range⽅法，可以完成系统range的所有功能
  - 一个参数时，返回0到这个参数
'''
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

for i in my_range(30,20,-2):
    print(i)
'''
2.⽤⽣成器完成⾃定义enumerate⽅法，也可以为可迭代对象提供索引⽀持
不判断，和系统⼀样，传⾮迭代对象抛异常
enumerate多用于在for循环中得到计数，利用它可以同时获得索引和值，即需要index和value值的时候可以使用enumerate
'''
list = [1,2,3,4,5]
def my_enumerate(iterable,start=0):
    for v in iterable:
        yield (start,v)
        start += 1


obj = my_enumerate(list)
print(obj.__next__())
print(obj.__next__())
print(obj.__next__())

'''
# 3.⽤⽣成器完成获取阶乘得⽅法，第⼀次next得到1的阶乘，第⼆次next得到2的阶乘，依次类推，
直接for循环，可以依次得到指定范围内得所有阶乘， eg： factorial(10)，可以得到1~10之间的10个阶乘
'''
def factorial(num):
    x = 1
    for i in range(1,num + 1):
        x *= i
        yield x

for i in factorial(10):
    print(i)

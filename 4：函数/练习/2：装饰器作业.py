#--*-- coding:utf-8 --*--
# @Time   ： 2019/4/15 16:36
# @Author : Wesley
# @File   : 2：装饰器作业.py

# 1.写出完整的装饰器(不⽤考虑带参装饰器，就是普通装饰器)语法
def outer(func):
    def inner(*args,**kwargs):
        pass
        res = func(*args,**kwargs)
        pass
        return res
    return inner

# 2.有⼀个计算两个数和的⽅法，为其添加⼀个确保两个参数都是int或float类型的装饰器，保证运算不会抛异常
def is_int_float(func):
    def inner(*args,**kwargs):
        num_1 = args[0]
        num_2 = args[1]
        if isinstance(num_1,int) and isinstance(num_2,int):
            res = func(*args, **kwargs)
            return res
        elif isinstance(num_1,float) and isinstance(num_2,float):
            res = func(*args, **kwargs)
            return res
        return "非int或float类型"
    return inner

@is_int_float
def add(x,y):
    return x+y

res = add([],{})
print(res)

# 3.有⼀个⼀次性录⼊⼈名并返回⼈名的⽅法(⼈名只考虑存英⽂)，为其添加⼀个装饰器，使得处理后⼈名⾸字⺟⼀定⼤写

def name_startwith(func):
    def inner():
        res = func()
        return res.capitalize()
    return inner

@name_startwith
def input_name():
    name = input("please input name: ").strip()
    if name.isalpha():
        return name

print(input_name())

'''
拓展题：1.原功能： entry_grade
*) 可以完成『成绩录⼊功能』
-- 可以重复录⼊成绩，默认所有输⼊都是合法的(1~100之间的数)
-- 当录⼊成绩为0时，结束成绩的录⼊
-- 将录⼊的成绩保存在列表中并返回给外界， eg： [90, 80, 50, 70]
2.选择课程装饰器： choose_course
*) 为『成绩录⼊功能』新增选择课程的拓展功能，达到可以录⼊不同学科的成绩
-- 可以重复输⼊要录制的学科名，然后就可以进⼊该⻔学科的『成绩录⼊功能』，录⼊结束后，
可以进⼊下⼀⻔学科成绩录⼊
-- 当输⼊学科名为q时，结束所有录⼊⼯作
-- 将学科成绩保存在字典中并返回给外界， eg： {'math':[90, 80, 50, 70], 'english':
[70, 50, 55, 90]}
3.处理成绩装饰器： deal_fail
*) 可以将所有录⼊的成绩按60分为分⽔岭，转换为 "通过" | "不通过" 进⾏存储
-- 如果只对原功能装饰，结果还为list返回给外界， eg： ["通过", "通过", "不通过", "通
过"]
-- 如果对已被选择课程装饰器装饰了的原功能再装饰，结果就为dict返回给外界， eg：
{'math':["通过", "通过", "不通过", "通过"], 'english':["通过", "不通过", "不通过",
"通过"]}
'''
def deal_fail(func):
    '''处理成绩装饰器'''
    def inner():
        res = func()
        name,subject_str = res.split(':',1)
        subject_dict = eval(subject_str)
        for subject,grade_list in subject_dict.items():
            for i,grade in enumerate(grade_list):
                if grade < 60:
                    subject_dict[subject][i] = '不通过'
                else:
                    subject_dict[subject][i] = '通过'
        res = name + ': ' + str(subject_dict)
        return res
    return inner

def choose_course(func):
    '''选择课程装饰器'''
    def inner():
        subject_dict = {}
        while True:
            subject = input("Plase input your subject: ").strip()
            if subject == 'q' or subject == 'Q':
                break
            res = func()
            name,grade_list = res.split(':')
            # grade_list [100, 90]
            subject_dict[subject] = list(eval(grade_list))
            continue
        res = name+': '+ str(subject_dict)
        return res
    return inner

@deal_fail
@choose_course
def entry_grade():
    '''成绩录⼊'''
    grade_list = []
    while True:
        name = input("please input your name: ").strip()
        grade = input("please input your grade: ").strip()
        if grade.isdigit():
            if int(grade) > 0 and int(grade) <= 100:
                grade_list.append(int(grade))
                continue
            elif int(grade) == 0:
                break
        else:
            print("请输入0-100有效数字！")
    grade_data = "%s: " % name + str(grade_list)
    return grade_data

res = entry_grade()
print(res)


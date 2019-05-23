#--*-- coding:utf-8 --*--
# @Time   ： 2019/5/21 10:25
# @Author : Wesley
# @File   : day9作业.py

'''基础
1.自定义一个 Fruit 类：该类有一个 类属性: identify：值为"水果"，有两个对象属性: name，price：值由实例化对象时赋值，
一个类方法: get_identify：打印类属性identify的值，
一个对象方法：get_total_price(num)：打印『%s个%s值%s钱』，
一个静态方法：packing(*fruits)
	静态方法(装箱)的思路分析
	red_apple = Fruit("红苹果", 10)
	green_apple = Fruit("青苹果", 10)
	yellow_banana = Fruit("黄香蕉", 8)
	调用：Frulit.packing(red_apple, green_apple, yellow_banana) 打印：一箱装了2个苹果1个香蕉
'''
# class Fruit(object):
#
#     identify = "水果"   #类属性
#
#     def __init__(self,name,price):
#         '''两个对对象属性'''
#         self.name = name
#         self.price = price
#
#
#     @classmethod
#     def get_identify(cls):
#         '''类方法'''
#         print(cls.identify)
#
#     def get_total_price(self,num):
#         '''对象方法'''
#         self.num = num
#         print('%s个%s值%s钱' % (self.num,self.name,self.price * self.num))
#
#     @staticmethod
#     def packing(*fruits):
#         '''静态方法'''
#         apple = 0
#         banana = 0
#         for i in fruits:
#             if '苹果' in i.name:
#                 apple += 1
#             elif '香蕉' in i.name:
#                 banana += 1
#         print('一箱装了%s个苹果%s个香蕉' % (apple,banana))
#
#
# red_apple = Fruit("红苹果", 10)
# green_apple = Fruit("青苹果", 10)
# yellow_banana = Fruit("黄香蕉", 8)
# Fruit.packing(red_apple, green_apple, yellow_banana)


'''
2.自定义一个 Person 类，该类对象具有 name、weight、height、sex，
	-- 对name属性进行封装，但是外界任然可以访问name以及设置name
	-- 有一个方法属性bmi(标准体重)，可以获取一个人的bmi，bmi只读不可写，bmi计算规则
		-- 男：（身高cm－80）× 70﹪  |  女：（身高cm－70）× 60﹪
'''
# class Person(object):
#     def __init__(self,name,weight,height,sex):
#         self.__name = name
#         self.weight = weight
#         self.height = height
#         self.sex = sex
#
#     @property
#     def name(self):
#         return self.__name
#
#     @name.setter
#     def name(self,value):
#         self.__name = value
#
#     @property
#     def bmi(self):
#         if self.sex == '男':
#             return (self.height - 80) * 0.7
#         if self.sex == '女':
#             return (self.height - 70) * 0.6
#
# szk = Person('szk',70,170,'男')
# yue = Person('yue',60,165,'女')
# print(szk.bmi)
# print(yue.bmi)
#
# print('------------华丽分割线-----------------')
# szk.name = 'wesley'
# print(szk.name)

'''
用面向对象实现 植物大战僵尸游戏

1.定义一个僵尸Zombie类，该类可以实例化出多种僵尸对象，僵尸对象产生默认都有 名字name、血量HP、防具armor
	-- 名字：普通僵尸 | 路障僵尸 | 铁桶僵尸
	-- 血量：默认就是100，不需要外界提供
	-- 防具：不需要外界提供，从名字中分析确定，防具的值是一个列表，从名字分析得到
			-- ['无', 0] | ['路障', 5] | ['铁桶', 15]  => [防具名, 防具的防御值]
	-- 通过@property的getter、setter方式，对外提供防具的两个访问接口armor_name与armor_count
			-- armor_name可以取值、赋值、删除值：通过一个
				-- eg: 普通僵尸对象.armor_name = '铁桶'，不仅改变了防具名
				--     普通僵尸对象的名字name也会变成 铁桶僵尸
			-- armor_count只可以取值
			
2.定义一个角色User类，该类有名字name属性、以及打僵尸的beat方法
	-- 名字：随意自定义
	-- beat：该方法需要传入一个僵尸对象
			-- 在方法内部可以实现：某某用户攻击了某某个僵尸，僵尸损失多少血，还剩多少血
			-- 每一次攻击，都固定扣除25滴血，但是不同的僵尸会被防具相应抵消掉一定的伤害值
			-- 循环攻击僵尸，3s攻击一次，僵尸被击杀后，打印 某某用户击杀了某某个僵尸 并结束方法

3.定义一个Game类，该类有一个name属性，属性值为 "植物大战僵尸" ，该类中有一个start方法，通过Game.start()来启动游戏
	-- 游戏一开始先显示游戏的名字 植物大战僵尸游戏
	-- 会随机产生三种僵尸，总共产生三个作为要被击杀的对象
	-- 生成一个有角色名的角色，依次去击杀随机产生的每一只僵尸
		-- 开始击杀第一只僵尸 => 某某用户攻击了某某个僵尸，僵尸损失多少血，还剩多少血 => 某某用户击杀了某某个僵尸 => 第一只僵尸已被击杀完毕 => 开始击杀第二只僵尸 ... => 第三只僵尸已被击杀完毕
'''
import time
import random

class Zombie(object):
    name = ''
    HP = 100

    def __init__(self, armor_name):
        self.__armor_name = armor_name + '僵尸'
        if armor_name == '普通':
            self.__armor = ['无', 0]
        if armor_name == '路障':
            self.__armor = ['路障', 5]
        if armor_name == '铁桶':
            self.__armor = ['铁桶', 15]

    @property
    def armor_name(self):
        return self.__armor_name

    @armor_name.setter
    def armor_name(self, value):
        self.__armor_name = value
        if value == '普通':
            self.__armor = ['无', 0]
        if value == '路障':
            self.__armor = ['路障', 5]
        if value == '铁桶':
            self.__armor = ['铁桶', 15]

    @armor_name.deleter
    def armor_name(self):
        del self.__armor_name

    @property
    def armor_count(self):
        return self.__armor


# z1 = Zombie('普通')
# print(z1.armor_name, z1.armor_count)
#
# z2 = Zombie('铁桶')
# print(z2.armor_name, z2.armor_count)
#
# z3 = Zombie('路障')
# print(z3.armor_name, z3.armor_count, z3.HP)


class User(object):
    def __init__(self, name):
        self.name = name

    def beat(self, obj):
        zombie_HP = obj.HP
        zombie_name = obj.armor_name
        zombie_count = obj.armor_count[1]
        while True:
            zombie_HP = zombie_HP - 25 + zombie_count
            print('%s用户攻击了%s，僵尸损失%s血,还剩%s血' % (self.name, zombie_name, 25 - zombie_count, zombie_HP))
            if zombie_HP <= 0:
                print('%s用户击杀了%s僵尸' % (self.name,zombie_name))
                break
            time.sleep(3)

# u1 = User('wesley')
# u1.beat(z3)

class Game(object):
    print('----植物大战僵尸游戏----')

    @classmethod
    def start(cls):
        num = 1
        while num <= 3:
            zombie = random.choice(['普通','路障','铁桶'])
            zombie_obj = Zombie(zombie)
            user = User('szk')
            print('开始击杀第%s只僵尸' % num)
            user.beat(zombie_obj)
            print('第%s僵尸击杀完毕' %num)
            num += 1

Game.start()


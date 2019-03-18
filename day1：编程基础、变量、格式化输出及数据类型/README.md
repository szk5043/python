# 1：编程基础、变量、格式化输出及数据类型
#### 学习方法：3W1H
- 知道原理学技术：3w1h
- 忘掉原理用技术：熟练度
- 回归原理拔技术：源码
> 重点：熟练度

### 一、编程基础

#### 1、编程和编程语言

什么是编程语言？

编程语言：与计算机进行沟通的语言。

什么是编程？

编程：奴役计算机，让计算机安照指定的方式帮助我们完成特定的需求



#### 2、计算机语言的发展

机器语言：01代码指令

汇编语言：助记词 MOV CMP CF

高级语言：Java，C，Python

> 总结：
>
> 机器语言：与机器直接交互，执行效率最高
>
> 汇编语言：执行效率较高，没有机器语言效率高，开发效率比机器语言高
>
> 高级语言：执行效率最低，开发效率最高（重点）

#### 3、高级语言的执行方式

- 编译型：类似于百度翻译，执行效率高

- 解释型：类似于同声传译，开发效率高。（python：后出现的能使用前出现的资源，反则不行，因为程序从上往下执行）

  > 没有绝对的解释型预发，详情请点击[**pyc是何物？**](https://www.cnblogs.com/lzhn/p/7805251.html)



#### 4、Python的交互方式

- 实时交互：提前进入python解释器环境，只能一条一条的执行。

- 文件交互：将文件交给python解释器执行。（效率高）

  > 注：python默认文件后缀为.py

### 二、变量

#### 1、用3W1H

- what：可变的 状态（量是用来描述事物的某种状态）

- why：如何用代码来描述事物的某种（可变化）状态

- where：任何地方都会使用到变量

- how:

  - 如何定义变量： 变量名 = 变量值，=为赋值符号
    - name = 'wesley' : 在堆区开辟空间存放变量值，在栈区开辟名为变量名的空间存放堆区变量值那个区域的地址
    - name = 'szk' : 重新赋值，重新开辟空间存放变量值，跟原本的变量名进行绑定，原来变量名name的值就为

  - 如何使用变量： 变量名

    > 没有被变量名绑定的变量值就会被系统回收

> 内存的堆栈为何物？，[**内存堆栈**](没有被变量名绑定的变量值就会被系统回收)



#### 2、变量三要素

1. 变量值：变量名
2. 变量地址：id(变量名)
3. 变量的类型：type(变量名)

> 注：新建值，系统就会开辟空间存放该值，但存在python的优化机制，当变量值简单时，python会沿用之前的变量值

```python
name1 = 'szk'
name2 = 'szk'
id(name1) == id(name2) 
```

### 3、变量名命名规范

1. 可以由数字、字母、下划线组合
2. 不能以数字开头
3. 不能与系统关键字保留字重名
4. 见名知意，建议使用_连接语法（驼峰 owenName OwenName | _连接  owen_name），一般_开头或结尾都有特殊含义

### 三、格式化输出

### 1、用+ 加号拼接

```python
name = input("name: ")
age = int(input("age: "))
job = input("job: ")
info = '''
----- info of''' + name +''' -----
Name: ''' + str(name) + '''
Age: ''' + str(age) + '''
Job: ''' + str(job)
print(info)
```

### 2、占位符%拼接

```python
name = input("name: ")
age = int(input("age: "))
job = input("job: ")
info = '''
----- info of %s  -----
name: %s
age: %d
job: %s
''' %(name,name,age,job)
print(info)
```

> %s是字符串格式化，%d是整数格式化，%f的小数格式化（%.2f表示保留两位小数）

### 3、format函数拼接

#### a、位置拼接

```python
name='wesley'
age='25'
info='my name is {},my age is {}'.format(name,age)
print(info)
```

#### b、占位符拼接

```python
name='wesley'
age='25'
info='my name is {0},my age is {1}'.format(name,age)
print(info)
```

#### c、关键字拼接

```python
name='wesley'
age='25'
info='my name is {name},my age is {age}'.format(name=name,age=age)
print(info)
```

### 四、数据类型

#### 1、python中的数据类型

python数据类型分为整数int、小数float、字符串Str、布尔值Bool、列表List、元组Tupe、字典Dict

#### 2、int

```python
age = 18
print(age,type(age))
```

#### 3、float
```python
salary = 1.5
print(salary,type(salary))
```

#### 4、str
```python
name = szk
print(name,type(name))
```
#### 5、bool
```python
result = False
print(result,type(result))
```
#### 6、list
```python
list_1 = ["张三","李四","王五"]
print(list_1,type(list_1))
```
#### 7、tupe
```python
tupe_1 = ("张三","李四","王五")
print(tupe_1,type(tupe_1))
```
#### 8、dict
```python
dict_1 = {
    "name" : "张三",
    "age" : 18,
    "job" : "OP"
}
print(dict_1,type(dict_1))
```

### 五、运算符

#### 1、算术运算符

算术运算符有+、-、*、/、%

```python
print(10+2)
print(10-2)
print(10*2)
print(10/2)
print(10//2)
print(10%2)
```

#### 2、比较运算符

比较运算符有> 、 < 、 == 、 != 、 >= 、 <=

```python
res = 5 >= 3
print(res
```

#### 3、逻辑运算符
逻辑运算符有and、or、not
- and为真：两个真 | 为假，有一个及以上为假就为假
- or为假：两个假 | 为真，有一个及以上为真就为真
- not真真假假，假假真真
```python
res = 1 and 2 or 3
print(res)  # 2

res = 1 and 0 or 3
print(res)  # 3

res = 1 and 0 and 3
print(res)  # 0

res = 1 or 0 or 3
print(res)  # 1

res = 1 or 0 or 3  # 重点
print(res)  # 1
```





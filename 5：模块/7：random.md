## 七、random

### 1、概述

random模块主要用来生成随机数，最典型的应用就是生成验证码

### 2、random常用方法

```python
import random

print( random.randint(1,10) )        # 产生 1 到 10 的一个整数型随机数  
print( random.random() )             # 产生 0 到 1 之间的随机浮点数
print( random.uniform(1.1,5.4) )     # 产生  1.1 到 5.4 之间的随机浮点数，区间可以不是整数
print( random.choice('tomorrow') )   # 从序列中随机选取一个元素
print( random.randrange(1,100,2) )   # 生成从1到100的间隔为2的随机整数

'''
返回值
6
0.8209207788618604
1.4418925654292114
m
37
'''
```

### 3、生成验证码

**示例1：利用ANSI区间随机生成一个包含大小写字母和数字的 随机数**

```python
import random

def get_code(count):
    code = ""
    # 能产生大小写字母与数字
    # 进行字符串拼接
    for i in range(count):
        c1 = chr(random.randint(65, 90))
        c2 = chr(random.randint(97, 122))
        c3 = str(random.randint(0, 9))
        code += random.choice([c1, c2, c3])
    return code

print(get_code(4))

'''
返回值
0Veq
'''
```

或者，换一种写法

```python
import random

def get_code(count):
    code = ""
    # 能产生大小写字母与数字
    # 进行字符串拼接
    for i in range(count):
        r = random.choice([1, 2, 3])
        if r == 1:
            c = chr(random.randint(65, 90))
        elif r == 2:
            c = chr(random.randint(97, 122))
        else:
            c = str(random.randint(0, 9))
        code += c
    return code

print(get_code(4))
```

**示例2：直接写好随机生成的区间**

```python
import random

def get_code(count):
    target = "1234567890QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm"
    code_list = random.sample(target, count)
    return ''.join(code_list)

print(get_code(4))

'''
jSmJ
'''
```


#### 1.以自己的理解总结为什么会出现循环导入，并用代码举例说明

循环导入：a依赖b，b依赖a，导致调用在定义之先

```python
# a.py
a = 10
import b
print(b.b)
```

```python
# b.py
b = 20
import a 
print(a.a)
```

#### 2.如何来解决循环导入，并解决第1题中的循环导入问题

将导入的位置放到定义之后，即 将a.py  与 b.py变量调用放到变量定义之后，即可解决。
**遵循：先定义，后导入**

#### 3.完成housework.py文件，拥有三个功能：sweep、wash、cook，自定义功能实现(函数体)，从文件自执行和作为模块使用两方面，验证三个功能，且两方面使用方式可以共存

```python
# housework.py
def sweep():
    print('sweep 功能')

def wash():
    print('wash 功能')

def cook():
    print('cook 功能')

if __name__ == '__main__':  # 实现自运行和执行文件入口，不干扰
    sweep()
    wash()
    cook()
```

#### 4.导入模块的搜索路径有哪些？它们的优先级是？

搜索路径顺序：内存>内置模块>sys.path 的路径顺序遍历，自定义模块（自己写，第三方库，别人写）

#### 5.模块的相对路径和绝对路径
现有一个run.py运行文件，与run文件同级目录下有一个pgk文件夹，文件夹下有两个模块m1、m2，m1模块内有功能f1，可以打印字符串"我是m1模块"，m2模块内有功能f2，可以打印字符串"我是m2模块"，在run文件中，通过绝对路径方式导入m1模块，验证功能，在模块m1中通过相对路径导入m2模块，验证功能

**文件目录树：**

```shell
.
├── pgk
│   ├── __init__.py
│   ├── m1.py
│   └── m2.py
└── run.py
```

**绝对路径导入：**

`run.py`

```python
from pgk import m1,m2
m1.f1()
m2.f2()
```
`pkg/m1.py`

```python
def f1():
    print('我是m1模块')
```
`pkg/m2.py`

```python
def f2():
    print('我是m2模块')
```

**相对路径导入：**

`run.py`

```python
import pgk
pgk.f1()
pgk.f2()
```

`pkg/__init__.py`

```python
from .m1 import f1
from .m2 import f2
```

`pkg/m1.py`

```python
def f1():
    print('我是m1模块')
```

`pkg/m2.py`

```python
def f2():
    print('我是m2模块')
```




#### 6.建立如下包结构，完成包的使用

​	结构：
​	1）包名为pkg
​	2）一级目录pkg下：
​		-- m.py 模块 有函数m_fn
​		-- sub1 子包
​		-- sub2 子包
​	3）二级目录sub1下：
​		-- m1.py 模块 有函数 m1_fn
​	4）二级目录sub2下：
​		-- m2.py 模块 有函数 m2_fn
​	要求：
​	1）在执行文件run.py只导入pkg包，不做其他导入操作
​	2）在执行文件run.py中访问三个函数的方式分别是
​		pgk.m_fn()
​		pgk.m1_fn()
​		pgk.sub2.m2_fn()
​	如何来设计包
'''

**文件目录树：**

```shell
.
├── pgk
│   ├── __init__.py
│   ├── m.py
│   ├── sub1
│   │   ├── __init__.py
│   │   └── m1.py
│   └── sub2
│       ├── __init__.py
│       └── m2.py
└── run.py
```

`run.py`

```python
import pgk
pgk.m_fn()
pgk.m1_fn()
pgk.sub2.m2_fn()
```

`pgk\__init__.py`

```python
from .m import m_fn
from .sub1.m1 import m1_fn
from . import sub2
```

`pgk\m.py`

```python
def m_fn():
    print('m_fn')
```

`pgk/sub1/m1.py`

```python
def m1_fn():
    print('m1_fn')
```
`pgk/sub2/__init__.py`

```python
from .m2 import m2_fn
```


`pgk/sub2/m2.py`

```python
def m2_fn():
    print('m2_fn')
```


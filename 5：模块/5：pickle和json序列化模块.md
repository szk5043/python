## 五、Pickle和JSON序列化模块

### 1、序列化概述

**什么是序列化？**

我们在写入文件中的数据，只能是字符串，但是如果要想把内存的数据对象存到硬盘上去怎么办呐？下面就来说说序列化：**序列化就是将内存中的数据持久化到硬盘**

**为什么需要序列化？**

有个需求需要将字典存储到硬盘中，先转换为字符串写入文件；读取时，需要读取为字符串再转换为原始的格式，数据复杂时就很麻烦。序列化可以写入和读取都是原格式（比如字典）

**序列化和反序列化：**

序列化：能将 所有python中的数据序列化，（序列化时序列化成二进制格式写入文件）

反序列化：将之前序列化的数据，再恢复成python的数据格式

### 2、Pickle

**python优缺点：**

- python内置序列化模块之一
- pickle是二进制序列化格式
- 支持python所有数据类型
- 仅支持python语言写入和读取，无法跨语言

**示例1：将字典序列化写入文件**

```python
import pickle
users = {"name":"szk","age":26,"hobbies":["吃饭","睡觉","打豆豆"]}

print(type(pickle.dumps(users)))   #<class 'bytes'>

with open('user.txt','wb') as f:
    f.write(pickle.dumps(users))
```

**示例2：将序列化的文件进行反序列化读取**

```python
import pickle

with open('user.txt','rb') as f:
     user_dict = pickle.loads(f.read())
     print(user_dict,type(user_dict))
    
'''
#返回值
{'name': 'szk', 'age': 26, 'hobbies': ['吃饭', '睡觉', '打豆豆']} <class 'dict'>
'''
```

**示例3：直接序列化和反序列化操作文件**

```python
import pickle

users = {"name":"szk","age":26,"hobbies":["吃饭","睡觉","打豆豆"]}
pickle.dump(users,open('user.txt','wb'))    #序列化进文件
print(pickle.load(open('user.txt','rb')))   #从文件反序列化

'''
#返回值
{'name': 'szk', 'age': 26, 'hobbies': ['吃饭', '睡觉', '打豆豆']}
'''
```

### 3、JSON

**JSON的优缺点：**

- json是一种文本序列化格式（它输出unicode文本，虽然大部分时间它被编码`utf-8`）

- json是人类可读的，而pickle则不是;
- json可以支持python的数据类型有str、int、float、dic、list、bool
- json是可互操作的，并且在Python生态系统之外广泛使用，而pickle是特定于Python的;

- 默认情况下，json只能表示Python内置类型的子集，而不能表示自定义类; pickle可以表示极其庞大的Python类型（其中许多是自动的，通过巧妙地使用Python的内省工具;复杂的案例可以通过实现[特定的对象API](https://docs.python.org/3/library/pickle.html#pickle-inst)来解决）。

Python 和 JSON数据类型对比：

![images](./images/1.png)

**示例1：json序列化成json文件**

```python
import json

users = {"name":"szk","age":26,"hobbies":["吃饭","睡觉","打豆豆"]}
print(type(json.dumps(users)))   #<class 'str'>
json.dump(users,open('user.json','w',encoding='utf-8'))

'''
cat user.json
{"name": "szk", "age": 26, "hobbies": ["\u5403\u996d", "\u7761\u89c9", "\u6253\u8c46\u8c46"]}
'''
```

json.dump和json.dumps的区别：

- json.dump是将python数据保存成json文件
- json.dumps是将dict保存成str格式

json文件中的中文看起来是编码问题，因为json输出unicode文本

**示例2：json反序列化**

```python
import json

json_str = json.load(open('user.json','r',encoding='utf-8'))
print(json_str,type(json_str))

'''
返回值：
{'name': 'szk', 'age': 26, 'hobbies': ['吃饭', '睡觉', '打豆豆']} <class 'dict'>
'''
```

json.load和json.loads的区别：

- json.loads是将str转成dict
- json.load是从json文件读取数据，源格式是什么就读取为什么，示例2中源格式为dict


## 八、hashlib模块

### 1、概述

Python 中的 hashlib 模块用来进行 hash 或者 md5 加密。这里的加密，其实并非我们通常所说的加密，简单的说就是这种加密一般是不可逆的。

这种加密算法实际上是被称之为`摘要算法`，包括 MD5，SHA1 等等。MD5的全称是Message-Digest Algorithm 5（信息-摘要算法）。SHA1的全称是Secure Hash Algorithm(安全哈希算法) 。SHA1基于MD5，加密后的数据长度更长。

一般项目中，只保存用户密码的哈希值，而不直接保存密码。用户登录的时候，直接比对密码的哈希值即可。一般也会做`加盐`处理，就是在原密码的基础上加上一些额外的字母或数字进行哈希，增加`碰撞解密的成本`。

什么是碰撞解密：对于MD5的破解，实际上都属于【碰撞】。比如原文A通过MD5可以生成摘要M，我们并不需要把M还原成A，只需要找到原文B，生成同样的摘要M即可。

### 2、常用的hash算法

hashlib是个专门提供hash算法的库，里面包括md5, sha1, sha224, sha256, sha384, sha512。

```python
import hashlib

a = "I am wesley"
print(hashlib.md5(a.encode('utf-8')).hexdigest())
print(hashlib.sha1(a.encode('utf-8')).hexdigest())
print(hashlib.sha224(a.encode('utf-8')).hexdigest())
print(hashlib.sha256(a.encode('utf-8')).hexdigest())
print(hashlib.sha384(a.encode('utf-8')).hexdigest())
print(hashlib.sha512(a.encode('utf-8')).hexdigest())

'''
f1632e2eabe9f35c00c3826c7c26fea1
ba08a22add363f40985ee82bfb8a3409e7029b73
11a4b0242a1f84606806e7030669b5ecf0148c6b054f0eeaf34148b7
67887f3f77b43191cf7de13e800ad3b391d3e3bc6f85a93741c0b4d3126086f6
c46901aa8e29413005c640a55fe905fa0bed461660c1ba235ba7e8d47ba25781832426af9d3b82a13db6db252858d7a3
888c02c66af5728bb7b8552ddfecce861030c6baadf8c1dc906f7d8857efed017ff5f390879c51728edc18410b0bc3f9976d394fe898d6f23bcd3154e1484f39
'''
```

> 默认python3使用unicode编码，需要编码成utf-8，再获取十六进制数值

### 3、加盐

可以使用用户注册时间做**加盐**数据，但是需要将注册时间保存，否则哈希值比对就会出错

```python
import hashlib
import time

password = 'qwe123!@#'
now_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))

hash_obj = hashlib.md5(password.encode('utf-8'))
hash_obj.update(now_time.encode('utf-8'))
print(hash_obj.hexdigest())

'''
1dcc53bf1cd3a5a932f13ed3c02ce2b5
'''
```


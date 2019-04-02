## 二、三种字符串

#### 1、Unicode字符串
u/U（Unicode字符串）：python3.x默认的存储编码，所以一般不带u。

```python
s1 = u'abc123你好'
print(s1)

'''
返回值：
abc123你好
'''
```

#### 2、原始字符串
r/R非转义的原始字符串：字符串出现任何转义字符，都以原始字符串的方法表达
```python
s3 = r'你好\n好的'
print(s3)

'''
返回值：
你好\n好的
'''
```
> 字符串的转义字符\n，没有起效果，因为字符串前面加了r

#### 3、二进制字符串
b(bytes)：二进制字符串，数据传输都是以字节为单位
```python
s1 = 'abc123你好'
res = s1.encode('utf-8')   # 编码
print(res)
s2 = res.decode('utf-8')   # 解码
print(s2) 

'''
返回值：
b'abc123\xe4\xbd\xa0\xe5\xa5\xbd'
abc123你好
'''
```
> python3.x里默认的str是(py2.x里的)unicode, bytes是(py2.x)的str, b”“前缀代表的就是bytes 
> python2.x里, b前缀没什么具体意义， 只是为了兼容python3.x的这种写法


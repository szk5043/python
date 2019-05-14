## 九、re模块

### 1、概述

**正则表达式（Regular Expression）**是字符串处理的常用工具，通常被用来检索、替换那些符合某个模式（Pattern）的文本。很多程序设计语言都支持正则表达式，像Perl、Java、C/C++。在 Python 中是通过标准库中的 **re 模块** 提供对正则的支持。

### 2、作用和应用场景

- 用于从字符串中匹配满足某种规则的内容，多数用于爬虫应用程序

- 判断字符串串内容是否满足某种规则，多用于严重用户输入。例如密码是否规范，手机号是否正确等

### 3、语法

下图列出了Python支持的一些正则表达式元字符和语法：

| 元字符      | 描述                                                         |
| ----------- | :----------------------------------------------------------- |
| \           | 将下一个字符标记符、或一个向后引用、或一个八进制转义符。例如，“\\n”匹配\n。“\n”匹配换行符。序列“\\”匹配“\”而“\(”则匹配“(”。即相当于多种编程语言中都有的“转义字符”的概念。 |
| ^           | 匹配输入字行首。如果设置了RegExp对象的Multiline属性，^也匹配“\n”或“\r”之后的位置。 |
| $           | 匹配输入行尾。如果设置了RegExp对象的Multiline属性，$也匹配“\n”或“\r”之前的位置。 |
| *           | 匹配前面的子表达式任意次。例如，zo*能匹配“z”，也能匹配“zo”以及“zoo”。*等价于{0,}。 |
| +           | 匹配前面的子表达式一次或多次(大于等于1次）。例如，“zo+”能匹配“zo”以及“zoo”，但不能匹配“z”。+等价于{1,}。 |
| {*n*}       | *n*是一个非负整数。匹配确定的*n*次。例如，“o{2}”不能匹配“Bob”中的“o”，但是能匹配“food”中的两个o。 |
| {*n*,}      | *n*是一个非负整数。至少匹配*n*次。例如，“o{2,}”不能匹配“Bob”中的“o”，但能匹配“foooood”中的所有o。“o{1,}”等价于“o+”。“o{0,}”则等价于“o*”。 |
| {*n*,*m*}   | *m*和*n*均为非负整数，其中*n*<=*m*。最少匹配*n*次且最多匹配*m*次。例如，“o{1,3}”将匹配“fooooood”中的前三个o为一组，后三个o为一组。“o{0,1}”等价于“o?”。请注意在逗号和两个数之间不能有空格。 |
| ?           | 匹配前面的子表达式零次或一次。例如，“do(es)?”可以匹配“do”或“does”。?等价于{0,1}。 |
| ?           | 当该字符紧跟在任何一个其他限制符（*,+,?，{*n*}，{*n*,}，{*n*,*m*}）后面时，匹配模式是非贪婪的。非贪婪模式尽可能少地匹配所搜索的字符串，而默认的贪婪模式则尽可能多地匹配所搜索的字符串。例如，对于字符串“oooo”，“o+”将尽可能多地匹配“o”，得到结果[“oooo”]，而“o+?”将尽可能少地匹配“o”，得到结果 ['o', 'o', 'o', 'o'] |
| .点         | 匹配除“\n”和"\r"之外的任何单个字符。要匹配包括“\n”和"\r"在内的任何字符，请使用像“[\s\S]”的模式。 |
|             |                                                              |
| x\|y        | 匹配x或y。例如，“z\|food”能匹配“z”或“food”(此处请谨慎)。“[zf]ood”则匹配“zood”或“food”。 |
| [xyz]       | 字符集合。匹配所包含的任意一个字符。例如，“[abc]”可以匹配“plain”中的“a”。 |
| [^xyz]      | 负值字符集合。匹配未包含的任意字符。例如，“[^abc]”可以匹配“plain”中的“plin”任一字符。 |
| [a-z]       | 字符范围。匹配指定范围内的任意字符。例如，“[a-z]”可以匹配“a”到“z”范围内的任意小写字母字符。注意:只有连字符在字符组内部时,并且出现在两个字符之间时,才能表示字符的范围; 如果出字符组的开头,则只能表示连字符本身. |
| [^a-z]      | 负值字符范围。匹配任何不在指定范围内的任意字符。例如，“[^a-z]”可以匹配任何不在“a”到“z”范围内的任意字符。 |
| \b          | 匹配一个单词的边界，也就是指单词和空格间的位置（即正则表达式的“匹配”有两种概念，一种是匹配字符，一种是匹配位置，这里的\b就是匹配位置的）。例如，“er\b”可以匹配“never”中的“er”，但不能匹配“verb”中的“er”；“\b1_”可以匹配“1_23”中的“1_”，但不能匹配“21_3”中的“1_”。 |
| \B          | 匹配非单词边界。“er\B”能匹配“verb”中的“er”，但不能匹配“never”中的“er” |
| \s          | 匹配任何不可见字符，包括空格、制表符、换页符等等。等价于[ \f\n\r\t\v]。 |
| \S          | 匹配任何可见字符。等价于[^ \f\n\r\t\v]。                     |
| \w          | 匹配包括下划线的任何单词字符。类似但不等价于“[A-Za-z0-9_]”，这里的"单词"字符使用Unicode字符集。 |
| \W          | 匹配任何非单词字符。等价于“[^A-Za-z0-9_]”。                  |
| \d          | 匹配一个数字字符。等价于[0-9]。grep 要加上-P，perl正则支持   |
| \D          | 匹配一个非数字字符。等价于[^0-9]。grep要加上-P，perl正则支持 |
| \n          | 匹配一个换行符。等价于\x0a和\cJ。                            |
| \r          | 匹配一个回车符。等价于\x0d和\cM。                            |
| \t          | 匹配一个制表符。等价于\x09和\cI。                            |
| ( )         | 将( 和 ) 之间的表达式定义为“组”（group），并且将匹配这个表达式的字符保存到一个临时区域（一个正则表达式中最多可以保存9个），它们可以用 \1 到\9 的符号来引用。 |
| (?:pattern) | 非获取匹配，匹配pattern但不获取匹配结果，不进行存储供以后使用。这在使用或字符“(\|)”来组合一个模式的各个部分时很有用。例如“industr(?:y\|ies)”就是一个比“industry\|industries”更简略的表达式。 |
| \|          | 将两个匹配条件进行逻辑“或”（Or）运算。例如正则表达式(him\|her) 匹配"it belongs to him"和"it belongs to her"，但是不能匹配"it belongs to them."。注意：这个元字符不是所有的软件都支持的。 |

**贪婪模式与非贪婪模式**

“贪婪模式”总是尝试匹配尽可能多的字符；“非贪婪模式”则相反，总是匹配尽可能少的字符。例如，用”ab*“如果用于查找”abbbc”，将找到”abbb”。而如果使用非贪婪的数量词”ab*?”，将找到”a”。

### 3、匹配示例

**示例1：单个字符匹配**

```python
import re

#匹配a
print(re.findall(r'a','123abc嘿嘿'))  #返回['a']

#匹配a或b
print(re.findall(r'a|b','123abc嘿嘿'))   # 返回['a', 'b'] 不建议使用，因为存在特殊字符'|'就无法正确匹配
print(re.findall(r'[ab]','123abc嘿嘿'))   #返回['a', 'b'] 建议使用

#匹配非a非b
print(re.findall(r'[ab]','123abc嘿嘿'))   #返回['1', '2', '3', 'c', '嘿', '嘿']

# re.I不区分大小写匹配
print(re.findall(r'a', '123abc123ABC', flags=re.I))  #返回['a', 'A']

#匹配数字
print(re.findall(r'\d', '12abc嘿嘿12'))  #返回['1', '2', '1', '2'] ，不建议使用
print(re.findall(r'[0-9]','12abc嘿嘿12'))   #返回['1', '2', '1', '2'] 建议使用

#匹配非数字，\d数字 \D非数字
print(re.findall(r'\D', '12abc\f嘿嘿12'))  # ['a', 'b', 'c', '\x0c', '嘿', '嘿']

#匹配字母
print(re.findall(r'[a-zA-Z]', '12abc[嘿嘿ABC'))  #返回 ['a', 'b', 'c', 'A', 'B', 'C']

#匹配 字母、数字、下划线_和常用汉字
print(re.findall(r'\w', '12abc[_嘿嘿ABC'))    #返回['1', '2', 'a', 'b', 'c', '_', '嘿', '嘿', 'A', 'B', 'C']

#匹配汉字，用unicode编码[\u4e00-\u9fa5]匹配所有汉字
print(re.findall(r'[\u4e00-\u9fa5]', '12abc[_嘿嘿ABC'))  #返回['嘿', '嘿']

#匹配任何不可见字符，包括空格、制表符、换页符等等。等价于[ \f\n\r\t\v]
print(re.findall(r'\s', ' \f\n\r\t\v'))  #返回 [' ', '\x0c', '\n', '\r', '\t', '\x0b']

#匹配除“\n”和"\r"之外的任何单个字符
print(re.findall(r'.', ' \f\n\r\t\v*&_.'))  # 返回[' ', '\x0c', '\r', '\t', '\x0b', '*', '&', '_', '.']

#匹配任意字符，包括包括“\n”和"\r"在内的任何字符，加flags=re.S
print(re.findall(r'.', ' \f\n\r\t\v*&_.', flags=re.S))  #返回[' ', '\x0c', '\n', '\r', '\t', '\x0b', '*', '&', '_', '.']

# 只想匹配.字符，加转义符\.
print(re.findall(r'\.', ' \f\n\r\t\v*&_.'))  #返回 ['.']
```

**示例2：重复字符匹配**

贪婪匹配：尽可能多的匹配

```python
import re

# 匹配ab
print(re.findall(r'ab', 'abacbabc'))  # ['ab', 'ab']

# 匹配abb，并指定个数
print(re.findall(r'ab{2}', 'aababbabbb'))  # ['abb', 'abb']

# 匹配a0~2个b: a | ab | abb
print(re.findall(r'ab{,2}', 'aababbabbb'))  # ['a', 'ab', 'abb', 'abb']

#匹配 a0~n个b:
print(re.findall(r'ab{0,}', 'aababbabbb'))  # ['a', 'ab', 'abb', 'abbb']

#匹配 a1~3个b:
print(re.findall(r'ab{1,3}', 'aababbabbb'))  # ['ab', 'abb', 'abbb']

#匹配 ab* 等同于ab{0,}
print(re.findall(r'ab*', 'aababbabbb'))  # ['a', 'ab', 'abb', 'abbb']

#匹配 ab+ 等同于ab{1,}
print(re.findall(r'ab+', 'aababbabbb'))  # ['ab', 'abb', 'abbb']

# 匹配 ab?等同于ab{,1}
print(re.findall(r'ab?', 'aababbabbb'))  # ['a', 'ab', 'ab', 'ab']
```

贪婪匹配和非贪婪匹配对比：

```python
import re

print(re.findall(r'ab{1,3}', 'aababbabbb'))   #['ab', 'abb', 'abbb']
print(re.findall(r'ab{1,3}?', 'aababbabbb'))  # ['ab', 'ab', 'ab']
```

非贪婪匹配应用场景，一般都是结合有开头与结尾的标识，比如匹配HTML标签

```python
import re

print(re.findall(r'<.{1,}>', '<a><b>msg</b></a>'))  # ['<a><b>msg</b></a>']
print(re.findall(r'<.{1,}?>', '<a><b>msg</b></a>'))  # ['<a>', '<b>', '</b>', '</a>']
```

非贪婪模式中的*、+、？

```python
# *?等同于{0,}?
# +?等同于{1,}?
# ??等同于{,1}?
```

**实例3：分组语法**

findall(): 没有分组情况下，显示匹配的结果；如果有分组，显示分组结果

语法：

- 分组：()
- 取消分组：(?:)
- 有名分组：(?P<名字>)

匹配链接

```python
import re

# 匹配域名
print(re.findall(r'www\..+?\.com', 'www.baidu.comabcwww.sina.com'))  
# ['www.baidu.com', 'www.sina.com']

# 获取链接的域名：['baidu', 'sina']
print(re.findall(r'www\.(.+?)\.com', 'www.baidu.comabcwww.sina.com'))  
# ['baidu', 'sina']

# 分组编号: 从左往右数左(进行分组编号
print(re.findall(r'(www\.(.+?)\.(com|edu))', 'www.baidu.comabcwww.sina.edu'))   
#[('www.baidu.com', 'baidu', 'com'), ('www.sina.edu', 'sina', 'edu')]
print(re.findall(r'(www\.(.+?)\.(com|edu))', 'www.baidu.comabcwww.sina.edu')[0])   
#('www.baidu.com', 'baidu', 'com')

# 取消分组:(?:) 应用于，要将一些数据作为整体看待，但由不能产生分组
print(re.findall(r'(www\.(.+?)\.(?:com|edu))', 'www.baidu.comabcwww.sina.edu'))  
#[('www.baidu.com', 'baidu'), ('www.sina.edu', 'sina')]

# 结合分组可以完成数据的重组
res = re.sub(r'(good) (day) (a)', r'today is \3 \1 \2', 'good day a!!!')
print(res)  # today is a good day!!!
```

**示例4：其他方法**

match()：必须从头开始匹配，且只匹配一次，不是全文匹配

split(): 拆分

sub(): 替换

```python
import re

# match:不是全文匹配，必须从头开始匹配，且只匹配一次
res = re.match(r'(www\.(?P<site_name>.+?)\.(?:com|edu))', 'www.baidu.comwww.sina.edu')
# 可以通过分组号直接取出分组内容
print(res.group(1))   # www.baidu.com
print(res.group(2))   # baidu


# split(): 拆分
print('abc def xyz'.split(' '))   # ['abc', 'def', 'xyz']
print(re.split(r' ', 'abc def xyz'))  # ['abc', 'def', 'xyz']
print(re.split(r'[,@ ]', 'abc,def@xyz opq')) #['abc', 'def', 'xyz', 'opq']


# sub(): 替换
print(re.sub(r'good', 'bed', 'good good day a'))   # bed bed day a
print(re.sub(r'good', 'bed', 'good good day a', count=1))   # bed good day a
print(re.sub(r'good day a', '123', 'good day a!!!'))   # 123!!!

```


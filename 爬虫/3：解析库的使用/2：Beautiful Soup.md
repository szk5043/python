## 二、Beautiful Soup

### 1、简介

简单来说，Beautiful Soup就是Python的一个HTML或XML的解析库，可以用它来方便地从网页中提取数据。官方解释如下：

```
  Beautiful Soup提供一些简单的、Python式的函数来处理导航、搜索、修改分析树等功能。它是一个工具箱，通过解析文档为用户提供需要抓取的数据，因为简单，所以不需要多少代码就可以写出一个完整的应用程序。

  Beautiful Soup自动将输入文档转换为Unicode编码，输出文档转换为UTF-8编码。你不需要考虑编码方式，除非文档没有指定一个编码方式，这时你仅仅需要说明一下原始编码方式就可以了。

  Beautiful Soup已成为和lxml、html6lib一样出色的Python解释器，为用户灵活地提供不同的解析策略或强劲的速度。
```

所以说，利用它可以省去很多烦琐的提取工作，提高了解析效率。

### 2、解释器

Beautiful Soup在解析时实际上依赖解析器，它除了支持Python标准库中的HTML解析器外，还支持一些第三方解析器（比如lxml）。下表列出了Beautiful Soup支持的解析器。

| 解析器          | 使用方法                               | 优势                                                      | 劣势                                               |
| --------------- | -------------------------------------- | --------------------------------------------------------- | -------------------------------------------------- |
| Python标准库    | `BeautifulSoup(markup, "html.parser")` | Python的内置标准库、执行速度适中、文档容错能力强          | Python 2.7.3及Python 3.2.2之前的版本文档容错能力差 |
| lxml HTML解析器 | `BeautifulSoup(markup, "lxml")`        | 速度快、文档容错能力强                                    | 需要安装C语言库                                    |
| lxml XML解析器  | `BeautifulSoup(markup, "xml")`         | 速度快、唯一支持XML的解析器                               | 需要安装C语言库                                    |
| html5lib        | `BeautifulSoup(markup, "html5lib")`    | 最好的容错性、以浏览器的方式解析文档、生成HTML5格式的文档 | 速度慢、不依赖外部扩展                             |

通过以上对比可以看出，lxml解析器有解析HTML和XML的功能，而且速度快，容错能力强，所以推荐使用它。

如果使用lxml，那么在初始化Beautiful Soup时，可以把第二个参数改为`lxml`即可：

```python
from bs4 import BeautifulSoup

soup = BeautifulSoup('<p>Hello</p>', 'lxml')
print(soup.p.string)
```

在后面，Beautiful Soup的用法实例也统一用这个解析器来演示。

### 3、基本用法

**示例1：Beautiful Soup的基本用法：**

```python
from bs4 import BeautifulSoup

html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""

soup = BeautifulSoup(html, 'lxml')
print(soup.prettify())
print(soup.title.string)

'''
#返回值
<html>
 <head>
  <title>
   The Dormouse's story
  </title>
 </head>
 <body>
  <p class="title" name="dromouse">
   <b>
    The Dormouse's story
   </b>
  </p>
  <p class="story">
   Once upon a time there were three little sisters; and their names were
   <a class="sister" href="http://example.com/elsie" id="link1">
    <!-- Elsie -->
   </a>
   ,
   <a class="sister" href="http://example.com/lacie" id="link2">
    Lacie
   </a>
   and
   <a class="sister" href="http://example.com/tillie" id="link3">
    Tillie
   </a>
   ;
and they lived at the bottom of a well.
  </p>
  <p class="story">
   ...
  </p>
 </body>
</html>
The Dormouse's story
'''
```

- 声明变量HTML，它是一个HTML字符串。但是需要注意的是，它并不是一个完整的HTML字符串，因为`body`和`html`节点都没有闭合。

- 我们将它当作第一个参数传给`BeautifulSoup`对象，该对象的第二个参数为解析器的类型（这里使用`lxml`），此时就完成了`BeaufulSoup`对象的初始化。然后，将这个对象赋值给`soup`变量。
- 接下来，就可以调用`soup`的各个方法和属性解析这串HTML代码了。
- 首先，调用`prettify()`方法。这个方法可以把要解析的字符串以标准的缩进格式输出。这里需要注意的是，输出结果里面包含`body`和`html`节点，也就是说对于不标准的HTML字符串`BeautifulSoup`，可以自动更正格式。这一步不是由`prettify()`方法做的，而是在初始化`BeautifulSoup`时就完成了。
- 然后调用`soup.title.string`，这实际上是输出HTML中`title`节点的文本内容。所以，`soup.title`可以选出HTML中的`title`节点，再调用`string`属性就可以得到里面的文本了，所以我们可以通过简单调用几个属性完成文本提取

### 4、节点选择器

直接调用节点的名称就可以选择节点元素，再调用`string`属性就可以得到节点内的文本了，这种选择方式速度非常快。如果单个节点结构层次非常清晰，可以选用这种方式来解析。

**示例1：选择元素**

```python
from bs4 import BeautifulSoup

html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""

soup = BeautifulSoup(html,'lxml')
print(soup.title)      #查看html中title节点
print(type(soup.title))   #查看html中title节点类型
print(soup.title.string)     #查看html中title节点文本
print(soup.head)   #查看html中head节点
print(soup.p)  #查看html中p节点

'''
#返回值
<title>The Dormouse's story</title>
<class 'bs4.element.Tag'>
The Dormouse's story
<head><title>The Dormouse's story</title></head>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
'''
```

- 这里依然选用刚才的HTML代码，首先打印输出`title`节点的选择结果，输出结果正是`title`节点加里面的文字内容。
- 接下来，输出它的类型，是`bs4.element.Tag`类型，这是Beautiful Soup中一个重要的数据结构。经过选择器选择后，选择结果都是这种`Tag`类型。`Tag`具有一些属性，比如`string`属性，调用该属性，可以得到节点的文本内容，所以接下来的输出结果正是节点的文本内容。

- 接下来，我们又尝试选择了`head`节点，结果也是节点加其内部的所有内容。
- 最后，选择了`p`节点。不过这次情况比较特殊，我们发现结果是第一个`p`节点的内容，后面的几个`p`节点并没有选到。也就是说，当有多个节点时，这种选择方式只会选择到第一个匹配的节点，其他的后面节点都会忽略。

**示例2：获取节点属性的值**

上面演示了调用`string`属性来获取文本的值，那么如何获取节点属性的值呢？如何获取节点名呢？下面我们来统一梳理一下信息的提取方式。

##### (1)获取名称

可以利用`name`属性获取节点的名称。这里还是以上面的文本为例，选取`title`节点，然后调用`name`属性就可以得到节点名称：

```python
soup = BeautifulSoup(html,'lxml')
print(soup.title.name)

'''
title
'''
```

##### (2)获取属性

每个节点可能有多个属性，比如`id`和`class`等，选择这个节点元素后，可以调用`attrs`获取所有属性：

```python
soup = BeautifulSoup(html,'lxml')
print(soup.p.attrs)
print(soup.p.attrs['name'])

'''
#返回值
{'class': ['title'], 'name': 'dromouse'}
dromouse
'''
```

可以看到，`attrs`的返回结果是字典形式，它把选择的节点的所有属性和属性值组合成一个字典。接下来，如果要获取`name`属性，就相当于从字典中获取某个键值，只需要用中括号加属性名就可以了。比如，要获取`name`属性，就可以通过`attrs['name']`来得到。

其实这样有点烦琐，还有一种更简单的获取方式：可以不用写`attrs`，直接在节点元素后面加中括号，传入属性名就可以获取属性值了。样例如下：

```python
soup = BeautifulSoup(html,'lxml')
print(soup.p['name'])
print(soup.p['class'])

'''
#返回值
dromouse
['title']
'''
```

这里需要注意的是，有的返回结果是字符串，有的返回结果是字符串组成的列表。比如，`name`属性的值是唯一的，返回的结果就是单个字符串。而对于`class`，一个节点元素可能有多个`class`，所以返回的是列表。在实际处理过程中，我们要注意判断类型。

##### (3)获取内容

可以利用`string`属性获取节点元素包含的文本内容，比如要获取第一个`p`节点的文本：

```python
print(soup.p.string)

'''
返回值
The Dormouse's story
'''
```

再次注意一下，这里选择到的`p`节点是第一个`p`节点，获取的文本也是第一个`p`节点里面的文本

**示例3：嵌套选择**

在上面的例子中，我们知道每一个返回结果都是`bs4.element.Tag`类型，它同样可以继续调用节点进行下一步的选择。比如，我们获取了`head`节点元素，我们可以继续调用`head`来选取其内部的`title`节点元素：

```python
from bs4 import BeautifulSoup

html = """
<html><head><title>The Dormouse's story</title></head>
<body>
"""

soup = BeautifulSoup(html, 'lxml')
print(soup.head.title)
print(type(soup.head.title))
print(soup.head.title.string)

'''
<title>The Dormouse's story</title>
<class 'bs4.element.Tag'>
The Dormouse's story
'''
```

直接获取head子节点title节点的文本内容，是不是很棒棒。。。

##### **示例4：关联选择**

在做选择的时候，有时候不能做到一步就选到想要的节点元素，需要先选中某一个节点元素，然后以它为基准再选择它的子节点、父节点、兄弟节点等，这里就来介绍如何选择这些节点元素。

##### (1)子节点和子孙节点

选取节点元素之后，如果想要获取它的直接子节点，可以调用`contents`属性，示例如下：

```python
from bs4 import BeautifulSoup

html = """
<html>
    <head>
        <title>The Dormouse's story</title>
    </head>
    <body>
        <p class="story">
            Once upon a time there were three little sisters; and their names were
            <a href="http://example.com/elsie" class="sister" id="link1">
                <span>Elsie</span>
            </a>
            <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> 
            and
            <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>
            and they lived at the bottom of a well.
        </p>
        <p class="story">...</p>
"""

soup = BeautifulSoup(html,'lxml')
print(soup.p.contents)
        
'''
['\n            Once upon a time there were three little sisters; and their names were\n            ', <a class="sister" href="http://example.com/elsie" id="link1">
<span>Elsie</span>
</a>, '\n', <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>, ' \n            and\n            ', <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>, '\n            and they lived at the bottom of a well.\n        ']
'''    
```

可以看到，返回结果是列表形式。`p`节点里既包含文本，又包含节点，最后会将它们以列表形式统一返回。

需要注意的是，列表中的每个元素都是`p`节点的直接子节点。比如第一个`a`节点里面包含一层`span`节点，这相当于孙子节点了，但是返回结果并没有单独把`span`节点选出来。所以说，`contents`属性得到的结果是直接子节点的列表。

同样，我们可以调用`children`属性得到相应的结果：

```python
...其他代码同上
soup = BeautifulSoup(html, 'lxml')
print(soup.p.children)
for i, child in enumerate(soup.p.children):
    print(i, child)
    
'''
返回值
0 
            Once upon a time there were three little sisters; and their names were
            
1 <a class="sister" href="http://example.com/elsie" id="link1">
<span>Elsie</span>
</a>
2 

3 <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>
4  
            and
            
5 <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>
6 
            and they lived at the bottom of a well.
'''
```

还是同样的HTML文本，这里调用了`children`属性来选择，返回结果是生成器类型。接下来，我们用`for`循环输出相应的内容。

如果要得到所有的子孙节点的话，可以调用`descendants`属性：

```python
...其他代码同上
soup = BeautifulSoup(html, 'lxml')
print(soup.p.descendants)
for i, child in enumerate(soup.p.descendants):
    print(i, child)

'''
<generator object Tag.descendants at 0x0000022E3FCEBF48>
0 
            Once upon a time there were three little sisters; and their names were
            
1 <a class="sister" href="http://example.com/elsie" id="link1">
<span>Elsie</span>
</a>
2 

3 <span>Elsie</span>
4 Elsie
5 

6 

7 <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>
8 Lacie
9  
            and
            
10 <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>
11 Tillie
12 
            and they lived at the bottom of a well.
'''
```

此时返回结果还是生成器。遍历输出一下可以看到，这次的输出结果就包含了`span`节点。`descendants`会递归查询所有子节点，得到所有的子孙节点。

##### (2)父节点和祖先节点

如果要获取某个节点元素的父节点，可以调用`parent`属性：

```python
...其他代码同上

soup = BeautifulSoup(html, 'lxml')
print(soup.a.parent)

'''
#返回值
<p class="story">
            Once upon a time there were three little sisters; and their names were
            <a class="sister" href="http://example.com/elsie" id="link1">
<span>Elsie</span>
</a>
<a class="sister" href="http://example.com/lacie" id="link2">Lacie</a> 
            and
            <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>
            and they lived at the bottom of a well.
        </p>
'''
```

这里我们选择的是第一个`a`节点的父节点元素。很明显，它的父节点是`p`节点，输出结果便是`p`节点及其内部的内容。

需要注意的是，这里输出的仅仅是`a`节点的直接父节点，而没有再向外寻找父节点的祖先节点。如果想获取所有的祖先节点，可以调用`parents`属性：


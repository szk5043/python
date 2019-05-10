## 一、XPath的使用

### 1、XPath概述

XPath的选择功能十分强大，它提供了非常简洁明了的路径选择表达式。另外，它还提供了超过100个内建函数，用于字符串、数值、时间的匹配以及节点、序列的处理等。几乎所有我们想要定位的节点，都可以用XPath来选择。

XPath于1999年11月16日成为W3C标准，它被设计为供XSLT、XPointer以及其他XML解析软件使用，更多的文档可以访问其官方网站：<https://www.w3.org/TR/xpath/>。

### 2. XPath常用规则

列举了XPath的几个常用规则。

| 表达式     | 描述                     |
| ---------- | ------------------------ |
| `nodename` | 选取此节点的所有子节点   |
| `/`        | 从当前节点选取直接子节点 |
| `//`       | 从当前节点选取子孙节点   |
| `.`        | 选取当前节点             |
| `..`       | 选取当前节点的父节点     |
| `@`        | 选取属性                 |

这里列出了XPath的常用匹配规则，示例如下：

```python
//title[@lang='eng']
```

这就是一个XPath规则，它代表选择所有名称为`title`，同时属性`lang`的值为`eng`的节点。

后面会通过Python的lxml库，利用XPath进行HTML的解析。



**示例1：etree模块可以自动修正HTML文本**

```python
from lxml import etree

text = '''
<div>
    <ul>
         <li class="item-0"><a href="link1.html">first item</a></li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-inactive"><a href="link3.html">third item</a></li>
         <li class="item-1"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a>
     </ul>
 </div>
'''
html = etree.HTML(text)
result = etree.tostring(html)
print(result.decode('utf-8'))

'''
<html><body><div>
    <ul>
         <li class="item-0"><a href="link1.html">first item</a></li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-inactive"><a href="link3.html">third item</a></li>
         <li class="item-1"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a>
     </li></ul>
 </div>
</body></html>
'''
```

> HTML文本中的最后一个`li`节点是没有闭合的，已被修正

从文件文件进行解析，test.html的内容就是上面例子中的HTML代码，内容如下：

```html
<html><body><div>
    <ul>
         <li class="item-0"><a href="link1.html">first item</a></li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-inactive"><a href="link3.html">third item</a></li>
         <li class="item-1"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a>
     </li></ul>
 </div>
</body></html>
```
python代码：
```python
from lxml import etree

html = etree.parse('./test.html', etree.HTMLParser())
result = etree.tostring(html)
print(result.decode('utf-8'))

'''
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN" "http://www.w3.org/TR/REC-html40/loose.dtd">
<html><body><div>&#13;
    <ul>&#13;
         <li class="item-0"><a href="link1.html">first item</a></li>&#13;
         <li class="item-1"><a href="link2.html">second item</a></li>&#13;
         <li class="item-inactive"><a href="link3.html">third item</a></li>&#13;
         <li class="item-1"><a href="link4.html">fourth item</a></li>&#13;
         <li class="item-0"><a href="link5.html">fifth item</a>&#13;
     </li></ul>&#13;
 </div></body></html>
'''
```

> 这次不仅修正了`li`节点，还自动补上了`body`标签、`html`标签和`!DOCTYPE html`文档类型注释



**示例2：`etree.HTMLParser()`方法获取HTML标签**

**第一步**，先获取HTML所有标签

```python
from lxml import etree

html = etree.parse('./test.html', etree.HTMLParser())
result = html.xpath('//*')
print(result)

'''
[<Element html at 0x1bf451f6ec8>, <Element body at 0x1bf451f6e88>, <Element div at 0x1bf451f6f88>, <Element ul at 0x1bf451f6fc8>, <Element li at 0x1bf45202048>, <Element a at 0x1bf452020c8>, <Element li at 0x1bf45202108>, <Element a at 0x1bf45202148>, <Element li at 0x1bf45202188>, <Element a at 0x1bf45202088>, <Element li at 0x1bf452021c8>, <Element a at 0x1bf45202208>, <Element li at 0x1bf45202248>, <Element a at 0x1bf45202288>]
'''
```

这里使用*代表匹配所有节点，也就是整个HTML文本中的所有节点都会被获取。可以看到，返回形式是一个列表，每个元素是`Element`类型，其后跟了节点的名称，如`html`、`body`、`div`、`ul`、`li`、`a`等，所有节点都包含在列表中了。当然，此处匹配也可以指定节点名称。

**第二步**，获取指定HTML标签。如果想获取所有`li`节点，示例如下：

```python
from lxml import etree

html = etree.parse('./test.html', etree.HTMLParser())
result = html.xpath('//li')
print(result)

'''
[<Element li at 0x1dd5c9a8e48>, <Element li at 0x1dd5c9a8e88>, <Element li at 0x1dd5c9a8ec8>, <Element li at 0x1dd5c9a8f08>, <Element li at 0x1dd5c9a8f48>]
'''
```

**第三步**，获取指定元素的子节点或子孙节点。假如现在想选择`li`节点的所有直接`a`子节点，可以这样实现：

```python
from lxml import etree

html = etree.parse('./test.html', etree.HTMLParser())
result = html.xpath('//li/a')
print(result)

'''
[<Element a at 0x1c677792048>, <Element a at 0x1c677792088>, <Element a at 0x1c6777920c8>, <Element a at 0x1c677792108>, <Element a at 0x1c677792148>]
'''
```

这里通过追加`/a`即选择了所有`li`节点的所有直接`a`子节点。因为`//li`用于选中所有`li`节点，`/a`用于选中`li`节点的所有直接子节点`a`，二者组合在一起即获取所有`li`节点的所有直接`a`子节点。

> 因此，这里我们要注意`/`和`//`的区别，其中`/`用于获取直接子节点，`//`用于获取子孙节点。



**示例3：获取HTML指定节点的属性**

比如，现在首先选中`href`属性为`link4.html`的`a`节点，然后再获取其父节点，然后再获取其`class`属性，相关代码如下：

```python
from lxml import etree

html = etree.parse('./test.html', etree.HTMLParser())
result = html.xpath('//a[@href="link4.html"]/../@class')
print(result)

'''
['item-1']
'''
```

检查一下结果发现，这正是我们获取的目标`li`节点的`class`。

同时，我们也可以通过`parent::`来获取父节点，代码如下：

```python
from lxml import etree

html = etree.parse('./test.html', etree.HTMLParser())
result = html.xpath('//a[@href="link4.html"]/parent::*/@class')
print(result)
```

在选取的时候，我们还可以用`@`符号进行属性过滤。比如，这里如果要选取`class`为`item-1`的`li`节点，可以这样实现:

```python
from lxml import etree

html = etree.parse('./test.html', etree.HTMLParser())
result = html.xpath('//li[@class="item-0"]')
print(result)

'''
[<Element li at 0x1cc50267ec8>, <Element li at 0x1cc50267f08>]
'''
```

这里我们通过加入`[@class="item-0"]`，限制了节点的`class`属性为`item-0`，而HTML文本中符合条件的`li`节点有两个，所以结果应该返回两个匹配到的元素。

例如，我们想获取所有`li`节点下所有`a`节点的`href`属性，代码如下：

```python
from lxml import etree

html = etree.parse('./test.html', etree.HTMLParser())
result = html.xpath('//li/a/@href')
print(result)

'''
['link1.html', 'link2.html', 'link3.html', 'link4.html', 'link5.html']
'''
```

这里我们通过`@href`即可获取节点的`href`属性。注意，此处和属性匹配的方法不同，属性匹配是中括号加属性名和值来限定某个属性，如`[@href="link1.html"]`，而此处的`@href`指的是获取节点的某个属性，二者需要做好区分。

**示例4：获取HTML节点中的文本信息**

接下来尝试获取前面`li`节点中的文本，相关代码如下：

```python
from lxml import etree

html = etree.parse('./test.html', etree.HTMLParser())
result = html.xpath('//li[@class="item-0"]/a/text()')
print(result)

'''
['first item', 'fifth item']
'''
```

可以看到，这里的返回值是两个，内容都是属性为`item-0`的`li`节点的文本，这也印证了前面属性匹配的结果是正确的。

这里我们是逐层选取的，先选取了`li`节点，又利用`/`选取了其直接子节点`a`，然后再选取其文本，得到的结果恰好是符合我们预期的两个结果。

再来看下用另一种方式（即使用`//`）选取的结果，代码如下：

```python
from lxml import etree

html = etree.parse('./test.html', etree.HTMLParser())
result = html.xpath('//li[@class="item-0"]//text()')
print(result)

'''
['first item', 'fifth item', '\r\n     ']
'''
```

不出所料，这里的返回结果是3个。可想而知，这里是选取所有子孙节点的文本，其中前两个就是`li`的子节点`a`节点内部的文本，另外一个就是最后一个`li`节点内部的文本，即换行符。

所以说，如果要想获取子孙节点内部的所有文本，可以直接用`//`加`text()`的方式，这样可以保证获取到最全面的文本信息，但是可能会夹杂一些换行符等特殊字符。如果想获取某些特定子孙节点下的所有文本，可以先选取到特定的子孙节点，然后再调用`text()`方法获取其内部文本，这样可以保证获取的结果是整洁的。

**示例5：属性多值匹配**

有时候，某些节点的某个属性可能有多个值，例如：`<li class="li li-first"><a href="link.html">first item</a></li>`中`li`节点的`class`属性有两个值`li`和`li-first`，此时如果还想用之前的属性匹配获取，就无法匹配了，这时就需要用`contains()`函数了，代码如下：

```python
from lxml import etree

text = '''
<li class="li li-first"><a href="link.html">first item</a></li>
'''

html = etree.HTML(text)
result = html.xpath('//li[contains(@class, "li")]/a/text()')
print(result)

'''
['first item']
'''
```

这样通过`contains()`方法，第一个参数传入属性名称，第二个参数传入属性值，只要此属性包含所传入的属性值，就可以完成匹配了。

**示例6：多属性匹配**

根据多个属性确定一个节点，这时就需要同时匹配多个属性。此时可以使用运算符`and`来连接，示例如下：

```python
from lxml import etree

text = '''
<li class="li li-first" name="item"><a href="link.html">first item</a></li>
'''

html = etree.HTML(text)
result = html.xpath('//li[contains(@class, "li") and @name="item"]/a/text()')
print(result)

'''
['first item']
'''
```

这里的`li`节点又增加了一个属性`name`。要确定这个节点，需要同时根据`class`和`name`属性来选择，一个条件是`class`属性里面包含`li`字符串，另一个条件是`name`属性为`item`字符串，二者需要同时满足，需要用`and`操作符相连，相连之后置于中括号内进行条件筛选。

这里的`and`其实是XPath中的运算符。另外，还有很多运算符，如`or`、`mod`等，在此总结为下表。

| 运算符 | 描述           | 实例                | 返回值                                                      |
| ------ | -------------- | ------------------- | ----------------------------------------------------------- |
| `or`   | 或             | `age=19 or age=20`  | 如果`age`是19，则返回`true`。如果`age`是21，则返回`false`   |
| `and`  | 与             | `age>19 and age<21` | 如果`age`是20，则返回`true`。如果`age`是`18`，则返回`false` |
| `mod`  | 计算除法的余数 | `5 mod 2`           | 1                                                           |
| `|`    | 计算两个节点集 | `//book | //cd`     | 返回所有拥有`book`和`cd`元素的节点集                        |
| `+`    | 加法           | `6 + 4`             | 10                                                          |
| `-`    | 减法           | `6 - 4`             | 2                                                           |
| `*`    | 乘法           | `6 * 4`             | 24                                                          |
| `div`  | 除法           | `8 div 4`           | 2                                                           |
| `=`    | 等于           | `age=19`            | 如果`age`是19，则返回`true`。如果`age`是20，则返回`false`   |
| `!=`   | 不等于         | `age!=19`           | 如果`age`是18，则返回`true`。如果`age`是19，则返回`false`   |
| `<`    | 小于           | `age<19`            | 如果`age`是18，则返回`true`。如果`age`是19，则返回`false`   |
| `<=`   | 小于或等于     | `age<=19`           | 如果`age`是19，则返回`true`。如果`age`是20，则返回`false`   |
| `>`    | 大于           | `age>19`            | 如果`age`是20，则返回`true`。如果`age`是19，则返回`false`   |
| `>=`   | 大于或等于     | `age>=19`           | 如果`age`是19，则返回`true`。如果`age`是18，则返回`false`   |

此表参考来源：<http://www.w3school.com.cn/xpath/xpath_operators.asp>。

### 3、按序选择

有时候，我们在选择的时候某些属性可能同时匹配了多个节点，但是只想要其中的某个节点，如第二个节点或者最后一个节点，这时该怎么办呢？

这时可以利用中括号传入索引的方法获取特定次序的节点，示例如下：

```python
from lxml import etree

text = '''
<div>
    <ul>
         <li class="item-0"><a href="link1.html">first item</a></li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-inactive"><a href="link3.html">third item</a></li>
         <li class="item-1"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a>
     </ul>
 </div>
'''

html = etree.HTML(text)
result = html.xpath('//li[1]/a/text()')
print(result)
result = html.xpath('//li[last()]/a/text()')
print(result)
result = html.xpath('//li[position()<3]/a/text()')
print(result)
result = html.xpath('//li[last()-2]/a/text()')
print(result)

'''
['first item']
['fifth item']
['first item', 'second item']
['third item']
'''
```

第一次选择时，我们选取了第一个`li`节点，中括号中传入数字1即可。注意，这里和代码中不同，序号是以1开头的，不是以0开头。

第二次选择时，我们选取了最后一个`li`节点，中括号中传入`last()`即可，返回的便是最后一个`li`节点。

第三次选择时，我们选取了位置小于3的`li`节点，也就是位置序号为1和2的节点，得到的结果就是前两个`li`节点。

第四次选择时，我们选取了倒数第三个`li`节点，中括号中传入`last()-2`即可。因为`last()`是最后一个，所以`last()-2`就是倒数第三个。

这里我们使用了`last()`、`position()`等函数。在XPath中，提供了100多个函数，包括存取、数值、字符串、逻辑、节点、序列等处理功能，它们的具体作用可以参考：<http://www.w3school.com.cn/xpath/xpath_functions.asp>。

### 4、节点轴选择

XPath提供了很多节点轴选择方法，包括获取子元素、兄弟元素、父元素、祖先元素等，示例如下：

```python
from lxml import etree

text = '''
<div>
    <ul>
         <li class="item-0"><a href="link1.html"><span>first item</span></a></li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-inactive"><a href="link3.html">third item</a></li>
         <li class="item-1"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a>
     </ul>
 </div>
'''

html = etree.HTML(text)
result = html.xpath('//li[1]/ancestor::*')
print(result)
result = html.xpath('//li[1]/ancestor::div')
print(result)
result = html.xpath('//li[1]/attribute::*')
print(result)
result = html.xpath('//li[1]/child::a[@href="link1.html"]')
print(result)
result = html.xpath('//li[1]/descendant::span')
print(result)
result = html.xpath('//li[1]/following::*[2]')
print(result)
result = html.xpath('//li[1]/following-sibling::*')<code class="lang-python">
<span class="kwd">print</span><span class="pun">(</span><span class="pln">result</span><span class="pun">)</span>

'''
[<Element html at 0x107941808>, <Element body at 0x1079418c8>, <Element div at 0x107941908>, <Element ul at 0x107941948>]
[<Element div at 0x107941908>]
['item-0']
[<Element a at 0x1079418c8>]
[<Element span at 0x107941948>]
[<Element a at 0x1079418c8>]
[<Element li at 0x107941948>, <Element li at 0x107941988>, <Element li at 0x1079419c8>, <Element li at 0x107941a08>]
'''
```

第一次选择时，我们调用了`ancestor`轴，可以获取所有祖先节点。其后需要跟两个冒号，然后是节点的选择器，这里我们直接使用*，表示匹配所有节点，因此返回结果是第一个`li`节点的所有祖先节点，包括`html`、`body`、`div`和`ul`。

第二次选择时，我们又加了限定条件，这次在冒号后面加了`div`，这样得到的结果就只有`div`这个祖先节点了。

第三次选择时，我们调用了`attribute`轴，可以获取所有属性值，其后跟的选择器还是*，这代表获取节点的所有属性，返回值就是`li`节点的所有属性值。

第四次选择时，我们调用了`child`轴，可以获取所有直接子节点。这里我们又加了限定条件，选取`href`属性为`link1.html`的`a`节点。

第五次选择时，我们调用了`descendant`轴，可以获取所有子孙节点。这里我们又加了限定条件获取`span`节点，所以返回的结果只包含`span`节点而不包含`a`节点。

第六次选择时，我们调用了`following`轴，可以获取当前节点之后的所有节点。这里我们虽然使用的是*匹配，但又加了索引选择，所以只获取了第二个后续节点。

第七次选择时，我们调用了`following-sibling`轴，可以获取当前节点之后的所有同级节点。这里我们使用*匹配，所以获取了所有后续同级节点。

### 5、小结

以上是XPath轴的简单用法，更多轴的用法可以参考：<http://www.w3school.com.cn/xpath/xpath_axes.asp>。

到现在为止，我们基本上把可能用到的XPath选择器介绍完了。XPath功能非常强大，内置函数非常多，熟练使用之后，可以大大提升HTML信息的提取效率。

如果想查询更多XPath的用法，可以查看：<http://www.w3school.com.cn/xpath/index.asp>。

如果想查询更多Python lxml库的用法，可以查看<http://lxml.de/>。

转载请注明：[静觅](https://cuiqingcai.com) » [[Python3网络爬虫开发实战\] 4.1-使用XPath](https://cuiqingcai.com/5545.html)
## 一、urllib

### 1、概述

urllib是Python内置的HTTP请求库，无需安装即可使用。

urllib包含4个模块：

- **request**：它是最基本的HTTP请求模块，可以用来模拟发送请求。就像在浏览器里输入网址然后回车一样，只需要给库方法传入URL以及额外的参数，就可以模拟实现这个过程了。
- **error**：异常处理模块，如果出现请求错误，我们可以捕获这些异常，然后进行重试或其他操作以保证程序不会意外终止。
- **parse**：一个工具模块，提供了许多URL处理方法，比如拆分、解析、合并等。
- **robotparser**：主要是用来识别网站的robots.txt文件，然后判断哪些网站可以爬，哪些网站不可以爬，它其实用得比较少。

### 2、发送请求
**`urlopen()`**
urllib.request`模块提供了最基本的构造HTTP请求的方法，利用它可以模拟浏览器的一个请求发起过程，同时它还带有处理授权验证（authenticaton）、重定向（redirection)、浏览器Cookies以及其他内容。

下面我们来看一下它的强大之处。这里以baidu官网为例，我们来把这个网页抓下来：

```python
import urllib.request

response = urllib.request.urlopen('http://www.baidu.com/')
print(response.read().decode('utf-8'))
```

接下来，看看它返回的到底是什么。利用`type()`方法输出响应的类型：

```python
print(type(response))

'''
#返回值
<class 'http.client.HTTPResponse'>
'''
```

可以发现，它是一个`HTTPResposne`类型的对象。它主要包含`read()`、`readinto()`、`getheader(name)`、`getheaders()`、`fileno()`等方法，以及`msg`、`version`、`status`、`reason`、`debuglevel`、`closed`等属性。

得到这个对象之后，我们把它赋值为`response`变量，然后就可以调用这些方法和属性，得到返回结果的一系列信息了。

例如，调用`read()`方法可以得到返回的网页内容，调用`status`属性可以得到返回结果的状态码，如200代表请求成功，404代表网页未找到等。

下面再通过一个实例来看看：

```python
import urllib.request

response = urllib.request.urlopen('http://www.baidu.com/')
print(response.status)
print(response.getheaders())
print(response.getheader('Server'))

'''
#返回值：
200
[('Date', 'Wed, 24 Apr 2019 12:22:14 GMT'), ('Content-Type', 'text/html'), ('Transfer-Encoding', 'chunked'), ('Connection', 'Close'), ('Vary', 'Accept-Encoding'), ('Set-Cookie', 'BAIDUID=2CAF4EEC54C93A87BEA59A5A3A27E45D:FG=1; expires=Thu, 31-Dec-37 23:55:55 GMT; max-age=2147483647; path=/; domain=.baidu.com'),.....]
BWS/1.1
'''
```

可见，前两个输出分别输出了响应的状态码和响应的头信息，最后一个输出通过调用`getheader()`方法并传递一个参数`Server`获取了响应头中的`Server`值，结果是`nginx`，意思是服务器是用Nginx搭建的。

利用最基本的`urlopen()`方法，可以完成最基本的简单网页的GET请求抓取。

如果想给链接传递一些参数，该怎么实现呢？首先看一下`urlopen()`函数的API：

```python
urllib.request.urlopen(url, data=None, [timeout, ]*, cafile=None, capath=None, cadefault=False, context=None)
```

可以发现，除了第一个参数可以传递URL之外，我们还可以传递其他内容，比如`data`（附加数据）、`timeout`（超时时间）等。

下面我们详细说明下这几个参数的用法。

 **`data`参数** 

`data`参数是可选的。如果要添加该参数，并且如果它是字节流编码格式的内容，即`bytes`类型，则需要通过`bytes()`方法转化。另外，如果传递了这个参数，则它的请求方式就不再是GET方式，而是POST方式。

下面用实例来看一下：

```python
import urllib.parse
import urllib.request

data = bytes(urllib.parse.urlencode({'word': 'hello'}), encoding='utf8')
response = urllib.request.urlopen('http://httpbin.org/post', data=data)
print(response.read())
```

这里我们传递了一个参数`word`，值是`hello`。它需要被转码成`bytes`（字节流）类型。其中转字节流采用了`bytes()`方法，该方法的第一个参数需要是`str`（字符串）类型，需要用`urllib.parse`模块里的`urlencode()`方法来将参数字典转化为字符串；第二个参数指定编码格式，这里指定为`utf8`。

这里请求的站点是httpbin.org，它可以提供HTTP请求测试。本次我们请求的URL为<http://httpbin.org/post>，这个链接可以用来测试POST请求，它可以输出请求的一些信息，其中包含我们传递的`data`参数。

运行结果如下：




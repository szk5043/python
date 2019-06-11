## 六、网络编程只SocketServer实现多并发

### 1、概述

在现实生活中 , 一个服务端肯定常常需要同时服务好几个客户端 , 而上述篇章中并没有实现一对多同时进行的情况 , 
TCP中只能等前一个链接断开后续的才能连上 , 没连上就一直等 ; UDP则是接一次发一次 , 并不能同时接两次发两次 . 为了处理这个问题 ,即实现并发 (后续文章详细讲解) , Python中有一个socketserver模块可以满足我们的要求。

### 2、SocketServer

Python提供了两个级别访问的网络服务:

- 低级别的网络服务支持基本的socket , 它提供了标准的BSD Socket API , 可以访问底层操作系统Socket接口的全部方法

- 高级别的网络服务模块socketserver , 它提供了服务器中心类 , 可以简化网络服务器的开发

socket就不用说了 , now socketserver

我们知道基于TCP的套接字 , 关键就是两个循环 , 一个链接循环(多人) , 一个通信循环(多消息)

在socketserver模块中分为两大类 : server类 (解决链接问题) 和request类 (解决通信问题) 

如果想进一步了解 , 可以看看官方文档 , < [socketserver官方文档 ](https://docs.python.org/3/library/socketserver.html?highlight=socketserver#module-socketserver)>

### 3、实现TCP多并发

实现步骤：

- 定义一个class，继承`socketserver.BaseRequestHandler`类
- 使用`socketserver.BaseRequestHandler`类中的handle方法实现链接循环
- handle有两个属性：
	- `self.request.recv` 对应 socket中的recv属性
	- `self.request.send` 对应 socket中的send属性
- 实例化`socketserver.ThreadingTCPServer`对象
  - 第一个参数传入IP+Port元组
  - 第二个参数传入定义的类

**示例1：实现链接循环**

*server*

```python
import socketserver

class MyTCPhanler(socketserver.BaseRequestHandler):
    def handle(self):  #实现连接循环
        self.data = self.request.recv(1024).strip()
        print(self.client_address)
        print(self.data.decode('utf-8'))

if __name__ == '__main__':
    server = socketserver.ThreadingTCPServer(('127.0.0.1',8888),MyTCPhanler)
    server.serve_forever()    #对外提供服务
```

*client1*

```python
from socket import *

client = socket(AF_INET, SOCK_STREAM)
client.connect(('127.0.0.1', 8888))
client.send('client1'.encode('utf-8'))
client.close()
```

*client2*

```python
from socket import *

client = socket(AF_INET, SOCK_STREAM)
client.connect(('127.0.0.1', 8888))
client.send('client2'.encode('utf-8'))
client.close()
```

*server端交互*

```python
('127.0.0.1', 50511)
client1
('127.0.0.1', 50512)
client2
```

server.serve_forever()`实现的是连接循环，`handle`方法里面的`while True`实现通信循环，看示例2

**示例2：实现连接循环、通信循环**

*server*

```python
import socketserver

class MyTCPhanler(socketserver.BaseRequestHandler):
    def handle(self):          #实现链接循环
        while True:            #实现通信循环
            try:
                self.data = self.request.recv(1024).strip()
                print(self.client_address)
                self.request.send(self.data.upper())
            except ConnectionRefusedError:
                break
        self.request.close()


if __name__ == '__main__':
    server = socketserver.ThreadingTCPServer(('127.0.0.1',8888),MyTCPhanler)
    server.serve_forever()   
```

*client1*

```python
from socket import *
import time

client = socket(AF_INET, SOCK_STREAM)
client.connect(('127.0.0.1', 8888))

while True:   #通信循环
    client.send('client1'.encode('utf-8'))
    time.sleep(3)
    data = client.recv(1024)
    print(data)
client.close()
```

*client2*

```python
from socket import *
import time

client = socket(AF_INET, SOCK_STREAM)
client.connect(('127.0.0.1', 8888))

while True:   #通信循环
    client.send('client2'.encode('utf-8'))
    time.sleep(3)
    data = client.recv(1024)
    print(data)
client.close()
```

*server端交互*

```python
('127.0.0.1', 50797)
('127.0.0.1', 50798)
('127.0.0.1', 50797)
('127.0.0.1', 50798)
```

至此，实现的TCP多并发请求

### 4、实现UDP多并发请求

*server*

```python
import socketserver

class MyUdphandler(socketserver.BaseRequestHandler):
    def handle(self):
        data,sock = self.request
        print(self.client_address,'---->',data.decode())
        sock.sendto(data.upper(),self.client_address)

if __name__ == '__main__':
    server = socketserver.ThreadingUDPServer(('127.0.0.1',8888),MyUdphandler)
    server.serve_forever()


```

*client1*

```python
from socket import *
import time

client = socket(AF_INET,SOCK_DGRAM)

while True:
    client.sendto(b'client1',('127.0.0.1',8888))
    data , server_addr = client.recvfrom(1024)
    print(data)
    time.sleep(3)
client.close()

```

*client2*

 ```python
from socket import *
import time

client = socket(AF_INET,SOCK_DGRAM)

while True:
    client.sendto(b'client2',('127.0.0.1',8888))
    data , server_addr = client.recvfrom(1024)
    print(data)
    time.sleep(3)
client.close()

 ```

*server端交互*

```python
('127.0.0.1', 55172) ----> client1
('127.0.0.1', 64617) ----> client2
('127.0.0.1', 55172) ----> client1
('127.0.0.1', 64617) ----> client2
```

### 5、小结

基于TCP的SocketServer我们自定义的类中：

- `self.server`即套接字对象
- `self.requeest`即一个链接
- `self.client_address`即客户端地址

基于UDP的SocketServer我们自定义的类中：

- `self.requeest`是一个元组(第一个元素是客户端发来的数据，第二个元素是服务端的UDP套接字对象)，如`(b'client1', <socket.socket fd=3, family=AddressFamily.AF_INET, type=SocketKind.SOCK_DGRAM, proto=0, laddr=('127.0.0.1', 8888)>)`
- `self.client_address`即客户端地址`
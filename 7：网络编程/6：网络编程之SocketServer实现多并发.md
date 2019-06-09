六、网络编程只SocketServer实现多并发

1、概述

在现实生活中 , 一个服务端肯定常常需要同时服务好几个客户端 , 而上述篇章中并没有实现一对多同时进行的情况 , 
TCP中只能等前一个链接断开后续的才能连上 , 没连上就一直等 ; UDP则是接一次发一次 , 并不能同时接两次发两次 . 为了处理这个问题 ,即实现并发 (后续文章详细讲解) , Python中有一个socketserver模块可以满足我们的要求。

2、SocketServer

Python提供了两个级别访问的网络服务:

- 低级别的网络服务支持基本的socket , 它提供了标准的BSD Socket API , 可以访问底层操作系统Socket接口的全部方法

- 高级别的网络服务模块socketserver , 它提供了服务器中心类 , 可以简化网络服务器的开发

socket就不用说了 , now socketserver

我们知道基于TCP的套接字 , 关键就是两个循环 , 一个链接循环(多人) , 一个通信循环(多消息)

在socketserver模块中分为两大类 : server类 (解决链接问题) 和request类 (解决通信问题) 

如果想进一步了解 , 可以看看官方文档 , < [socketserver官方文档 ](https://docs.python.org/3/library/socketserver.html?highlight=socketserver#module-socketserver)>

3、实现多并发

*server*

```python
import socketserver

class MyBaby(socketserver.BaseRequestHandler):
    def handle(self):
        while True:
            try:
                data = self.request.recv(1024)
                print(data)
                self.request.send(data.upper())
            except ConnectionRefusedError:
                break

if __name__ == '__main__':
    server = socketserver.ThreadingTCPServer(('127.0.0.1',8888),MyBaby)
    server.serve_forever()
```

*client*

```python
import socket
import time

client = socket.socket()
client.connect(('127.0.0.1',8888))

while True:
    client.send(b'hello')
    data = client.recv(1024)
    print(data)
    time.sleep(1)
```


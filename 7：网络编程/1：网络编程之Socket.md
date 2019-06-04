## 一、网络编程之Socket

### 1、Socket概述

Socket是应用层与TCP/IP协议族通信的中间软件抽象层 , 它是一组接口 , 是从顶上三层 (osi七层协议的应用层) 进入传输层的接口 ; 顶上三层通常构成所谓的用户进程 , 底下四层却通常作为操作系统内核的一个部分提供

Socket又叫做套接字 , Python中socket为我们封装好了TCP/UDP协议 , 所以我们无需深入理解 , 只要遵循socket的规定去编程就可以了

### 2、Socket对象

**①、创建一个socket对象**

Socket在Python是一个封装好的类，可以拿来即用

示例1：创建一个Scoket对象

```python
# 导入socket模块
import socket

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM,0)
```
或者可以使用 from module import * ,可以大幅度减少代码,仅仅提一下,毕竟有弊端
```python
from socket import *

sock = socket(AF_INET,SOCK_STREAM,0)
```

**②、socket类参数说明**

其构造函数源码

```python
def __init__(self, family=AF_INET, type=SOCK_STREAM, proto=0, fileno=None):
    # 下面内容就不摘了
    pass
```

*family* : 地址簇

| 参数     | 说明                   |
| -------- | ---------------------- |
| AF_INET  | IPv4 , 即默认为IPv4    |
| AF_INET6 | IPv6                   |
| AF_UNIX  | 针对Unix系统进程间通信 |

*type* : 类型

| 参数           | 说明                                                         |
| -------------- | ------------------------------------------------------------ |
| SOCK_STREAM    | 面向流 , 即TCP                                               |
| SOCK_DGRAM     | 面向数据报 , 即UDP                                           |
| SOCK_RAW       | 原始套接字 , 可处理ICMP,IGMP等网络报文 ; 可以处理特殊的IPv4报文 ; 利用原始套接字 , 可以通过IP_HDRINCL套接字选项由用户构造IP头 |
| SOCK_RDM       | 一种可靠的UDP形式 . SOCK_RAM用来提供对原始协议的低级访问 , 在需要执行某些特殊操作时使用 , 如发送ICMP报文 , SOCK_RAW通常仅限于高级用户或管理员运行的程序使用 |
| SOCK_SEQPACKET | 可靠的连续数据包服务                                         |

*proto* : 协议

| 参数 | 说明                                                         |
| ---- | ------------------------------------------------------------ |
| 0    | 与特定的地址家族相关的协议 , 如果是0 , 则系统就会根据地址格式和套接类别 , 自动选择一个合适的协议 |

还有一个*fileno*参数是无需理会的

### 3、基于TCP的Socket

TCP协议是有链接的 , 面向流的 , 数据传输可靠 , 必须先启动服务端

**①、基于TCP协议的服务端创建流程**

- 创建套接字对象， *创建socket对象* 
- 绑定IP和端口，*绑定 bind()* 
- 开始监听链接，*监听 listen()* 

- 阻塞 , 等待客户端成功连接，*阻塞 accept()* 

- 接收请求数据，*接收 recv()* 

- 处理并发送请求数据，*发送 send()* 

- 通信完毕 , 关闭链接 , 关闭套接字，*关闭 close()*                    

**示例1：创建一个TCP服务端**

```python
import socket                    # 导入socket模块

sock = socket.socket()           # 创建socket对象
sock.bind(('127.0.0.1',8888))    # 绑定IP和端口
sock.listen(5)                   # 开始监听连接
conn,addr = sock.accept()        # 阻塞，等待客户端成功连接
conn.send(b'hello world')        # 发送请求结果，必须是bytes类型
conn.close()                     # 关闭连接
sock.close()                     # 关闭socket
```

**②、基于TCP协议的客户端创建流程**

- 创建套接字对象 ，*创建socket对象* 
- 连接服务端 , 按照IP和端口连接， *连接 connet()* 
- 发送请求数据 ，*发送 send()* 
- 接收请求数据，*接收 recv()* 
- 通信完毕 , 关闭套接字，*关闭 close()*

**示例2：创建一个TCP客户端**

```python
import socket                      # 导入模块

sock = socket.socket()             # 创建套接字对象
sock.connect(('127.0.0.1',8888))   # 建立连接
sock.send(b'is client')            # 发送请求数据
content = sock.recv(1024)          # 接受请求数据
print(content.decode())            # 打印接受请求数据
sock.close()                       # 关闭套接字
```


### 4、基于UDP的Socket

UDP协议是无连接的，面向数据报的，数据传输不可靠，无在乎先启动服务端或客户端，都不会报错

**①、基于UDP协议的服务端创建流程**

- 创建套接字对象，*创建socket对象* 
- 绑定IP和端口，*绑定 bind()* 
- 接收请求数据， *接收 recvfrom()* 
- 通信完毕 , 关闭套接字，*关闭 close()*                    

**示例1：创建一个UDP服务端**
```python
import socket                                    # 导入socket模块

sock = socket.socket(type=socket.SOCK_DGRAM)     # 创建socket对象
sock.bind(('127.0.0.1',8888))                    # 绑定IP和端口
data,addr = sock.recvfrom(1024)                  # 接收请求,返回数据和地址
print(data.decode())                             # 打印请求
sock.close()                                     # 关闭socket
```


**②、基于UDP协议的客户端创建流程**

- 创建套接字对象， *创建socket对象*
- 发送请求数据，*发送 sendto()*
- 通信完毕 , 关闭套接字，* 关闭 close()*

**示例2：创建一个UDP客户端**

```python
import socket                                  # 导入模块

sock = socket.socket(type=socket.SOCK_DGRAM)   # 创建套接字对象
sock.sendto(b'is client',('127.0.0.1',8888))   # 发送请求数据
sock.close()                                   # 关闭套接字
```

**③、解决地址已经使用的问题**

错误：``OSError: [Errno 48] Address already in use``

解决：添加一条socket配置 , 重用ip和端口

```python
import socket 

sock = socket.socket()

# 添加在bind前 
sock.setsockopt(socket.SOL_SOCKET,SO_REUSEADDR,1) sock.bind(address) 
```


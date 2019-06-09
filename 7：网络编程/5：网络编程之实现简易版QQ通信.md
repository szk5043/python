五、网络编程之实现简易版QQ通信

1、概述

使用TCP和UDP分别实现简易版QQ通信

2、TCP实现

因为TCP是有链接的 , 这就导致只能有一个服务端 , 但是可以有多个客户端

示例1：实现简易版QQ

*server*

```python
from socket import *

server = socket()
server.bind(('127.0.0.1',8888))
server.listen(5)

while True:
    conn,addr = server.accept()
    print('请求来自客户端: {}'.format(addr))
    while True:
        try:
            data = conn.recv(1024)
            print('data from [%s]: %s' % addr,data.decode('utf-8'))
            if data == 'q':
                break
            else:
                while True:
                    message = input('请输入想要发送的内容：').strip().encode('utf-8')
                    if len(message) == 0: continue
                    conn.send(message)
                    break
        except ConnectionRefusedError:
            break
    conn.close()
server.close()
```

*client*

```python
from socket import *

client = socket()
client.connect(('127.0.0.1',8888))

while True:
    message = input('请输入你想要发送的内容: ').strip().encode('utf-8')
    if len(message) == 0:
        continue
    elif message == b'q':
        break
    else:
        client.send(message)
        data = client.recv(1024)
        print('%s: %s' % ('127.0.0.1',8888),data.decode('utf-8'))
client.close()
```

当然实际应用中是不会用TCP来完成的 , 而是用UDP , 这里只是模拟 , 并且以上还有有问题没有解决的 , 比如如果发送的消息大于1024字节 , 那么就不能完整接收信息了 , 可以通过防粘包处理

TCP版本的服务端可以允许同时连入5个客户端 , 值得注意的是并不是同时连入 , 按照顺序排队 , 只有前面的人说完了会连入后序的客户端

3、UDP实现

示例2：实现简易版QQ

*server*

```python
from socket import *

server = socket(type=SOCK_DGRAM)
server.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
server.bind(('127.0.0.1',8889))

while True:
    msg,addr = server.recvfrom(1024)
    print('从客户端: %s，接收消息：%s' % (addr,msg.decode('utf-8')))
    if msg == b'q':
        break
    while True:
        messages= input('请输入消息>>>: ').strip().encode('utf-8')
        if not messages:continue
        server.sendto(messages,addr)
        break
server.close()
```

*client*

```python
from socket import *

client = socket(type=SOCK_DGRAM)
server_addr = ('127.0.0.1',8889)

while True:
    messages = input('请输入消息：').strip().encode('utf-8')
    if not messages:
        continue
    elif messages == b'q':
        break
    else:
        client.sendto(messages,server_addr)
        msg,addr = client.recvfrom(1024)
        print('从服务器: %s，接收消息：%s' % (addr, msg.decode('utf-8')))
client.close()
```

利用UDP实现才更接近现实 , 我们只需要知道他的ip和端口 , 我们就可以跟他讲话 , 在他即可以是服务端 , 也可以是客户端 , 不过必须注意接收和发送流程的问题
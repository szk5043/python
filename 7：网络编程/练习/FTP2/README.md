## FTP程序

### 需求
- 用户加密认证
- 允许同时多用户登录
- 每个用户有自己的家目录，且只能访问自己的家目录
- 对用户进行磁盘配额，每个用户可用空间不同
- 允许用户在ftp server上随意切换目录
- 允许用户查看当前目录下文件
- 允许上传和下载文件，保证文件一致性
- 文件传输过程中显示进度条
- 附件功能：支持文件的断电续传

### 流程图
![image](1.tiff)

### 目录结构

```shell
$ tree .
.
├── 1.tiff
├── README.md
├── ftpclient
│   └── ftpclient.py
└── ftpserver
    ├── conf
    │   └── settings.py
    ├── database
    ├── ftpserver.py
    ├── home
    │   ├── szk
    │   └── test
    ├── log
    └── modules
        ├── auth_user.py
        └── sokect_server.py
```




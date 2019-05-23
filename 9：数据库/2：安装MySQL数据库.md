## 二、安装MySQL数据库

### 1、下载

登陆[MySQL官网](<https://dev.mysql.com/downloads/mysql/5.7.html#downloads>)下载，或使用下面的下载链接

[https://cdn.mysql.com//Downloads/MySQL-5.6/mysql-5.6.44-winx64.zip](https://cdn.mysql.com//Downloads/MySQL-5.6/mysql-5.6.44-winx64.zip)

[https://cdn.mysql.com//Downloads/MySQL-5.7/mysql-5.7.26-winx64.zip](https://cdn.mysql.com//Downloads/MySQL-5.7/mysql-5.7.26-winx64.zip)

### 2、安装

（1）、Windows下安装

下载MySQL5.6，直接解压

在数据库目录新建**startup.bat启动脚本**，双击即可启动

```powershell
cd bin
mysqld --standalone
```

在数据库目录新建**shutdown.bat关闭服务脚本**，双击即可关闭服务

```powershell
cd bin
mysqladmin shutdown -u root -p
```

（2）、Linux容器方式安装

数据库配置

```shell
$ cat my.cnf 
[mysqld]
sql_mode = "STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION"
key_buffer_size = 384M
max_allowed_packet = 32M

default-time-zone = "+08:00"

max_connections=4096

[mysqldump]
max_allowed_packet = 32M
```

部署脚本

```shell
$ cat start_db.sh 
#!/bin/bash

MYSQL_VERSION=5.7.23
MYSQL_DOCKER_IMAGE=mysql:$MYSQL_VERSION

MYSQL_CNF_DIR=/opt/deploy/mysql/conf
DATA_DIR=/opt/deploy/mysql/data

DATABASE_USERNAME=root
DATABASE_PASSWORD=123

# 1. start container
docker run -t -d --name mysql --restart unless-stopped -v $MYSQL_CNF_DIR:/etc/mysql/conf.d -v $DATA_DIR:/var/lib/mysql -p 3306:3306 -e TZ='Asia/Hong_Kong' -e MYSQL_ROOT_PASSWORD="$DATABASE_PASSWORD" $MYSQL_DOCKER_IMAGE
echo 'start container mysql successfully...'
```

> 需自动安装docker

### 3、修改和恢复数据库密码

①、修改默认密码

```powershell
mysql -u root -p    #使用cmd进去mysql bin目录，执行此命令，直接回车
use mysql;
UPDATE user SET Password=PASSWORD('123') where USER='root';
FLUSH PRIVILEGES;
quit
```

> 重新登陆，即可使用新密码登陆

②、清除密码

```shell
mysqld -skip-grant-tables    #使用此命令启动数据库
mysql     #无密码登录
update mysql.user set password = password("root") where user = "root" and host="localhost";  #修改密码
```

③、修改密码

```shell
msyqladmin -u用户名 -p旧密码 password 新密码
```


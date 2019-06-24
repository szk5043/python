## 三、MySQL之数据库管理

### 1、库管理

##### (1)、 显示数据库

```
SHOW DATABASES;
```

默认数据库：

- mysql - 用户权限相关数据
- test - 用于用户测试数据
- information_schema - MySQL本身架构相关数据

##### (2)、 创建数据库

```
# utf-8
CREATE DATABASE 数据库名称 DEFAULT CHARSET utf8 COLLATE utf8_general_ci;
```

##### (3)、 使用数据库

```
USE db_name;
```

显示当前使用的数据库中所有表：SHOW TABLES;

### 2、用户管理

语法

```sql
创建用户
    create user '用户名'@'IP地址' identified by '密码';
删除用户
    drop user '用户名'@'IP地址';
修改用户
    rename user '用户名'@'IP地址'; to '新用户名'@'IP地址';;
修改密码
    set password for '用户名'@'IP地址' = Password('新密码')
  
PS：用户权限相关数据保存在mysql数据库的user表中，所以也可以直接对其进行操作（不建议）
```

### 3、授权管理

```sql
show grants for '用户'@'IP地址'                  -- 查看权限
grant  权限 on 数据库.表 to   '用户'@'IP地址'      -- 授权
revoke 权限 on 数据库.表 from '用户'@'IP地址'      -- 取消权限
```

授权目标数据库的各类方式

```sql
数据库名.*           数据库中的所有
数据库名.表          指定数据库中的某张表
数据库名.存储过程     指定数据库中的存储过程
*.*                所有数据库
```

授权用户的各类方式

```sql
用户名@IP地址         用户只能在改IP下才能访问
用户名@192.168.1.%   用户只能在改IP段下才能访问(通配符%表示任意)
用户名@%             用户可以再任意IP下访问(默认IP地址为%)
```

**常见的例子：**

```sql
grant all privileges on db1.tb1 TO '用户名'@'IP'
grant select on db1.* TO '用户名'@'IP'
grant select,insert on *.* TO '用户名'@'IP'
revoke select on db1.tb1 from '用户名'@'IP'
flush privileges        #将数据读取到内存中，从而立即生效
```




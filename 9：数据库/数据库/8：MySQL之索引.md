## 八、MySQL之索引

### 1、介绍

索引是数据库中最常用也是最重要的手段之一 , 是数据库中专门用于帮助用户快速查询数据的一种数据结构 , 类似于字典中的目录 , 查找字典内容时可以根据目录查找到数据的存放位置 , 然后直接获取值即可

索引是在MySQL的存储引擎层中实现的  而不是在服务器层实现的 , 所以每种存储引擎的索引都不一定完全相同 , 也不是所有的存储引擎都支持所有的索引类型

是否需要对每一列都要加索引？

- 不是的，索引固然加速了查找，但是对增删改查的效率不高。原则需要根据业务决定(向经常使用的字段上加索引)

索引使用的前提（**语句前面加一个explain**，测试是否用到索引，type:ALL表示全表查询）：

- 不能使用`like`
- 不要在语句中使用函数
- 类型需要一致

三个常用引擎支持的索引类型比较

| 索引          | MyISAM引擎 | InnoDB引擎    | Memory引擎 |
| ------------- | ---------- | ------------- | ---------- |
| B-Tree索引    | 支持       | 支持          | 支持       |
| HASH索引      | 不支持     | 不支持        | 支持       |
| R-Tree索引    | 支持       | 不支持        | 不支持     |
| Full-text索引 | 支持       | 5.6版本后支持 | 不支持     |

索引的类型：

- 主键索引：加速查找+不能为空+不能重复 primary key
- 唯一索引：加速查找+不能重复 unique(name)
	- 联合唯一索引：加速查找+两列不能重复
- 普通索引：加速查找 `index ix_name (name)`

### 2、插入三百万条数据

①、创建相关的库和表

```sql
/*创建库*/
create database db3;
/*切换库*/
use db3;
/*创建表*/
create table user(id int auto_increment primary key,name char(32) not null default '',password char(32) not null default '')engine=Innodb charset=utf8;
```

②、循环插入数据

```python
import pymysql

# 连接mysql数据库
conn = pymysql.connect(host='127.0.0.1',user='root',password='123',database='db3')

cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)  #cursor=pymysql.cursors.DictCursor,返回的数据以字典展示

sql = 'insert into user(name,password) values (%s,%s)'

data = []
for i in range(3000000):
    data.append(('root'+str(i),'passwd'+str(i)))
cursor.executemany(sql,data)

conn.commit()  #提交

cursor.close()
conn.close()
```

查看插入的数据

```sql
select count(id) from user;
+-----------+
| count(id) |
+-----------+
|   3000000 |
+-----------+
```

### 3、创建主键索引

两种创建索引的方式：

①、创建表结构的时候创建索引

```sql
create table xxx(
	id int auto_increment primary key,
	name varchar(32) not null default '',
	unique uq_name (name));
```

②、表结构已经创建完后创建索引

```sql
create table xxx(
	id int,
	name varchar(32) not null default '',
	unique uq_name (name));
	
alter table xxx change id id int primary key;
```

### 4、创建唯一索引

两种创建索引的方式：

①、创建表结构的时候创建索引

```sql
create table xxx(
	id int auto_increment primary key,
	name varchar(32) not null default '',
	unique uq_name (name));
```

②、表结构已经创建完后创建索引

```sql
create index ix_name on xxx(name);
```

### 5、创建普通索引

两种创建索引的方式：

①、创建表结构的时候创建索引

```sql
create table xxx(
	id int auto_increment primary key,
	name varchar(32) not null default '',
	index ix_name (name),
	unique uq_name (name));
```

②、表结构已经创建完后创建索引

```sql
create index ix_name on xxx(name);
```

### 6、查看创建的索引

```sql
show indexs ix_name from name\G;
```

### 7、删除索引

①、删除普通索引和唯一索引

```sql
drop index 索引名 on 表名；
```

②、删除主键索引

```sql
alter table 表名 drop primary key;
```


## 四、MySQL之增删改查

### 1、库的增、删、改、查

语法：

```
增
	create database 数据库名;
删
	drop database （数据库名）db2;
改
	删掉数据库， 然后新建
查：
	show databases;
切换库：
	use 数据库名(db2);
```

**示例1：库的增删改查**

```sql
mysql> create database db1;      #增
Query OK, 1 row affected (0.01 sec)

mysql> drop database db1;        #删
Query OK, 0 rows affected (0.01 sec)

#改，删除重建

mysql> show databases;          #查
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| performance_schema |
| sys                |
+--------------------+
4 rows in set (0.01 sec)

mysql> use mysql;           #切换数据库       
Database changed
```

### 2、表的增、删、改、查

**①、创建表语法**：

```
create table 表名 (
		列1 列属性 [是否为null 默认值],
		列2 列属性 [是否为null 默认值],
		.....
		列n 列属性 [是否为null 默认值]
	)engine = 存储引擎  charset = 字符集
```

**示例1：创建表，并查看表**

```sql
mysql> create table t1(id int auto_increment primary key, name char(32) not null default '', create_time datetime not null default '1970-01-01 00:00:00') engine=Innodb charset=utf8;
Query OK, 0 rows affected (0.02 sec)

mysql> show tables;     #查看创建的表
+---------------+
| Tables_in_db1 |
+---------------+
| t1            |
+---------------+
1 row in set (0.00 sec)

mysql> desc t1;        #查看详细的建表语句
+-------------+----------+------+-----+---------------------+----------------+
| Field       | Type     | Null | Key | Default             | Extra          |
+-------------+----------+------+-----+---------------------+----------------+
| id          | int(11)  | NO   | PRI | NULL                | auto_increment |
| name        | char(32) | NO   |     |                     |                |
| create_time | datetime | NO   |     | 1970-01-01 00:00:00 |                |
+-------------+----------+------+-----+---------------------+----------------+
3 rows in set (0.00 sec)

mysql> select * from t1;    #查看表中数据
Empty set (0.00 sec)
```

**②、删除表语法**

```
drop table 表名；(表里的数据会没有）
```

**③、修改表语法**

```sql
修改一列：
	alter table 表名(t3) change  老列名(name)   新列名(usernme char(32));
添加一列：
	alter table 表名(t3) add  新列名(age int); 
删除一列;
	alter table 表名(t3) drop 老列名(age);
```

**示例二：修改表**

```sql
mysql> alter table t1 change name username char(32);  #修改一列
Query OK, 0 rows affected (0.02 sec)
Records: 0  Duplicates: 0  Warnings: 0

mysql> alter table t1 add (age int);      #添加一列
Query OK, 0 rows affected (0.01 sec)
Records: 0  Duplicates: 0  Warnings: 0

mysql> desc t1;       #查看修改
+-------------+----------+------+-----+---------------------+----------------+
| Field       | Type     | Null | Key | Default             | Extra          |
+-------------+----------+------+-----+---------------------+----------------+
| id          | int(11)  | NO   | PRI | NULL                | auto_increment |
| username    | char(32) | YES  |     | NULL                |                |
| create_time | datetime | NO   |     | 1970-01-01 00:00:00 |                |
| age         | int(11)  | YES  |     | NULL                |                |
+-------------+----------+------+-----+---------------------+----------------+
4 rows in set (0.00 sec)

mysql> alter table t1 drop age;      #删除一行
Query OK, 0 rows affected (0.02 sec)
Records: 0  Duplicates: 0  Warnings: 0
```

**④、查看表**

```sql
mysql> show tables;
+---------------+
| Tables_in_db1 |
+---------------+
| t1            |
+---------------+
1 row in set (0.00 sec)
```

### 3、行的增、删、改、查

**①、增加行语法：**

```
insert into 表名(列1，列2，...., 列n) values (‘值1’, '值2'， ..., '值n');
```

**示例三、增加行数据**

```sql
mysql> insert into t1 (username,age) values('szk',23);    #增加一行数据
Query OK, 1 row affected (0.01 sec) 

mysql> insert into t1(username,age) values('wesley',25),('test1',22),('test2',23);    #增加多行数据
Query OK, 3 rows affected (0.00 sec)
Records: 3  Duplicates: 0  Warnings: 0

mysql> select * from t1;     #查看增加的数据
+----+----------+---------------------+------+
| id | username | create_time         | age  |
+----+----------+---------------------+------+
|  1 | szk      | 1970-01-01 00:00:00 |   23 |
|  2 | wesley   | 1970-01-01 00:00:00 |   25 |
|  3 | test1    | 1970-01-01 00:00:00 |   22 |
|  4 | test2    | 1970-01-01 00:00:00 |   23 |
+----+----------+---------------------+------+
4 rows in set (0.00 sec)
```

**②、删除行语法**

```
delete from 表名(t1);        #再次插入数据的时候，id是从上一次主键id开始的
truncate t1        #删除数据，然后再次插入数据的时候，id从1开始
delete from t1 where id = 3;      #删除指定id的数据
```

**示例四、删除行数据**

```sql
mysql> delete from t1;              #删除表中的行数据
Query OK, 4 rows affected (0.00 sec)

mysql> select * from t1;    #空了
Empty set (0.00 sec)

mysql> insert into t1(username,age) values('wesley',25),('test1',22),('test2',23);   #新增数据
Query OK, 3 rows affected (0.00 sec)
Records: 3  Duplicates: 0  Warnings: 0

mysql> select * from t1;      #查看数据，id从上次主键递增
+----+----------+---------------------+------+
| id | username | create_time         | age  |
+----+----------+---------------------+------+
|  5 | wesley   | 1970-01-01 00:00:00 |   25 |
|  6 | test1    | 1970-01-01 00:00:00 |   22 |
|  7 | test2    | 1970-01-01 00:00:00 |   23 |
+----+----------+---------------------+------+
3 rows in set (0.00 sec)

mysql> truncate t1;    #另外一个删除数据
Query OK, 0 rows affected (0.01 sec)

mysql> select * from t1;    #空了
Empty set (0.00 sec)

mysql> insert into t1(username,age) values('wesley',25),('test1',22),('test2',23);   #插入数据
Query OK, 3 rows affected (0.00 sec)
Records: 3  Duplicates: 0  Warnings: 0

mysql> select * from t1;    #查看数据，id从1开始
+----+----------+---------------------+------+
| id | username | create_time         | age  |
+----+----------+---------------------+------+
|  1 | wesley   | 1970-01-01 00:00:00 |   25 |
|  2 | test1    | 1970-01-01 00:00:00 |   22 |
|  3 | test2    | 1970-01-01 00:00:00 |   23 |
+----+----------+---------------------+------+
3 rows in set (0.00 sec)
```

**③、改行数据语法**

```
update 表名 set name='xxxx';
```

**示例四、修改行数据**

```sql
mysql> update t1 set username='szk',age=26 where id=2;
Query OK, 1 row affected (0.00 sec)
Rows matched: 1  Changed: 1  Warnings: 0

mysql> select * from t1;
+----+----------+---------------------+------+
| id | username | create_time         | age  |
+----+----------+---------------------+------+
|  1 | wesley   | 1970-01-01 00:00:00 |   25 |
|  2 | szk      | 1970-01-01 00:00:00 |   26 |
|  3 | test2    | 1970-01-01 00:00:00 |   23 |
+----+----------+---------------------+------+
3 rows in set (0.00 sec)
```

**④、查数据语法**

```
select * from t1;     #将所有列的值全部显示
select 列名1,列名2... from t1;  #指定列的值显示
```

**示例五、查看数据**

```sql
mysql> select * from t1;      #查看所有数据
+----+----------+---------------------+------+
| id | username | create_time         | age  |
+----+----------+---------------------+------+
|  1 | wesley   | 1970-01-01 00:00:00 |   25 |
|  2 | szk      | 1970-01-01 00:00:00 |   26 |
|  3 | test2    | 1970-01-01 00:00:00 |   23 |
+----+----------+---------------------+------+
3 rows in set (0.00 sec)

mysql> select * from t1 where id=1;    #查看指定id值数据
+----+----------+---------------------+------+
| id | username | create_time         | age  |
+----+----------+---------------------+------+
|  1 | wesley   | 1970-01-01 00:00:00 |   25 |
+----+----------+---------------------+------+
1 row in set (0.00 sec)

mysql> select username,age from t1 ;    #查看指定列数据
+----------+------+
| username | age  |
+----------+------+
| wesley   |   25 |
| szk      |   26 |
| test2    |   23 |
+----------+------+
3 rows in set (0.00 sec)

mysql> select username,age from t1 where id >1 and id <3 ;   #组合条件查询
+----------+------+
| username | age  |
+----------+------+
| szk      |   26 |
+----------+------+
1 row in set (0.00 sec)

mysql> select * from t1 where username like 's%';   #通配符匹配查询，%匹配字符串后面所有的字符
+----+----------+---------------------+------+
| id | username | create_time         | age  |
+----+----------+---------------------+------+
|  2 | szk      | 1970-01-01 00:00:00 |   26 |
+----+----------+---------------------+------+
1 row in set (0.00 sec)

mysql> select * from t1 where username like 'test_';   #通配符匹配查询，_匹配字符串后面一个字符
+----+----------+---------------------+------+
| id | username | create_time         | age  |
+----+----------+---------------------+------+
|  3 | test2    | 1970-01-01 00:00:00 |   23 |
+----+----------+---------------------+------+
1 row in set (0.00 sec)

mysql> select * from t1 limit 0,1;   #限制取几条，从第几条开始（索引），取几条数据
+----+----------+---------------------+------+
| id | username | create_time         | age  |
+----+----------+---------------------+------+
|  1 | wesley   | 1970-01-01 00:00:00 |   25 |
+----+----------+---------------------+------+
1 row in set (0.00 sec)

mysql> select * from t1 limit 1,2;  #从第索引1开发，取两条数据
+----+----------+---------------------+------+
| id | username | create_time         | age  |
+----+----------+---------------------+------+
|  2 | szk      | 1970-01-01 00:00:00 |   26 |
|  3 | test2    | 1970-01-01 00:00:00 |   23 |
+----+----------+---------------------+------+
2 rows in set (0.00 sec)
```

**示例六、数据排序**

```sql
mysql> select * from t1 order by age desc,id asc;  # 首先按照age进行降序， 如果age相同的话，再按照id进行升序排列
+----+----------+---------------------+------+
| id | username | create_time         | age  |
+----+----------+---------------------+------+
|  1 | wesley   | 1970-01-01 00:00:00 |   25 |
|  3 | test2    | 1970-01-01 00:00:00 |   23 |
|  2 | test1    | 1970-01-01 00:00:00 |   22 |
+----+----------+---------------------+------+
3 rows in set (0.00 sec)
```

**示例七、使用聚合函数分组**

语法

```
group by 列名
having 对分组之后的结果进行二次删选
聚合函数：
	count(): 计数
	sum()  : 求和
	max()  : 最大值
	min()  : 最小值
	avg()  : 平均值
```

```sql
mysql> select age,count(age) from t1 group by age;   #对age进行计数并分组
+------+------------+
| age  | count(age) |
+------+------------+
|   22 |          2 |
|   23 |          2 |
|   25 |          2 |
+------+------------+
3 rows in set (0.00 sec)

mysql> select age,sum(age) from t1 group by age;   #对age进行求和并分组
+------+----------+
| age  | sum(age) |
+------+----------+
|   22 |       44 |
|   23 |       46 |
|   25 |       50 |
+------+----------+
3 rows in set (0.00 sec)

mysql> select age,count(id) as cnt from t1 group by age having cnt>=2;  #对id进行计数重命名为cnt，并筛选出>=2的项
+------+-----+
| age  | cnt |
+------+-----+
|   22 |   2 |
|   23 |   2 |
|   25 |   2 |
+------+-----+
3 rows in set (0.00 sec)
```

**示例八：表连接**

```sql
/*查看老师表*/
select * from teacher;
+-----+--------+
| tid | tname  |
+-----+--------+
|   1 | 波多   |
|   2 | 苍空   |
|   3 | 饭岛   |
+-----+--------+

/*查看课程表*/
select * from course;
+-----+--------+-----------+
| cid | cname  | tearch_id |
+-----+--------+-----------+
|   1 | 生物   |         1 |
|   2 | 体育   |         1 |
|   3 | 物理   |         2 |
+-----+--------+-----------+

/*内连接查询*/
select * from teacher,course where teacher.tid=course.tearch_id;
+-----+--------+-----+--------+-----------+
| tid | tname  | cid | cname  | tearch_id |
+-----+--------+-----+--------+-----------+
|   1 | 波多   |   1 | 生物   |         1 |
|   1 | 波多   |   2 | 体育   |         1 |
|   2 | 苍空   |   3 | 物理   |         2 |
+-----+--------+-----+--------+-----------+

/*外连接查询，左查询*/
select * from course left join teacher on teacher.tid=course.tearch_id;
+-----+--------+-----------+------+--------+
| cid | cname  | tearch_id | tid  | tname  |
+-----+--------+-----------+------+--------+
|   1 | 生物   |         1 |    1 | 波多   |
|   2 | 体育   |         1 |    1 | 波多   |
|   3 | 物理   |         2 |    2 | 苍空   |
+-----+--------+-----------+------+--------+

/*查询每个老师教授的课程数量*/
select teacher.tname,count(course.cname) from teacher left join course on course.tearch_id=teacher.tid group by tname;
+--------+---------------------+
| tname  | count(course.cname) |
+--------+---------------------+
| 波多   |                   2 |
| 苍空   |                   1 |
| 饭岛   |                   0 |
+--------+---------------------+
```

**示例九、SQL嵌套、子查询**

不建议大家在线上使用SQL子查询进行操作，建议将SQL语句分叉成多条简单的SQL语句， 分别查询， 速度是快于嵌套查询

```sql
/*查询没学过“李平”老师课的同学的学号、姓名*/
select distinct student_id from score where corse_id not in (select cid from teacher left join course on teacher.tid=course.tearch_id where tname like '李平老师');
```




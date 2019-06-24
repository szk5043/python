## 六、MySQL主键和外键

### 1、主键概念

什么是主键？

- 一种特殊的唯一索引,不允许有空值,

- 如果主键使用单个列，则它的值必须唯一
- 如果是多列，则成为联合主键，则其组合必须唯一

为什么需要主键？

- 主键可以保证记录的唯一和主键域非空
- 数据库管理系统对于主键自动生成唯一索引，所以**主键也是一个特殊的索引**
- 在设置表格式时，对于自增列，必须是索引(含主键)

### 2、主键使用

设置表格式时，对于自增列，必须是索引(含主键)

```sql
/* 自增 */
CREATE TABLE tablename(
    column_name type NOT NULL auto_increment PRIMARY KEY,
)ENGINE=InnoDB DEFAULT CHARSET=utf8
或
CREATE TABLE tablename(
    column_name type NOT NULL auto_increment,
    INDEX(column_name)
)ENGINE=InnoDB DEFAULT CHARSET=utf8
    对于自增列,必须是索引(含主键)
    对于自增可以设置步长和起始值
```

示例1：设置表格式中id为自增列

```sql
/*创建t2表，id之自增列，且含主键*/
mysql> create table t2(id int auto_increment primary key, name char(32) not null default '') engine=Innodb charset=utf8;
Query OK, 0 rows affected (0.01 sec)

/*查看建表格式*/
mysql> desc t2;    
+-------+----------+------+-----+---------+----------------+
| Field | Type     | Null | Key | Default | Extra          |
+-------+----------+------+-----+---------+----------------+
| id    | int(11)  | NO   | PRI | NULL    | auto_increment |
| name  | char(32) | NO   |     |         |                |
+-------+----------+------+-----+---------+----------------+
2 rows in set (0.00 sec)

/*插入数据*/
mysql> insert into t2 (name) values('szk'),('wesley'),('test1');
Query OK, 3 rows affected (0.00 sec)
Records: 3  Duplicates: 0  Warnings: 0

/*查看表数据*/
mysql> select * from t2;
+----+--------+
| id | name   |
+----+--------+
|  1 | szk    |
|  2 | wesley |
|  3 | test1  |
+----+--------+
3 rows in set (0.01 sec)
```

### 3、外键概念

什么是外键？

- `foreign key`，外面的键，即不在自己表中的键。
- 如果一张表中有一个非主键的字段指向另外一张表的主键，那么将该字段称之为外键。
- 每张表中，可以有多个外键。
- 表引擎必须为InnoDB，MyISAM不支持

为什么需要外键？

- 很多场景中表的数据重复太厉害，可以通过将重复数据新建一张表，通过外键的方式关联到新表

### 4、外键使用

- **基本语法**：`foreign key(外键字段) + references + 外部表名(主键字段);`

创建如下五张表，包含复杂的外键关系：

![mysql练习题.png](https://i.loli.net/2019/06/11/5cff855aa774e17530.png)

班级

```sql
/*创建班级表*/
create table class( cid int auto_increment primary key, caption char(32) not null default '')engine=Innodb charset=utf8;

/*插入班级数据*/
INSERT into class(caption) VALUES('三年二班'),('一年三班'),('三年一班');
```

学生

```sql
/*创建学生表*/
create table student(
  sid int auto_increment primary key,
  sname char(32) not null default '',
  gender char(6) not null default '',
  class_id int,
  constraint class_student foreign key (class_id) references class(cid)
  )engine=Innodb charset=utf8;

/*插入学生数据*/
INSERT into student(sname,gender,class_id) VALUES('钢弹','女',1),('铁锤','女',1),('山炮','男',2);
```

老师

```sql
/*创建老师表*/
CREATE table teacher(
	tid int auto_increment primary key,
	tname char(32) not null default ''
)engine=Innodb charset=utf8;	

/*插入老师数据*/
INSERT into teacher(tname) VALUES('波多'),('苍空'),('饭岛');
```

课程

```sql
/*创建课程表*/
CREATE table course(
	cid int auto_increment primary key,
	cname char(32) not null default '',
  tearch_id int,
  constraint teacher_course foreign key (tearch_id) references teacher(tid)
)engine=Innodb charset=utf8;	

/*插入课程数据*/
INSERT into course(cname,tearch_id) VALUES('生物',1),('体育',1),('物理',2);
```

成绩表

```sql
/*创建成绩表*/
CREATE table score(
	sid int auto_increment primary key,
	student_id int,
  corse_id int,
  number int,
  constraint student_score foreign key (student_id) references student(sid),
  constraint corse_score foreign key (corse_id) references course(cid)
)engine=Innodb charset=utf8;

/*插入成绩数据*/
INSERT into score(student_id,corse_id,number) VALUES(1,1,60),(1,2,59),(2,2,100);
```

5、外键的变种

①、唯一索引

唯一索引有两个功能 : 加速查找和唯一约束(可含NULL)

与普通索引类似 , 不同的就是 : 索引列的值必须唯一 , 但允许有空值 , 如果是组合索引 , 则列值的组合必须唯一



②、一对多，外键映射关系

```
userinfo
			
id   name   age  depart_id
1     zekai 23     1
2     zekai 23     2
3     zekai 23     1

department：
id   name
1    开发部
2    保安部
3    运维部
```

③、一对一，外键映射关系

```
userinfo
			
id   name     age 
1     eagon   23     
2     zekai   23     
3     lxxx    23   
4     linhaifeng   78

blog表：				   外键 + 唯一约束
id     url             uid
1      /linhaifeng/     4
2      /lxxx/           3
```

详细建表语句

```sql
/*创建userinfo表*/
create table userinfo (id int auto_increment primary key,name char(32) not null default '',age int not null default '1')engine=Innodb charset=utf8;

/*创建blog表*/
create table bolg (id int auto_increment primary key, url char(32) not null default '',uid int,constraint fk_name_uid foreign key (uid) references userinfo(id), unique  uid (uid));
```

④、多对多，外键映射关系

```
userinfo			
id	name	age	
1	root1	23	
2	root2	24	
3	root3	25	
4	root4	26	
5	root5	27	
			
host	
id	name
1	c1.com
2	c2.com
3	c3.com
				
user2host			
id	uid	hid	
1	1	1	
2	1	2	
3	1	3	
4	2	1
```

详细建表语句

```sql
create table userinfo (id int auto_increment primary key,name char(32) not null default '',age int not null default '1')engine=Innodb charset=utf8;

create table host(id int auto_increment primary key,name char(32) not null default '')engine=Innodb charset=utf8;

create table user2host(id int auto_increment primary key, uid int,hid int,constraint fk_name_uid foreign key (uid) references userinfo(id),constraint fk_host_hid foreign key (hid) references host(id),  unique  uid_hid (uid,hid));
```




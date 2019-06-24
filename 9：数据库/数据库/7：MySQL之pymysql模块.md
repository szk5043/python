## 七、MySQL之pymysql模块

### 1、概述

Python如何实现对mysql数据库的增删改查呢？答案：pymysql模块



### 2、pymysql实现增、删、改、查

①、pymysql的安装

```shell
pip3 install pymysql  # 安装模块
```
②、查
```python
import pymysql

# 连接mysql数据库
conn = pymysql.connect(host='127.0.0.1',user='root',password='123',database='db2')

#实例化cursor对象，cursor=pymysql.cursors.DictCursor返回的数据以字典展示
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)  

#定义查询语句
sql = 'select * from student'  

#执行语句
cursor.execute(sql)
# res = cursor.fetchone()  #取一条数据
# res = cursor.fetchmany(10)  #取十条数据
res = cursor.fetchall()   #将数据全部取出来
for item in res:
    print(item)

cursor.close()
conn.close()

'''返回值
{'sid': 1, 'gender': '男', 'class_id': 1, 'sname': '理解'}
{'sid': 2, 'gender': '女', 'class_id': 1, 'sname': '钢蛋'}
...
{'sid': 18, 'gender': '男', 'class_id': 3, 'sname': 'wesley'}

'''
```

③、增

示例1：增加一条数据

```python
import pymysql

# 连接mysql数据库
conn = pymysql.connect(host='127.0.0.1',user='root',password='123',database='db2')

cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)  #cursor=pymysql.cursors.DictCursor,返回的数据以字典展示

sql = 'insert into student (sid,gender,class_id,sname) values (%s,%s,%s,%s)'

cursor.execute(sql,('19','男','1','szk'))

conn.commit()  #提交

cursor.close()
conn.close()
```

查看增加的内容

```sql
select * from student where sid=19;
+-----+--------+----------+-------+
| sid | gender | class_id | sname |
+-----+--------+----------+-------+
|  19 | 男     |        1 | szk   |
+-----+--------+----------+-------+
1 row in set (0.00 sec)
```

示例二、增加多条数据

```python
import pymysql

# 连接mysql数据库
conn = pymysql.connect(host='127.0.0.1',user='root',password='123',database='db2')

cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)  #cursor=pymysql.cursors.DictCursor,返回的数据以字典展示

sql = 'insert into student (sid,gender,class_id,sname) values (%s,%s,%s,%s)'

#增加多条数据
data = [
    ('20','男', '1', 'szk1'),
    ('21','男','2','szk2'),
    ('22','男','3','szk3'),
]
cursor.executemany(sql,data)  

conn.commit()  #提交

cursor.close()
conn.close()
```

查看增加的内容

```sql
select * from student where sid>19;
+-----+--------+----------+-------+
| sid | gender | class_id | sname |
+-----+--------+----------+-------+
|  20 | 男     |        1 | szk1  |
|  21 | 男     |        2 | szk2  |
|  22 | 男     |        3 | szk3  |
+-----+--------+----------+-------+
3 rows in set (0.00 sec)
```

④、删

示例1：删除一条数据

```python
import pymysql

# 连接mysql数据库
conn = pymysql.connect(host='127.0.0.1',user='root',password='123',database='db2')

cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)  #cursor=pymysql.cursors.DictCursor,返回的数据以字典展示

sql = 'delete from student where sid=%s'

#删除数据
cursor.execute(sql,(22))

conn.commit()  #提交

cursor.close()
conn.close()
```

示例2：删除多条数据

```sql
import pymysql

# 连接mysql数据库
conn = pymysql.connect(host='127.0.0.1',user='root',password='123',database='db2')

cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)  #cursor=pymysql.cursors.DictCursor,返回的数据以字典展示

sql = 'delete from student where sid=%s'

#删除数据
cursor.executemany(sql,(20,21))

conn.commit()  #提交

cursor.close()
conn.close()
```

### 3、SQL注入

示例代码：

```python
username = input('username>>: ').strip
pwd = input('pwd>>: ')

sql = "select * from user where name ='%s'and pwd = '%s'" %(username,pwd)
```

常见SQL注入代码：

```sql
/*#号前面的条件为真，#号后面的代码忽略*/
select * from user where name = 'wesley' #'and pwd = ''   

/*#号前面的1=1为真，#号后面的代码忽略*/
select * from user where name = 'abcdefg' or 1=1 #' and pwd = ''
```

SQL注入产生的原因：

- 没有对用户输入的做审核

python中的解决方法：

```python
cursor.execte(sql,(username,pwd))
```

> cursor.execte()默认已经做了SQL合法性检测功能
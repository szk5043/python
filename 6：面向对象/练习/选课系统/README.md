## 作业要求

角色:学校、学生、课程、讲师

### 需求:

1. 创建北京、上海 2 所学校
2. 创建linux , python , go 3个课程 ， linux\py 在北京开， go 在上海开
3. 管理员创建学校 ，老师，课程
4. 课程包含课程名称（周期，价格等属性）
5. 学校包含学校名称，地址等属性
6. 创建老师角色要关联学校
7. 学生注册登录后，可以选择学校，选择课程，查看成绩
8. 老师登录后，可以查看教授课程，选择想要教授的课程，查看课程下的学生，修改学生成绩等

### 视图和功能：

- 学生视图
  - 注册   
  - 登录   
  - 选择校区   
  - 选择课程   
  - 查看成绩   
- 老师视图   
  - 登录   
  - 查看教授课程   
  - 选择教授课程   
  - 查看课程下学生   
  - 修改学生成绩   
- 管理视图，创建讲师， 创建班级，创建课程   
  - 注册    
  - 登录   
  - 创建学校   
  - 创建老师   
  - 创建课程   
    上面的操作产生的数据都通过pickle序列化保存到文件里

总共分三个视图：

```python
#     管理员视图：
        def admin_register():
            pass
        def admin_login():
            pass
        def creat_school():
            pass
        def creat_teacher():
            pass
        def creat_course():
            pass
 #   老师视图：
        def teacher_login():
            pass
        def check_course():
            pass
        def choose_course():
            pass
        def check_student():
            pass
        def modify_score():
            pass
 #   学生视图：
        def student_register():
            pass
        def student_login():
            pass
        def choose_school():
            pass
        def choose_course():
            pass
        def check_score():
            pass
```

### 项目结构

```shell
├── README.md
├── conf                     #配置信息    
│   └── settings.py
├── core                     #放置用户层视图
│   ├── admin.py
│   ├── src.py
│   ├── student.py
│   └── teacher.py
├── db                       #存放数据信息
│   ├── admin
│   ├── db_handler.py
│   ├── modles.py
│   └── school
├── interface                #接口层
│   ├── admin_interface.py
│   ├── common_interface.py
│   ├── school_interface.py
│   ├── student_interface.py
│   └── teacher_interface.py
├── lib                      #公共方法
│   └── common.py
└── start.py                 #程序入口
```

![架构图](/Users/wesley/Desktop/CodeBase/python/6%EF%BC%9A%E9%9D%A2%E5%90%91%E5%AF%B9%E8%B1%A1/%E7%BB%83%E4%B9%A0/%E9%80%89%E8%AF%BE%E7%B3%BB%E7%BB%9F/%E6%9E%B6%E6%9E%84%E5%9B%BE.png)

### 对象保存及查询

```python
# modles
class BaseClass():
    '''公共方法基类'''

    def save(self):
    # 将对象自身调用save函数进行保存
        db_handler.save(self)

    @classmethod
    def select(cls,name):
    # 将类自身和对象名字调用select函数进行查询
        return db_handler.select(name,cls.__name__.lower())

class Admin(BaseClass):
    '''管理员类'''
    def __init__(self,name,passwd):
        self.name = name
        self.passwd = passwd
        self.save()
     		#类通过继承基类的方法，将对象自己保存进文件

    def __str__(self):
        return "name:%s password:%s " % (self.name,self.passwd)
      
# db_handler
def save(obj):
    '''将对象保存进文件'''
    path_obj = os.path.join(settings.DB_PATH,obj.__class__.__name__.lower())
    # 对象拼接，找到具体的文件夹路径，如 `选课系统/db/school`
    path_file = os.path.join(path_obj,obj.name)
    # 对象名拼接，找到具体的文件名路径，如`选课系统/db/school/szk`
    if not os.path.exists(path_obj):
    # 如果没有则创建，并且将对象写入文件
        os.mkdir(path_obj)
    with open(path_file,'wb') as f:
        pickle.dump(obj,f)
        f.flush()
        # 实时保存进文件


def select(name,type):
    '''从文件读取对象'''
    path_obj = os.path.join(settings.DB_PATH,type)
    # 对象拼接，找到具体的文件夹路径，如 `选课系统/db/school`
    path_file = os.path.join(path_obj,name)
    # 对象名拼接，找到具体的文件名路径。如`选课系统/db/school/szk`
    if not os.path.exists(path_obj):
    # 如果没有则创建
        os.mkdir(path_obj)
    if os.path.exists(path_file):
    # 如果有，则从文件中读取对象
        with open(path_obj,'rb') as f:
            return pickle.load(f)
    else:
        return False
      
```

接口层通过传入`name`查询和保存对象

```python
# admin_interface
def register_interface(user,passwd):
    '''管理员注册接口'''
    obj_names = Admin.select(user)
    # 获取已经创建的用户名，如果存在，则返回空
    if user in obj_names:
        return
    admin = Admin(user,passwd)
    return admin

def login_interface(user,passwd):
    '''管理员登录接口'''
    obj = Admin.select(user)
    if obj and obj.passwd == passwd:
        return obj
```

用户层通过接收接口层的返回值，来确认逻辑关系

```python
# admin
def admin_register():
    '''管理员注册'''
    while True:
        user = input('请输入注册的用户名：').strip()
        passwd = input('请输入注册的密码：').strip()
        conf_passwd = input('请再输入一次密码：').strip()
        if user == 'q' or passwd == 'q':break
        if user is None or passwd is None:
            print('用户名或密码不能为空！')
            continue
        if passwd != conf_passwd:
            print('两次密码输入不同，请重新输入!')
            continue
        obj = admin_interface.register_interface(user,passwd)
        # 调用接口层处理业务逻辑
        if obj:
            print('注册成功')
            return
        else:
            print('用户已存在，请重新输入')


def admin_login():
    '''管理员登录'''
    while True:
        user = input('请输入用户名：').strip()
        passwd = input('请输入密码：').strip()
        if user == 'q' or passwd == 'q':break
        obj = admin_interface.login_interface(user,passwd)
        # 调用接口层处理业务逻辑
        if obj:
            print('登录成功')
            admin_status['user'] = user
            return
        else:
            print('用户名或密码错误')
```

### 对象需要的属性

```shell
需要的类型有哪些:
管理员
    用户名 密码
学员
    名字 密码 课程[str]  学校str  成绩{'python':99}
老师
    姓名  密码   教授的课程
学校
    学校的名字 地址  老师 课程
课程
    名称 价格 周期  学生
```


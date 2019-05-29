作业要求
角色:学校、学生、课程、讲师
要求:

1. 创建北京、上海 2 所学校
2. 创建linux , python , go 3个课程 ， linux\py 在北京开， go 在上海开
3. 管理员创建学校 ，老师，课程
4. 课程包含课程名称（周期，价格等属性）
5. 学校包含学校名称，地址等属性
6. 创建老师角色要关联学校
7. 学生注册登录后，可以选择学校，选择课程，查看成绩
8. 老师登录后，可以查看教授课程，选择想要教授的课程，查看课程下的学生，修改学生成绩等

最终分为以下视图和功能：
1 学生视图
	1、注册   
        2、登录   
        3、选择校区   
        4、选择课程   
        5、查看成绩   
2 老师视图   
	1、登录   
        2、查看教授课程   
        3、选择教授课程   
        4、查看课程下学生   
        5、修改学生成绩   
3 管理视图，创建讲师， 创建班级，创建课程   
        1、注册    
        2、登录   
        3、创建学校   
        4、创建老师   
        5、创建课程   
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
conf放置配置信息setting
core：放置用户层视图
db：数据操作层py文件和以文件形式保存的数据
interface：放置接口相关信息，有管理员接口，老师接口，学校接口，学生接口和公共接口
lib：放置公共方法

用户功能层：src下：
                src：主视图，
                admin：管理员视图，
                student：学生视图
                teacher：老师视图

接口层：interface下：
                  admin_interface管理员的接口
                  common_interface公共的接口
                  school_interface学校的接口
                  student_interface学生的接口
                  teacher_interface老师的接口
数据层：db目录下：
                db_handler，文件操作相关的方法
                models：各种类及类方法的定义

其它目录：admin，course，school，student，teacher是自动生成的目录，用来存放数据信息

start.py启动文件
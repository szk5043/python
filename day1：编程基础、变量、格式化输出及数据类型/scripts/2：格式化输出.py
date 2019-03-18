# 用加号+拼接
# name = input("name: ")
# age = int(input("age: "))
# job = input("job: ")
# info = '''
# ----- info of''' + name +''' -----
# Name: ''' + str(name) + '''
# Age: ''' + str(age) + '''
# Job: ''' + str(job)
# print(info)

# 占位符%拼接
# name = input("name: ")
# age = int(input("age: "))
# job = input("job: ")
# info = '''
# ----- info of %s  -----
# name: %s
# age: %f
# job: %s
# ''' %(name,name,age,job)
# print(info)

# format函数拼接
name='wesley'
age='25'
info='my name is {name},my age is {age}'.format(name=name,age=age)
print(info)
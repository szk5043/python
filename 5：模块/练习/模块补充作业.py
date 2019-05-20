#--*-- coding:utf-8 --*--
# @Time   ： 2019/5/16 11:44
# @Author : Wesley
# @File   : 模块补充作业.py

#1.自定义身份证正则：正则不具备逻辑，所以月的天数都用31天考虑
import re
str1 = "^" + "\\d{6}" + "(18|19|([23]\\d))\\d{2}" + "((0[1-9])|(10|11|12))" + "(([0-2][1-9])|10|20|30|31)" + "\\d{3}" + "[0-9Xx]" + "$"
# strData = input("请输入您的身份证号:")
pattern = r'^\d{6}(18|19|([23]\d))\d{2}((0[1-9])|(10|11|12))(([0-2][1-9])|10|20|30|31)\d{3}[0-9Xx]$'
res = re.match(pattern,'321183399410184854')
print(res)
'''
#2.结合requests模块与正则匹配，获取百度首页所有图片地址链接，保存到文件中
提示：pip3 install requests
res = requests.get('https://www.baidu.com')  # 获取主页
ctx = res.content.decode('utf-8')  # 解析得到主页内容

用正则取出结果：['www.baidu.com/img/bd_logo1.png', 'www.baidu.com/bdorz/login.gif', 'www.baidu.com/bdorz/login.gif', 'www.baidu.com/img/gs.gif']
'''
import requests
res = requests.get('https://www.baidu.com')  # 获取主页
ctx = res.content.decode('utf-8')  # 解析得到主页内容
pattern= r'www.baidu.com/[^\s]+\.(?:gif|png)'
print(re.findall(pattern,ctx))
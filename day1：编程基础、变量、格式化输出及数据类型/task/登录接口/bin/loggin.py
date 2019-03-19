#--*-- coding:utf-8 --*--
# @Time   ： 2019/3/18 15:45
# @Author : Wesley
# @File   : loggin.py
import sys
import os
BASE_DIR = os.path.dirname( os.path.dirname( os.path.abspath(__file__) ) )
sys.path.append(BASE_DIR)
from core import main

main.say_hello

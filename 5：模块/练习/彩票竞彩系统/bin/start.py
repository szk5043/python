#--*-- coding:utf-8 --*--
# @Time   ： 2019/5/16 15:43
# @Author : Wesley
# @File   : start.py
import os
import sys

BASE_PATH = os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_PATH)

from core import src

if __name__ == '__main__':
    src.run()

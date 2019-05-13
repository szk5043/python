# --*-- coding:utf-8 --*--
# @Time   ： 2019/5/10 14:13
# @Author : Wesley
# @File   : start.py
import sys, os

path = os.path.dirname(__file__)
sys.path.append(path)

from core import src

if __name__ == '__main__':
    src.run()

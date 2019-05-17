#--*-- coding:utf-8 --*--
# @Time   ： 2019/5/16 15:44
# @Author : Wesley
# @File   : common.py
import logging.config
from conf import settings

def get_logger(name):
    logging.config.dictConfig(settings.LOGGING_DIC)
    logger = logging.getLogger(name)
    return logger
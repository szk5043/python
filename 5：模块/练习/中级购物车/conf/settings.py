# --*-- coding:utf-8 --*--
# @Time   ： 2019/5/10 15:03
# @Author : Wesley
# @File   : settings.py
import os

# 基础目录配置
BASE_PATH = os.path.dirname(os.path.dirname(__file__))
DB_PATH = os.path.join(BASE_PATH, 'db')

#日志配置
# 定义三种日志输出格式 开始
standard_format = '[%(asctime)s][%(threadName)s:%(thread)d][task_id:%(name)s][%(filename)s:%(lineno)d]' \
                 '[%(levelname)s][%(message)s]' #其中name为getlogger指定的名字
#standard_format = "%(asctime)s %(levelname)s %(filename)s[line:%(lineno)d] - %(message)s"

#simple_format = '[%(levelname)s][%(asctime)s][%(filename)s:%(lineno)d]%(message)s'
simple_format =  "%(asctime)s %(levelname)s %(filename)s[line:%(lineno)d] - %(message)s"
id_simple_format = '[%(levelname)s][%(asctime)s] %(message)s'

# 定义日志输出格式 结束
# 日志文件夹
LOG_PATH = os.path.join(BASE_PATH, 'log')

atm_shopping_logfile_name = 'atm_shopping.log'

# 如果不存在定义的日志目录就创建一个
if not os.path.isdir(LOG_PATH):
    os.mkdir(LOG_PATH)

# log文件的全路径
# ATM/log/atm_shop.log
atm_shopping_logfile_path = os.path.join(LOG_PATH, atm_shopping_logfile_name)

# log配置字典
LOGGING_DIC = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': standard_format
        },
        'simple': {
            'format': simple_format
        },
    },
    'filters': {},
    'handlers': {
        #打印到终端的日志
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',  # 打印到屏幕
            'formatter': 'simple'
        },
        #打印到文件的日志,收集info及以上的日志
        'atm_shopping_log': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',  # 保存到文件
            'formatter': 'standard',
            'filename': atm_shopping_logfile_path ,  # 日志文件
            'maxBytes': 1024*1024*5,  # 日志大小 5M
            'backupCount': 5,
            'encoding': 'utf-8',  # 日志文件的编码，再也不用担心中文log乱码了
        },
    },
    'loggers': {
        #logging.getLogger(__name__)拿到的logger配置
        '': {
            'handlers': ['atm_shopping_log', 'console'],  # 这里把上面定义的handler都加上，即log数据既写入文件又打印到屏幕
            'level': 'DEBUG',
            'propagate': True,  # 向上（更高level的logger）传递
        },
    },
}


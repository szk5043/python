import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
# 项目根目录
LOG_DIR = os.path.join(BASE_DIR,'log')
#日志目录
USER_HOME = os.path.join(BASE_DIR,'home')
#用户家目录
ACCOUNTS_FILE = os.path.join(BASE_DIR,'conf','accounts.cfg')
#用户配置文件



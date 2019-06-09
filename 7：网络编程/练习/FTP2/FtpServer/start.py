'''
项目入口，调用执行ftp_server
'''

import os
import sys

BASE_PATH = os.path.dirname(__file__)
sys.path.append(BASE_PATH)

from core import ftp_server


if __name__ == '__main__':
    ftp_server.run()
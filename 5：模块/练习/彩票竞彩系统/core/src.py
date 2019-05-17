#--*-- coding:utf-8 --*--
# @Time   ： 2019/5/16 15:43
# @Author : Wesley
# @File   : src.py

import random
from lib import common
from db import db_handler

game_logger = common.get_logger('游戏日志')

def guess_the_size():
    '''猜大小：用户选择大或小，然后开奖，中奖与否都记录竞猜记录，中奖则记录中奖记录'''
    result = random.sample('大小',1)
    answer = input('请输入大或小: ').strip()
    if answer == '大' or answer == '小':
        if not result == answer:
            db_handler.save('猜大小：未中奖')
            game_logger.info('猜大小：未中奖')
        else:
            db_handler.save('猜大小：中奖了')
            game_logger.info('猜大小：中奖了')



def match_3():
    '''匹配3个数字'''
    result = random.sample('0123456789',3)
    answer = input('请输入三个数字: ').strip()
    if not len(answer) == 3:
        print('请输入三个数字，不能多或少！')
    if not answer.isdigit():
        print('只能输入数字！')
    num = 0
    for i in answer:
        if i in result:
            num += 1
    if num == 3:
        db_handler.save('匹配3个数字：一等奖')
        game_logger.info('匹配3个数字：一等奖')
    if num == 2:
        db_handler.save('匹配3个数字：二等奖')
        game_logger.info('匹配3个数字：二等奖')
    if num == 1:
        db_handler.save('匹配3个数字：三等奖')
        game_logger.info('匹配3个数字：三等奖')



def match_5():
    '''匹配5个数字'''
    result = random.sample('0123456789',5)
    answer = input('请输入五个数字: ').strip()
    if not len(answer) == 5:
        print('请输入五个数字，不能多或少！')
    if not answer.isdigit():
        print('只能输入数字！')
    num = 0
    for i in answer:
        if i in result:
            num += 1
    if num == 5:
        db_handler.save('匹配5个数字：一等奖')
        game_logger.info('匹配5个数字：一等奖')
    if num == 4:
        db_handler.save('匹配5个数字：二等奖')
        game_logger.info('匹配5个数字：二等奖')
    if num == 3:
        db_handler.save('匹配5个数字：三等奖')
        game_logger.info('匹配5个数字：三等奖')
    if num == 2:
        db_handler.save('匹配5个数字：四等奖')
        game_logger.info('匹配5个数字：四等奖')
    if num == 1:
        db_handler.save('匹配5个数字：五等奖')
        game_logger.info('匹配5个数字：五等奖')

def select():
    relust = db_handler.select()
    print(relust)

def run():
    '''主程序'''
    menu_dic = {
        '0': exit,
        '1': guess_the_size,
        '2': match_3,
        '3': match_5,
        '4': select,
    }
    while True:
        print('''
        0：退出
        1：猜大小
        2：匹配三
        3：匹配五
        4：查看中奖纪录
        ''')
        choice = input('请输入游戏编号：').strip()
        if choice.isdigit():
            if choice in menu_dic:
                menu_dic[choice]()
            else:
                print('您输入的游戏编号有误，请重新输入！')
        else:
            print('请输入正确的数字！')
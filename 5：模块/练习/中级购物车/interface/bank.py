# --*-- coding:utf-8 --*--
# @Time   ： 2019/5/10 15:06
# @Author : Wesley
# @File   : bank.py
from db import db_handler


def transfer_interface(from_user, to_user, balance):
    from_user_dic = db_handler.select(from_user)
    to_user_dic = db_handler.select(to_user)
    if not to_user_dic:
        return False, '对方用户不存在'
    if from_user_dic['balance'] < balance:
        return False, '余额不足'
    from_user_dic['balance'] -= balance
    to_user_dic['balance'] += balance
    from_user_dic['bankflow'].append('向%s用户成功转帐%s' % (to_user_dic, balance))
    to_user_dic['bankflow'].append('从%s用户成功收帐%s' % (from_user_dic, balance))
    db_handler.save(from_user_dic)
    db_handler.save(to_user_dic)
    return True, '向%s用户成功转帐%s' % (to_user_dic, balance)


def repay_interface(user, balance):
    user_dic = db_handler.select(user)
    user_dic['balance'] += balance
    user_dic['bankflow'].append('%s成功还款%s元' % (user, balance))
    db_handler.save(user_dic)
    return '%s成功还款%s元' % (user, balance)


def withdraw_interface(user, balance):
    user_dic = db_handler.select(user)
    if user_dic['balance'] < balance * 1.05:
        return False, '您的余额不足'
    user_dic['balance'] -= balance * 1.05
    user_dic['bankflow'].append('%s成功取款%s元' % (user, balance))
    db_handler.save(user_dic)
    return True,'%s成功取款%s元' % (user, balance)

def check_record_interface(user):
    user_dic = db_handler.select(user)
    bankflow_list = user_dic['bankflow']
    if not bankflow_list:
        return False,'没有记录'
    return True,bankflow_list
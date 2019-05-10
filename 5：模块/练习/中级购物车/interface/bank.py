# --*-- coding:utf-8 --*--
# @Time   ： 2019/5/10 15:06
# @Author : Wesley
# @File   : bank.py
from db import db_handler


def check_balance_interface(name):
    user_dic = db_handler.select(name)
    return user_dic['balance']


def withdraw_interface(name, balance):
    user_dic = db_handler.select(name)
    if user_dic['balance'] >= balance * 1.05:
        user_dic['balance'] -= balance * 1.05
        db_handler.save(user_dic)
        return True, '取款成功'
    else:
        return False, '余额不足'

def repay_interface(name,balance):
    user_dic = db_handler.select(name)
    user_dic['balance'] += balance
    db_handler.save(user_dic)
    return True,'还款成功'

def transfer_interface(from_user,to_user,balance):
    to_user_dic = db_handler.select(to_user)
    if to_user_dic:
        from_user_dic = db_handler.select(from_user)
        if from_user_dic['balance'] >= balance:
            from_user_dic['balance'] -= balance
            to_user_dic['balance'] += balance

            db_handler.save(to_user_dic)
            db_handler.save(from_user_dic)
            return True,'转账成功'
        else:
            return False,'余额不足'
    else:
        return False,'对方账号不存在'



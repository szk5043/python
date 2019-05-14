# --*-- coding:utf-8 --*--
# @Time   ： 2019/5/10 15:06
# @Author : Wesley
# @File   : shopping.py

from db import db_handler
from interface import bank
from lib import common

shopping_logger = common.get_logger('shopping')

def shopping_cart_interface(user, shopping_cart):
    '''购物车接口：将商品加入购物车'''
    user_dic = db_handler.select(user)
    for shop, shop_dic in shopping_cart.items():
        price = shop_dic['price']
        if shop in user_dic['shopping_cart']:
            user_dic['shopping_cart'][shop]['number'] += 1
        else:
            user_dic['shopping_cart'][shop] = {'price': price, 'number': 1}
        user_dic['bankflow'].append('%s成功添加%s商品进购物车' % (user, shop))
        shopping_logger.info('%s成功添加%s商品进购物车' % (user, shop))
        db_handler.save(user_dic)
        #return '%s成功添加%s商品进购物车' % (user, shop)


def pay_interface(user, shopping_cart):
    '''结账接口：
           1、判断用户余额是否大于商品总价
           1、加入购物袋
           2、清空购物车
           3、调用付款接口付款
    '''
    user_dic = db_handler.select(user)
    cost = 0  # 总价
    for shop, shop_dic in shopping_cart.items():
        price = shop_dic['price']
        # 如果商品在用户购物车中已存在则+1，不存在则新增
        if shop in user_dic['shopping_cart']:
            user_dic['shopping_cart'][shop]['number'] += 1
        user_dic['shopping_cart'][shop] = {'price': price, 'number': 1}
        number = user_dic['shopping_cart'][shop]['number']
        cost += (price * number)
    if cost > user_dic['balance']:
        shopping_logger.info('余额不足，无法付款')
        return False#, '余额不足，无法付款'
    # 将购物车商品加入购物袋，并清空购物车
    for shop, shop_dic in user_dic['shopping_cart'].items():
        price = shop_dic['price']
        if shop in user_dic['reticule']:
            user_dic['reticule'][shop]['number'] += 1
        user_dic['reticule'][shop] = {'price': price, 'number': 1}
    user_dic['shopping_cart'] = {}
    bank.pay_interface(user, cost)
    db_handler.save(user_dic)
    return True


def check_shop_cart_interface(user):
    '''查看购物车接口'''
    user_dic = db_handler.select(user)
    reticule = user_dic['reticule']
    return reticule

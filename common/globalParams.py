#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Date    : 2017/3/14 13:07
# @Version : python 3.4
# @Author  : KingDow


def global_init():  # 初始化
    global global_dict
    global_dict = {}


def set_value(key, value):
    """ 定义一个全局变量 """
    global_dict[key] = value


def get_value(key, default_value=''):
    """ 获得一个全局变量,不存在则返回默认值 """
    try:
        return global_dict[key]
    except KeyError:
        return default_value

# login_uid
# agent_name
# agent_part
# bloger_group
# agent_phone
# resblock_id
# resblock_name
# buildingNo
# unit
# floor
# room_no
# firstSourceId
# secondSource
# userName
# telPhone
# gender
# keeperOwnerUid
# toKeeperTypeName
# house_id
# busopp_id
# repairId
# repairCode
# paywayId
# paywayCode
# standard_id
# assess_code
# rent_price

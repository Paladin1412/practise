#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Date    : 2017/3/14 13:07
# @Version : python 3.4
# @Author  : KingDow


def init():  # 初始化
    global global_dict
    global_dict = {}


def set_value(key, value):
    """ 定义一个全局变量 """
    global_dict[key] = value


def get_value(key, default_value=None):
    """ 获得一个全局变量,不存在则返回默认值 """
    try:
        return global_dict[key]
    except KeyError:
        return default_value

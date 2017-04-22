#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Date    : 2017/3/14 13:07
# @Version : python 3.4
# @Author  : KingDow
import pymysql
import time


class GlobalParams(object):
    def __init__(self):
        ###########################################################
        # MySQL数据库配置
        self.mysql_name = 'newziroom'
        self.mysql_config = {
            'host': '10.16.24.231',
            'port': 3306,
            'user': 'root',
            'password': '123456',
            'charset': 'utf8mb4',
            'cursorclass': pymysql.cursors.DictCursor
        }

        ###########################################################
        # Oracle数据库配置
        self.orcl_user = 'hlasset'
        self.orcl_pswd = 'oracle'
        self.orcl_config = ('10.16.16.10', 1521, 'svdp')

        ###########################################################
        self.header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) Chrome/56.0.2896.3 Safari/537.36'}
        self.host = 'www.ziroom.com'
        self.crm_domain = 's.t.ziroom.com'

        ###########################################################
        self.user_info = {
            'username': '',
            'password': ''
        }

        ###########################################################
        self.logconf = {
            'path': '../log/error-%s.log' % time.strftime(
                '%Y-%m-%d', time.localtime(time.time())),
            'console_level': 'INFO',
            'file_level': 'DEBUG'
        }

#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Date    : 2017/3/14 13:07
# @Version : python 3.4
# @Author  : KingDow
import pymysql
import time
from httpconfig import HttpConfig
from dbconfig import MysqlConfig, OracleConfig
from logconfig import Logger


class GlobalParams(object):
    def __init__(self):
        mysql_name = 'newziroom'
        mysql_config = {
            'host': '10.16.24.231',
            'port': 3306,
            'user': 'root',
            'password': '123456',
            'charset': 'utf8mb4',
            'cursorclass': pymysql.cursors.DictCursor
        }
        orcl_user = 'hlasset'
        orcl_pswd = 'oracle'
        orcl_config = ('10.16.16.10', 1521, 'svdp')

        header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) Chrome/56.0.2896.3 Safari/537.36'
        }
        host = 'www.ziroom.com'

        log_config = {
            'file_path': '../log/error-%s.log' % time.strftime('%Y-%m-%d', time.localtime(time.time())),
            'console_level': 'logging.INFO',
            'file_level': 'logging.DEBUG'
        }

        self.http = HttpConfig(host=host, headers=header)
        self.mysql = MysqlConfig(config=mysql_config, db=mysql_name)
        self.oracle = OracleConfig(orcl_config, orcl_user, orcl_pswd)
        self.logger = Logger(log_config.get('file_path'), log_config.get('console_level'), log_config.get('file_level'))

    def get_http(self):
        return self.http

    def get_mysql_conn(self):
        return self.mysql.mysql_conn()

    def get_orcl_conn(self):
        return self.oracle.oracle_conn()

    def close_mysql_conn(self):
        self.mysql.mysql_close()

    def close_orcl_conn(self):
        self.oracle.oracle_close()

    def log(self):
        return self.logger

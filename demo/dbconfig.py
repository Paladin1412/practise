#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Date    : 2017/3/14 13:06
# @Version : python 3.4
# @Author  : KingDow
import cx_Oracle
import pymysql
import sys


class MysqlConfig(object):
    def __init__(self, config, db):
        self.config = config
        self.db = db

    def mysql_conn(self):
        config = self.config
        try:
            conn = pymysql.connect(**config).select_db(self.db)
            return conn
        except Exception as e:
            print('MySQL数据库链接异常---->>%s' % e)
            sys.exit()

    def mysql_close(self):
        self.mysql_conn().close()


class OracleConfig(object):
    def __init__(self, orcl_config, username, password):
        self.orcl_config = orcl_config
        self.username = username
        self.password = password

    def oracle_conn(self):
        try:
            tns = cx_Oracle.makedsn(*self.orcl_config)
            conn = cx_Oracle.connect(self.username, self.password, tns)
            return conn
        except Exception as e:
            print('Oracle数据库链接异常---->>%s' % e)
            sys.exit()

    def oracle_close(self):
        self.oracle_conn().close()

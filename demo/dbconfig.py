#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Date    : 2017/3/14 13:06
# @Version : python 3.4
# @Author  : KingDow
import sys

import cx_Oracle
import pymysql

from demo.globalparams import GlobalParams


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


class OracleConfig(object):
    def __init__(self, orcl_config, orcl_user, orcl_pswd):
        self.orcl_config = orcl_config
        self.username = orcl_user
        self.password = orcl_pswd

    def oracle_conn(self):
        try:
            tns = cx_Oracle.makedsn(*self.orcl_config)
            conn = cx_Oracle.connect(self.username, self.password, tns)
            return conn
        except Exception as e:
            print('Oracle数据库链接异常---->>%s' % e)
            sys.exit()


class GetMysql(object):
    def __init__(self):
        gp = GlobalParams()
        self.config = gp.mysql_config
        self.db = gp.mysql_name
        self.mysql = MysqlConfig(config=self.config, db=self.db)

    def get_mysql_conn(self):
        return self.mysql.mysql_conn()

    def mysql_close(self):
        self.mysql.mysql_conn().close()


class GetOracle(object):
    def __init__(self):
        gp = GlobalParams()
        self.oracle = OracleConfig(gp.orcl_config, gp.orcl_user, gp.orcl_pswd)

    def get_oracle_conn(self):
        return self.oracle.oracle_conn()

    def oracle_close(self):
        self.oracle.oracle_conn().close()

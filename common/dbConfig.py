#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Date    : 2017/3/14 13:06
# @Version : python 3.4
# @Author  : KingDow
import sys
import cx_Oracle
import pymysql
from common import readConfig
from common.logConfig import GetLog

log = GetLog().log()


class MysqlConfig(object):
    def __init__(self, db, config):
        self.db = db
        self.config = config
        self.conn = None

    def get_mysql_conn(self):
        try:
            self.conn = pymysql.connect(**self.config)
            self.conn.select_db(self.db)
            if self.conn: log.debug('Connect MySQL DB successfully!')
            return self.conn
        except Exception as e:
            log.error('MySQL数据库链接异常---->>%s' % e)
            sys.exit()

    def mysql_conn_close(self):
        self.conn.close()
        log.debug('Closed MySQL DB Successfully!')


class OracleConfig(object):
    def __init__(self, user, pwd, config):
        self.orcl_config = config
        self.username = user
        self.password = pwd
        self.conn = None

    def oracle_conn(self):
        try:
            tns = cx_Oracle.makedsn(*self.orcl_config)
            self.conn = cx_Oracle.connect(self.username, self.password, tns)
            if self.conn: log.debug('Connect Oracle DB Successfully!')
            return self.conn
        except Exception as e:
            log.error('Oracle数据库链接异常---->>%s' % e)
            sys.exit()


class GetMysql(object):
    def __init__(self, db, config):
        read_config = readConfig.ReadConfig()
        dbname = read_config.conf_mysql(db)
        dbconfig = read_config.conf_mysql(config)
        self.mysql = MysqlConfig(db=dbname, config=dbconfig)

    def get_mysql_conn(self):
        return self.mysql.get_mysql_conn()

    def mysql_conn_close(self):
        self.mysql.conn.close()
        log.debug('Closed MySQL DB Successfully!')


class GetOracle(object):
    def __init__(self, user, pwd, config):
        read_config = readConfig.ReadConfig()
        dbuser = read_config.conf_oracle(user)
        dbpwd = read_config.conf_oracle(pwd)
        dbconfig = read_config.conf_oracle(config)
        self.oracle = OracleConfig(user=dbuser, pwd=dbpwd, config=dbconfig)

    def get_oracle_conn(self):
        return self.oracle.oracle_conn()

    def oracle_close(self):
        self.oracle.oracle_conn().close()
        log.debug('Closed Oracle DB Successfully!')

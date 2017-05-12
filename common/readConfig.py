#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Date    : 2017/4/22 20:01
# @Version : python 3.4
# @Author  : KingDow
import configparser
import json
import os
import time

# 项目根目录
rootPath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 配置文件目录
configPath = os.path.join(rootPath, "config", "testConfig.ini")
# 日志目录
logPath = os.path.join(rootPath, "log", 'error-%s.log' % time.strftime(
    '%Y-%m-%d', time.localtime(time.time())))


class ReadConfig(object):
    def __init__(self):
        self.cf = configparser.ConfigParser()
        self.cf.read(configPath)

    def conf_format(self, section, key):
        value = self.cf.get(section, key)
        if value[0] == value[-1] in ("'", '"'):
            value = value[1:-1]
        if value[0] == '{' and value[-1] == '}' and ':'.find(value):
            try:
                return json.loads(value.replace("'", '"'))
            except ValueError:
                return eval(value)
        return value

    def conf_http(self, name):
        return self.conf_format("HTTP", name)

    def conf_db1(self, name):
        return self.conf_format("MYSQL", name)

    def conf_db2(self, name):
        return self.conf_format("ORACLE", name)

    def conf_email(self, name):
        return self.conf_format("EMAIL", name)

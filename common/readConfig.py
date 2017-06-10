#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Date    : 2017/4/22 20:01
# @Version : python 3.4
# @Author  : KingDow
import ast
import configparser
import os
import time

# 项目根目录
rootPath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 配置文件目录
configPath = os.path.join(rootPath, "config", "testConfig.ini")
# 参数配置
keeperParanmsPath = os.path.join(rootPath, "proAPI", "keeper", "keeperParam", "keeperParams.ini")
# 日志目录
logPath = os.path.join(rootPath, "log", 'error-%s.log' % time.strftime(
    '%Y-%m-%d', time.localtime(time.time())))


class ReadConfig(object):
    def __init__(self, conf_path='configPath'):
        self.cf = configparser.ConfigParser()
        if conf_path == 'configPath':
            self.cf.read(configPath)
        elif conf_path == 'keeperParanmsPath':
            self.cf.read(keeperParanmsPath)
        else:
            print('---->> configPath ERROR！')

    def conf_format(self, section, key):
        value = self.cf.get(section, key)
        try:
            newvalue = ast.literal_eval(value)
        except ValueError:
            newvalue = value
        return newvalue

    def conf_value(self, section, key):
        return self.conf_format(section, key)

#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Date    : 2017/4/22 20:01
# @Version : python 3.4
# @Author  : KingDow
import configparser
import json
import os
import time

os.chdir('../config')
configPath = os.path.join(os.getcwd(), "test.ini")
os.chdir('../log')
logPath = os.path.join(os.getcwd(), 'error-%s.log' % time.strftime(
    '%Y-%m-%d', time.localtime(time.time())))


class ReadConfig(object):
    def __init__(self):
        # fd = open(configPath)
        # data = fd.read()
        #
        # #  remove BOM
        # if data[:3] == codecs.BOM_UTF8:
        #     data = data[3:]
        #     file = codecs.open(configPath, "w")
        #     file.write(data)
        #     file.close()
        # fd.close()

        self.cf = configparser.ConfigParser()
        self.cf.read(configPath)

    def conf_format(self, section, key):
        value = self.cf.get(section, key)
        if value[0] == value[-1] in("'", '"'):
            value = value[1:-1]

        if value[0] == '{' and value[-1] == '}' and ':'.find(value):
            return json.loads(value.replace("'", '"'))
        return value

    def conf_http(self, name):
        return self.conf_format("HTTP", name)

    def conf_db(self, name):
        return self.conf_format("MYSQL1", name)

# a = ReadConfig()
# b = a.conf_format("HTTP", "header")
# print(type(b), b)

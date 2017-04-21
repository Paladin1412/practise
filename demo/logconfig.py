#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Date    : 2017/3/14 13:07
# @Version : python 3.4
# @Author  : KingDow
import logging
import logging.handlers

from demo.globalparams import GlobalParams


class Logger(object):
    def __init__(self, path, console_level=logging.DEBUG, file_level=logging.DEBUG):
        self.logger = logging.getLogger(path)
        self.logger.setLevel(logging.DEBUG)
        fmt = logging.Formatter('%(asctime)s %(levelname)s %(message)s', '%Y-%m-%d %H:%M:%S')

        # 设置CMD /Console日志
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(fmt)
        stream_handler.setLevel(console_level)

        # 设置文件日志
        file_handler = logging.FileHandler(path)
        # 设置文件大小以及最多同时存在的数量
        date_handler = logging.handlers.TimedRotatingFileHandler(path, when='D', interval=1, backupCount=10)
        # size_handler = logging.handlers.RotatingFileHandler(path, maxBytes=20, backupCount=5)
        file_handler.setFormatter(fmt)
        file_handler.setLevel(file_level)

        self.logger.addHandler(stream_handler)
        # self.logger.addHandler(file_handler)
        self.logger.addHandler(date_handler)

    def debug(self, message):
        self.logger.debug(message)

    def info(self, message):
        self.logger.info(message)

    def warning(self, message):
        self.logger.warning(message)

    def error(self, message):
        self.logger.error(message)

    def critical(self, message):
        self.logger.critical(message)


class GetLog(object):
    def __init__(self):
        gp = GlobalParams()
        self.logger = Logger(gp.logconf['path'], gp.logconf['console_level'], gp.logconf['file_level'])

    def log(self):
        return self.logger

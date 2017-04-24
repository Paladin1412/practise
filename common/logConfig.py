#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Date    : 2017/3/14 13:07
# @Version : python 3.4
# @Author  : KingDow
import logging
import logging.handlers
import threading

from common import readConfig


class Logger(object):
    def __init__(self, path, console_level=logging.INFO, file_level=logging.DEBUG):
        self.logger = logging.getLogger(path)
        self.logger.setLevel(logging.DEBUG)
        fmt = logging.Formatter('%(asctime)s %(levelname)s %(message)s', '%Y-%m-%d %H:%M:%S')

        # 设置CMD /Console日志
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(fmt)
        stream_handler.setLevel(console_level)

        # 设置文件日志
        date_handler = logging.handlers.TimedRotatingFileHandler(path, when='D', interval=1, backupCount=30)
        date_handler.setFormatter(fmt)
        date_handler.setLevel(file_level)

        self.logger.addHandler(stream_handler)
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
    def __init__(self, path=readConfig.logPath):
        self.path = path
        self.logger = None
        self.tl = threading.Lock()

    def log(self):
        if not self.logger:
            self.tl.acquire()
            self.logger = Logger(path=self.path)
            self.tl.release()
        return self.logger

#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Date    : 2017/3/14 13:07
# @Version : python 3.4
# @Author  : KingDow
import logging
import logging.handlers
import threading
from common import readConfig

# Color escape string
COLOR_RED = '\033[1;31m'
COLOR_GREEN = '\033[1;32m'
COLOR_YELLOW = '\033[1;33m'
COLOR_BLUE = '\033[1;34m'
COLOR_PURPLE = '\033[1;35m'
COLOR_CYAN = '\033[1;36m'
COLOR_GRAY = '\033[1;37m'
COLOR_WHITE = '\033[1;38m'
COLOR_RESET = '\033[1;0m'

# Define log color
LOG_COLORS = {
    'DEBUG': '%s',
    'INFO': COLOR_GREEN + '%s' + COLOR_RESET,
    'WARNING': COLOR_YELLOW + '%s' + COLOR_RESET,
    'ERROR': COLOR_RED + '%s' + COLOR_RESET,
    'CRITICAL': COLOR_RED + '%s' + COLOR_RESET,
    'EXCEPTION': COLOR_RED + '%s' + COLOR_RESET,
}


class Logger(object):
    def __init__(self, path, console_level=logging.INFO, file_level=logging.DEBUG):
        self.logger = logging.getLogger(__name__)
        if not len(self.logger.handlers):
            self.logger.setLevel(logging.DEBUG)
            fmt = logging.Formatter('%(asctime)s | %(levelname)-8s | %(message)s', '%Y-%m-%d %H:%M:%S')

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
        self.tl = threading.Lock()

    def log(self):
        self.tl.acquire()
        logger = Logger(path=self.path)
        self.tl.release()
        return logger

#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Date    : 2017/3/14 13:07
# @Version : python 3.4
# @Author  : KingDow
import os


class CommonFunc(object):
    def __init__(self, path):
        self.path = path

    def is_path(self):
        return os.path.isdir(self.path)

    def is_path_exist(self):
        if not os.path.exists(self.path):
            os.makedirs(self.path)

    def is_file_exist(self):
        try:
            with open(self.path) as f:
                f.close()
                return True
        except IOError:
            return False

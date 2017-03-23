#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Date    : 2017/3/14 13:08
# @Version : python 3.4
# @Author  : KingDow
import nose
from demo import DemoTest

if __name__ == '__main__':
    demo = DemoTest()
    result = nose.run()

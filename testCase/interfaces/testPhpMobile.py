#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Date    : 2017/4/24 18:04
# @Version : python 3.4
# @Author  : KingDow

from common import globalParams
from proAPI.interfaces.PhpLogin import PhpLogin
from proAPI.interfaces.PhpMobile import PhpMobile
from proAPI.ziroomer.getappid import CommonApiParas


class TestPhpMobile(object):
    def __init__(self):
        globalParams.global_init()  # 全局变量初始化
        PhpLogin().php_login_normal('suikk', '123')
        self.th = PhpMobile()

    def setUp(self):
        CommonApiParas().get_appid()
        print("MyTestClass setup")

    def tearDown(self):
        print("MyTestClass teardown")

    def test_get_is_focus_resblock(self):
        resp = self.th.get_is_focus_resblock()
        assert resp.get('status') == 'success'

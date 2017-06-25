#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Date    : 2017/4/24 16:46
# @Version : python 3.4
# @Author  : KingDow
from common import globalParams
from proAPI.interfaces.PhpLogin import PhpLogin
from proAPI.ziroomer.getappid import CommonApiParas


class TestPhpLogin(object):
    def __init__(self):
        globalParams.global_init()  # 全局变量初始化
        self.th = PhpLogin()
        self.loginName = 'suikk'
        self.password = '123'

    def setUp(self):
        CommonApiParas().get_appid()
        print("MyTestClass setup")

    def tearDown(self):
        print("MyTestClass teardown")

    def test_php_login_normal(self):
        response = self.th.php_login_normal(self.loginName, self.password)
        assert response.get('status') == 'success'

    def test_php_statistical_information_quantity(self):
        response = self.th.php_statistical_information_quantity()
        assert response.get('status') == 'success'

    def test_php_steward_information(self):
        response = self.th.php_steward_information()
        assert response.get('status') == 'success'

    def test_php_get_announcement_list(self):
        response = self.th.php_get_announcement_list()
        assert response.get('status') == 'success'

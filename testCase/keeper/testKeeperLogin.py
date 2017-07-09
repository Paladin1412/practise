#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Date    : 2017/4/24 16:37
# @Version : python 3.4
# @Author  : KingDow
from nose.tools import assert_equal

from common import globalParams
from proAPI.keeper.KeeperLogin import KeeperLogin
from proAPI.ziroomer.getappid import CommonApiParas


class TestKeeperLogin(object):
    def __init__(self):
        globalParams.global_init()  # 全局变量初始化
        self.th = KeeperLogin()

    def setUp(self):
        CommonApiParas().get_appid()
        print("MyTestClass setup")

    def tearDown(self):
        print("MyTestClass teardown")

    def test_get_latest_version(self):
        response = self.th.get_latest_version()
        status = response.get('status')
        assert_equal(status, 'success')

    def test_get_home_page_module(self):
        response = self.th.get_home_page_module()
        status = response.get('status')
        assert_equal(status, 'success')

    def test_get_schedule_by_keeperid_and_condition(self):
        response = self.th.get_schedule_by_keeperid_and_condition()
        status = response.get('status')
        assert_equal(status, 'success')

    def test_get_app_be_evaluate(self):
        response = self.th.get_app_be_evaluate()
        status = response.get('status')
        assert_equal(status, 'success')

    def test_get_target_info(self):
        response = self.th.get_target_info()
        status = response.get('status')
        assert_equal(status, 'success')

    def test_get_all_module(self):
        response = self.th.get_all_module()
        status = response.get('status')
        assert_equal(status, 'success')

    def test_get_message_list(self):
        response = self.th.get_message_list()
        status = response.get('status')
        assert_equal(status, 'success')

#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Date    : 2017/4/24 17:49
# @Version : python 3.4
# @Author  : KingDow
from nose.tools import assert_equal

from common import globalParams
from proAPI.keeper.KeeperBusOpp import KeeperBusOpp
from proAPI.ziroomer.getappid import CommonApiParas


class TestKeeperBusOpp(object):
    def __init__(self):
        globalParams.global_init()  # 全局变量初始化
        self.th = KeeperBusOpp()

    def setUp(self):
        CommonApiParas().get_appid()
        print("MyTestClass setup")

    def tearDown(self):
        print("MyTestClass teardown")

    def test_query_perform(self):
        response = self.th.query_perform()
        status = response.get('status')
        assert_equal(status, 'success')

    def test_get_user_info_by_condition(self):
        response = self.th.get_user_info_by_condition()
        status = response.get('status')
        assert_equal(status, 'success')

    def test_app_search_bus_opp_by_standard_info(self):
        response = self.th.app_search_bus_opp_by_standard_info()
        status = response.get('status')
        assert_equal(status, 'success')

    def test_check_bus_opp(self):
        response = self.th.check_bus_opp()
        status = response.get('status')
        assert_equal(status, 'success')

    def test_query_bo_first_source_list(self):
        response = self.th.query_bo_first_source_list()
        status = response.get('status')
        assert_equal(status, 'success')

    def test_query_bo_second_source_list(self):
        response = self.th.query_bo_second_source_list()
        status = response.get('status')
        assert_equal(status, 'success')

    def test_get_keeper_by_and_source_type(self):
        response = self.th.get_keeper_by_and_source_type()
        status = response.get('status')
        assert_equal(status, 'success')

    def test_query_bo_list_by_keeper(self):
        response = self.th.query_bo_list_by_keeper()
        status = response.get('status')
        assert_equal(status, 'success')

    def test_change_bus_opp_has_look_over(self):
        response = self.th.change_bus_opp_has_look_over()
        status = response.get('status')
        assert_equal(status, 'success')

    def test_query_house_info(self):
        response = self.th.query_house_info()
        status = response.get('status')
        assert_equal(status, 'success')

    def test_add_track_by_keeper(self):
        response = self.th.add_track_by_keeper()
        status = response.get('status')
        assert_equal(status, 'success')

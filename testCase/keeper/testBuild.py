#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Date    : 2017/4/24 18:10
# @Version : python 3.4
# @Author  : KingDow
from nose.tools import assert_equal

from common import globalParams
from proAPI.keeper.Build import BuildInfo
from proAPI.ziroomer.getappid import CommonApiParas


class TestBuildInfo(object):
    def __init__(self):
        globalParams.global_init()  # 全局变量初始化
        self.th = BuildInfo()
        self.loginName = 'suikk'
        self.password = '123'

    def setUp(self):
        CommonApiParas().get_appid()
        print("MyTestClass setup")

    def tearDown(self):
        print("MyTestClass teardown")

    def test_get_district_list(self):
        response = self.th.get_district_list()
        status = response.get('status')
        assert_equal(status, 'success')

    def test_get_village_list(self):
        response = self.th.get_village_list()
        status = response.get('status')
        assert_equal(status, 'success')

    def test_get_build_num_list(self):
        response = self.th.get_build_num_list()
        status = response.get('status')
        assert_equal(status, 'success')

    def test_get_unit_list(self):
        response = self.th.get_unit_list()
        status = response.get('status')
        assert_equal(status, 'success')

    def test_get_floor_list(self):
        response = self.th.get_floor_list()
        status = response.get('status')
        assert_equal(status, 'success')

    def test_get_room_num_list(self):
        response = self.th.get_room_num_list()
        status = response.get('status')
        assert_equal(status, 'success')

#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Date    : 2017/4/24 17:52
# @Version : python 3.4
# @Author  : KingDow
from common import globalParams
from proAPI.busopp.BusOpp import BusOpp
from proAPI.ziroomer.getappid import CommonApiParas


class TestBusOpp(object):
    def __init__(self):
        globalParams.global_init()  # 全局变量初始化
        self.th = BusOpp()

    def setUp(self):
        CommonApiParas().get_appid()
        print("MyTestClass setup")

    def tearDown(self):
        print("MyTestClass teardown")

    def test_query_opp_page_info(self):
        response = self.th.query_opp_page_info()
        assert response.get('status') == 'success'

    def test_query_opp_life_cycle_new(self):
        response = self.th.query_opp_life_cycle_new()
        assert response.get('status') == 'success'

    def test_get_child_list_by_ident(self):
        response = self.th.get_child_list_by_ident()
        assert response.get('status') == 'success'

    def test_get_survey_info_list_by_house_id(self):
        response = self.th.get_survey_info_list_by_house_id()
        assert response.get('status') == 'success'

    def test_commit_survey(self):
        response = self.th.commit_survey()
        assert response.get('status') == 'success'


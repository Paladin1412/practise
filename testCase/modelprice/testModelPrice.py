#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Date    : 2017/6/25 22:31
# @Version : python 3.4
# @Author  : KingDow
from common import globalParams
from proAPI.keeper.Build import BuildInfo
from proAPI.modelprice.ModelPrice import ModelPrice
from proAPI.ziroomer.getappid import CommonApiParas


class TestModelPrice(object):
    def __init__(self):
        globalParams.global_init()  # 全局变量初始化
        self.th = ModelPrice()
        self.loginName = 'suikk'
        self.password = '123'

    def setUp(self):
        CommonApiParas().get_appid()
        print("MyTestClass setup")

    def tearDown(self):
        print("MyTestClass teardown")

    def test_modelprice_login(self):
        response = self.th.modelprice_login()
        assert response.get('status') == 'success'

    def test_guide_index(self):
        response = self.th.guide_index()
        assert response.get('status') == 'success'

    def test_resblock_info(self):
        response = self.th.resblock_info()
        assert response.get('status') == 'success'

    def test_district_info(self):
        response = self.th.district_info()
        assert response.get('status') == 'success'

    def test_get_resblock(self):
        response = self.th.get_resblock()
        assert response.get('status') == 'success'

    def test_get_is_focus(self):
        response = self.th.get_is_focus()
        assert response.get('status') == 'success'

    def test_get_building_info(self):
        response = self.th.get_building_info()
        assert response.get('status') == 'success'

    def test_get_unit_info(self):
        response = self.th.get_unit_info()
        assert response.get('status') == 'success'

    def test_get_floor_info(self):
        response = self.th.get_floor_info()
        assert response.get('status') == 'success'

    def test_get_room_info(self):
        response = self.th.get_room_info()
        assert response.get('status') == 'success'

    def test_get_standard_info(self):
        response = self.th.get_standard_info()
        assert response.get('status') == 'success'

    def test_commit_house_info(self):
        response = self.th.commit_house_info()
        assert response.get('status') == 'success'

    def test_detail_house_info(self):
        response = self.th.detail_house_info()
        assert response.get('status') == 'success'

    def test_get_rent_price(self):
        response = self.th.get_rent_price()
        assert response.get('status') == 'success'

    def test_commit_room_info(self):
        response = self.th.commit_room_info()
        assert response.get('status') == 'success'

    def test_commit_config_info(self):
        response = self.th.commit_config_info()
        assert response.get('status') == 'success'

    def test_get_hire_price(self):
        response = self.th.get_hire_price()
        assert response.get('status') == 'success'

    def test_get_assess_result(self):
        response = self.th.get_assess_result()
        assert response.get('status') == 'success'

    def test_commit_assess_info(self):
        response = self.th.commit_assess_info()
        assert response.get('status') == 'success'

    def test_assess_list_info(self):
        response = self.th.assess_list_info()
        assert response.get('status') == 'success'

    def test_view_assess_info(self):
        response = self.th.view_assess_info()
        assert response.get('status') == 'success'

    def test_admit_assess_info(self):
        response = self.th.admit_assess_info()
        assert response.get('status') == 'success'

    def test_undo_assess_info(self):
        response = self.th.undo_assess_info()
        assert response.get('status') == 'success'

    def test_del_assess_info(self):
        response = self.th.del_assess_info()
        assert response.get('status') == 'success'

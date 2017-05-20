#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Date    : 2017/5/14 11:53
# @Version : python 3.4
# @Author  : KingDow
from common import globalParams
from testCase.busopp.testBusOpp import BusOpp
from testCase.interfaces.testPhpLogin import PhpLogin
from testCase.interfaces.testPhpMobile import PhpMobile
from testCase.keeper.testBuild import BuildInfo
from testCase.keeper.testKeeperBusOpp import KeeperBusOpp
from testCase.keeper.testKeeperLogin import KeeperLogin

if __name__ == '__main__':
    globalParams.init()  # 全局变量初始化

    test = PhpLogin()
    test.test_php_login_normal()
    test.test_php_statistical_information_quantity()
    test.test_php_steward_information()
    test.test_php_get_announcement_list()

    mobile = PhpMobile()
    mobile.test_get_is_focus_resblock()

    crm = BuildInfo()
    crm.test_get_build_num_list()
    crm.test_get_unit_list()
    crm.test_get_floor_list()
    crm.test_get_room_num_list()

    crm1 = KeeperLogin()
    crm1.test_get_latest_version()
    crm1.test_get_district_list()
    crm1.test_get_home_page_module()
    crm1.test_get_schedule_by_keeperid_and_condition()
    crm1.test_get_app_be_evaluate()
    crm1.test_get_target_info()
    crm1.test_get_all_module()
    crm1.test_get_message_list()

    crm2 = KeeperBusOpp()
    crm2.test_query_perform()
    crm2.test_get_user_info_by_condition()
    crm2.test_get_village_list()
    crm2.test_app_search_bus_opp_by_standard_info()
    crm2.test_check_bus_opp()
    crm2.test_query_bo_first_source_list()
    crm2.test_query_bo_second_source_list()
    crm2.test_get_keeper_by_and_source_type()

    busopp = BusOpp()
    busopp.test_query_opp_page_info()

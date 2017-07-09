#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Date    : 2017/5/14 11:53
# @Version : python 3.4
# @Author  : KingDow

from common import globalParams
from proAPI.busopp.BusOpp import BusOpp
from proAPI.keeper.Build import BuildInfo
from proAPI.keeper.KeeperBusOpp import KeeperBusOpp
from proAPI.keeper.KeeperLogin import KeeperLogin
from proAPI.modelprice.ModelPrice import ModelPrice
from testCase.interfaces.testPhpLogin import PhpLogin
from testCase.ziroomer.getappid import CommonApiParas

if __name__ == '__main__':
    globalParams.global_init()  # 全局变量初始化
    CommonApiParas().get_appid()

    test = PhpLogin()
    test.php_login_normal('huangcx9', '123')
    test.php_statistical_information_quantity()
    test.php_steward_information()
    test.php_get_announcement_list()

    # mobile = PhpMobile()
    # mobile.get_is_focus_resblock()

    crm = BuildInfo()
    crm.get_district_list()
    crm.get_village_list()
    crm.get_build_num_list()
    crm.get_unit_list()
    crm.get_floor_list()
    crm.get_room_num_list()

    crm1 = KeeperLogin()
    crm1.get_latest_version()
    crm1.get_home_page_module()
    crm1.get_schedule_by_keeperid_and_condition()
    crm1.get_app_be_evaluate()
    crm1.get_target_info()
    crm1.get_all_module()
    crm1.get_message_list()

    crm2 = KeeperBusOpp()
    crm2.query_perform()
    crm2.get_user_info_by_condition()
    crm2.app_search_bus_opp_by_standard_info()
    crm2.check_bus_opp()
    crm2.query_bo_first_source_list()
    crm2.query_bo_second_source_list()
    crm2.get_keeper_by_and_source_type()
    crm2.create_busopp()

    crm2.query_bo_list_by_keeper()
    crm2.change_bus_opp_has_look_over()
    crm2.query_house_info()
    crm2.add_track_by_keeper()

    busopp = BusOpp()
    busopp.query_opp_page_info()
    busopp.query_opp_life_cycle_new()
    busopp.get_child_list_by_ident()
    busopp.get_child_list_by_ident('repair')
    busopp.get_child_list_by_ident('payway')
    busopp.get_survey_info_list_by_house_id()
    busopp.commit_survey()

    modelprice = ModelPrice()
    modelprice.modelprice_login()
    # modelprice.guide_index()
    modelprice.resblock_info()
    modelprice.district_info()
    modelprice.get_resblock()
    modelprice.get_is_focus()

    modelprice.get_building_info()
    modelprice.get_unit_info()
    modelprice.get_floor_info()
    modelprice.get_room_info()
    modelprice.get_standard_info()
    modelprice.commit_house_info()
    modelprice.detail_house_info()
    modelprice.get_rent_price()
    modelprice.commit_room_info()
    modelprice.commit_config_info()
    modelprice.get_hire_price()
    modelprice.get_assess_result()
    modelprice.commit_assess_info()
    modelprice.assess_list_info()
    modelprice.view_assess_info()
    modelprice.admit_assess_info()
    # modelprice.undo_assess_info()
    # modelprice.del_assess_info()

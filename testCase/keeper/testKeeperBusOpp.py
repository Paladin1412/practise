#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Date    : 2017/4/24 17:49
# @Version : python 3.4
# @Author  : KingDow
from common import commFunc
from common import globalParams
from common.httpConfig import GetHttp
from common.logConfig import GetLog
from testCase.keeper.keeperParams.keeperParms import KeeperParams


class KeeperBusOpp(object):
    def __init__(self):
        self.log = GetLog().log()
        self.http = GetHttp('crm_domain').get_http()

    def test_query_perform(self):
        """
        不同线索来源列表
        :return:
        """
        url = '/busopp/queryPerform'
        data = {'keeperId': globalParams.get_value('login_uid'),
                'appType': KeeperParams().appType,
                'source': KeeperParams().source,
                'keeperCode': globalParams.get_value('login_uid'),
                'osType': KeeperParams().osType,
                'imei': KeeperParams().imei,
                'versionInt': KeeperParams().versionInt,
                'uuid': KeeperParams().app_id() + commFunc.timestamp_13(),
                'timestamp': commFunc.timestamp_13(),
                'appId': globalParams.get_value('app_id'),
                'cityCode': KeeperParams().cityCode
                }
        data['sign'] = commFunc.get_crm_sign(data)
        resp = self.http.http_post(url, data)
        return resp

    def test_get_user_info_by_condition(self):
        url = '/user/getUserInfoByCondition'
        data = {'appType': KeeperParams().appType,
                'source': KeeperParams().source,
                'keeperCode': globalParams.get_value('login_uid'),
                'osType': KeeperParams().osType,
                'imei': KeeperParams().imei,
                'versionInt': KeeperParams().versionInt,
                'uuid': KeeperParams().app_id() + commFunc.timestamp_13(),
                'timestamp': commFunc.timestamp_13(),
                'condition': KeeperParams().condition,
                'appId': globalParams.get_value('app_id'),
                'cityCode': KeeperParams().cityCode
                }
        data['sign'] = commFunc.get_crm_sign(data)
        resp = self.http.http_post(url, data)
        return resp

    def test_get_village_list(self):
        url = '/house/getVillageList'
        data = {'source': KeeperParams().source,
                'uuid': KeeperParams().app_id() + commFunc.timestamp_13(),
                'timestamp': commFunc.timestamp_13(),
                'resblock': KeeperParams().resblock,
                'appId': globalParams.get_value('app_id'),
                'cityCode': KeeperParams().cityCode,
                'keeperId': globalParams.get_value('login_uid'),
                'districtId': KeeperParams().districtId,
                'appType': KeeperParams().appType,
                'keeperCode': globalParams.get_value('login_uid'),
                'osType': KeeperParams().osType,
                'imei': KeeperParams().imei,
                'versionInt': KeeperParams().versionInt
                }
        data['sign'] = commFunc.get_crm_sign(data)
        resp = self.http.http_post(url, data)
        return resp

    def test_app_search_bus_opp_by_standard_info(self):
        url = '/busopp/appSearchBusOppByStandardInfo'
        data = {'source': KeeperParams().source,
                'buildNum': '11%E5%8F%B7%E6%A5%BC',
                'uuid': KeeperParams().app_id() + commFunc.timestamp_13(),
                'timestamp': commFunc.timestamp_13(),
                'appId': globalParams.get_value('app_id'),
                'roomNum': '402',
                'cityCode': KeeperParams().cityCode,
                'districtId': KeeperParams().districtId,
                'keeperId': globalParams.get_value('login_uid'),
                'appType': KeeperParams().appType,
                'keeperCode': globalParams.get_value('login_uid'),
                'osType': KeeperParams().osType,
                'imei': KeeperParams().imei,
                'versionInt': KeeperParams().versionInt,
                'unit': '2%E5%8D%95%E5%85%83',
                'floor': KeeperParams().floor,
                'villageId': '1111027374425'
                }
        data['sign'] = commFunc.get_crm_sign(data)
        resp = self.http.http_post(url, data)
        return resp

    def test_check_bus_opp(self):
        url = '/busopp/checkBusOpp'
        data = {'source': KeeperParams().source,
                'buildNum': '11%E5%8F%B7%E6%A5%BC',
                'uuid': KeeperParams().app_id() + commFunc.timestamp_13(),
                'districtName': '%E6%9C%9D%E9%98%B3',
                'timestamp': commFunc.timestamp_13(),
                'appId': globalParams.get_value('app_id'),
                'roomNum': '402',
                'cityCode': KeeperParams().cityCode,
                'districtId': KeeperParams().districtId,
                'appType': KeeperParams().appType,
                'keeperCode': globalParams.get_value('login_uid'),
                'osType': KeeperParams().osType,
                'imei': KeeperParams().imei,
                'versionInt': KeeperParams().versionInt,
                'isTopBaseFloor': '0',
                'villageName': '%E8%8A%B3%E5%9B%AD%E9%87%8C',
                'unit': KeeperParams().unit,
                'floor': KeeperParams().floor,
                'villageId': '1111027374425'
                }
        data['sign'] = commFunc.get_crm_sign(data)
        resp = self.http.http_post(url, data)
        return resp

    def test_query_bo_first_source_list(self):
        url = '/busopp/queryBOFirstSourceList'
        data = {'appType': KeeperParams().appType,
                'source': KeeperParams().source,
                'keeperCode': globalParams.get_value('login_uid'),
                'osType': KeeperParams().osType,
                'imei': KeeperParams().imei,
                'versionInt': KeeperParams().versionInt,
                'uuid': KeeperParams().app_id() + commFunc.timestamp_13(),
                'timestamp': commFunc.timestamp_13(),
                'appId': globalParams.get_value('app_id'),
                'boType': '1',
                'cityCode': KeeperParams().cityCode
                }
        data['sign'] = commFunc.get_crm_sign(data)
        resp = self.http.http_post(url, data)
        return resp

    def test_query_bo_second_source_list(self):
        url = '/busopp/queryBOSecondSourceList'
        data = {'appType': KeeperParams().appType,
                'source': KeeperParams().source,
                'keeperCode': globalParams.get_value('login_uid'),
                'osType': KeeperParams().osType,
                'imei': KeeperParams().imei,
                'versionInt': KeeperParams().versionInt,
                'uuid': KeeperParams().app_id() + commFunc.timestamp_13(),
                'timestamp': commFunc.timestamp_13(),
                'appId': globalParams.get_value('app_id'),
                'firstSourceId': '104',
                'cityCode': KeeperParams().cityCode
                }
        data['sign'] = commFunc.get_crm_sign(data)
        resp = self.http.http_post(url, data)
        return resp

    def test_get_keeper_by_and_source_type(self):
        url = '/busopp/getKeeperByAndSourceType'
        data = {'entryPersonName': '%E9%BB%84%E6%98%A5%E6%99%93',
                'source': KeeperParams().source,
                'entryPersonCode': '20189548',
                'firstSource': '153',
                'buildNum': '11%E5%8F%B7%E6%A5%BC',
                'uuid': KeeperParams().app_id() + commFunc.timestamp_13(),
                'secondSource': '151',
                'timestamp': commFunc.timestamp_13(),
                'appId': globalParams.get_value('app_id'),
                'roomNum': '402',
                'cityCode': KeeperParams().cityCode,
                'keeperId': globalParams.get_value('login_uid'),
                'districtId': KeeperParams().districtId,
                'appType': KeeperParams().appType,
                'keeperCode': globalParams.get_value('login_uid'),
                'osType': KeeperParams().osType,
                'imei': KeeperParams().imei,
                'versionInt': KeeperParams().versionInt,
                'unit': KeeperParams().unit,
                'floor': KeeperParams().floor,
                'villageId': '1111027374425'
                }
        data['sign'] = commFunc.get_crm_sign(data)
        resp = self.http.http_post(url, data)
        return resp

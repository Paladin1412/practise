#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Date    : 2017/4/24 17:49
# @Version : python 3.4
# @Author  : KingDow
import random
import time
from common import commFunc
from common import globalParams
from common.httpConfig import GetHttp
from common.logConfig import GetLog
from common.readConfig import ReadConfig
from proAPI.keeper.Build import BuildInfo


class KeeperBusOpp(object):
    def __init__(self):
        self.log = GetLog().log()
        self.http = GetHttp('crm_domain').get_http()

    def query_perform(self):
        """
        不同线索来源列表
        :return:
        """
        url = '/busopp/queryPerform'
        data = {'keeperId': globalParams.get_value('login_uid'),
                'appType': ReadConfig('keeperParams').conf_value('keeperParams', 'appType'),
                'source': ReadConfig('keeperParams').conf_value('keeperParams', 'source'),
                'keeperCode': globalParams.get_value('login_uid'),
                'osType': ReadConfig('keeperParams').conf_value('keeperParams', 'osType'),
                'imei': ReadConfig('keeperParams').conf_value('keeperParams', 'imei'),
                'versionInt': ReadConfig('keeperParams').conf_value('keeperParams', 'versionInt'),
                'uuid': globalParams.get_value('app_id') + commFunc.timestamp_13(),
                'timestamp': commFunc.timestamp_13(),
                'appId': globalParams.get_value('app_id'),
                'cityCode': ReadConfig('keeperParams').conf_value('keeperParams', 'cityCode')
                }
        data['sign'] = commFunc.get_crm_sign(data)
        resp = self.http.http_post(url, data)
        return resp

    def get_user_info_by_condition(self):
        """
        根据输入手机号码查询业主信息
        :return:
        """
        url = '/user/getUserInfoByCondition'
        data = {'appType': ReadConfig('keeperParams').conf_value('keeperParams', 'appType'),
                'source': ReadConfig('keeperParams').conf_value('keeperParams', 'source'),
                'keeperCode': globalParams.get_value('login_uid'),
                'osType': ReadConfig('keeperParams').conf_value('keeperParams', 'osType'),
                'imei': ReadConfig('keeperParams').conf_value('keeperParams', 'imei'),
                'versionInt': ReadConfig('keeperParams').conf_value('keeperParams', 'versionInt'),
                'uuid': globalParams.get_value('app_id') + commFunc.timestamp_13(),
                'timestamp': commFunc.timestamp_13(),
                'condition': ReadConfig('keeperParams').conf_value('keeperParams', 'ownerPhone'),
                'appId': globalParams.get_value('app_id'),
                'cityCode': ReadConfig('keeperParams').conf_value('keeperParams', 'cityCode')
                }
        data['sign'] = commFunc.get_crm_sign(data)
        resp = self.http.http_post(url, data)

        if resp.get('data'):
            globalParams.set_value('userName', resp.get('data')[0].get('userName'))
            globalParams.set_value('telPhone', resp.get('data')[0].get('telPhone'))
            globalParams.set_value('gender', resp.get('data')[0].get('gender'))
        else:
            self.log.warning('根据业主手机号查询业主信息为空，接口返回值：' + resp)
        return resp

    def app_search_bus_opp_by_standard_info(self):
        """
        http://s.t.ziroom.com/crm-reserve/busopp/appSearchBusOppByStandardInfo
        提交时查询现有商机
        :return:
        """
        url = '/busopp/appSearchBusOppByStandardInfo'
        data = {'source': ReadConfig('keeperParams').conf_value('keeperParams', 'source'),
                'buildNum': globalParams.get_value('buildingNo'),
                'uuid': globalParams.get_value('app_id') + commFunc.timestamp_13(),
                'timestamp': commFunc.timestamp_13(),
                'appId': globalParams.get_value('app_id'),
                'roomNum': globalParams.get_value('room_no'),
                'cityCode': ReadConfig('keeperParams').conf_value('keeperParams', 'cityCode'),
                'districtId': ReadConfig('keeperParams').conf_value('keeperParams', 'districtId'),
                'keeperId': globalParams.get_value('login_uid'),
                'appType': ReadConfig('keeperParams').conf_value('keeperParams', 'appType'),
                'keeperCode': globalParams.get_value('login_uid'),
                'osType': ReadConfig('keeperParams').conf_value('keeperParams', 'osType'),
                'imei': ReadConfig('keeperParams').conf_value('keeperParams', 'imei'),
                'versionInt': ReadConfig('keeperParams').conf_value('keeperParams', 'versionInt'),
                'unit': globalParams.get_value('unit'),
                'floor': globalParams.get_value('floor'),
                'villageId': globalParams.get_value('resblock_id')
                }
        data['sign'] = commFunc.get_crm_sign(data)
        resp = self.http.http_post(url, data)
        error_code = int(resp.get("error_code"))
        if error_code != 0:
            while True:
                build_info = BuildInfo()
                build_info.get_build_num_list()
                build_info.get_unit_list()
                build_info.get_floor_list()
                build_info.get_room_num_list()
                new_resp = self.app_search_bus_opp_by_standard_info()
                new_error_code = int(new_resp.get("error_code"))
                if new_error_code == 503178:  # 商机已录入
                    continue
                elif new_error_code == 503433:  # 商机已签约
                    continue
                else:
                    return new_resp
        return resp

    def check_bus_opp(self):
        url = '/busopp/checkBusOpp'
        data = {'source': ReadConfig('keeperParams').conf_value('keeperParams', 'source'),
                'buildNum': globalParams.get_value('buildingNo'),
                'uuid': globalParams.get_value('app_id') + commFunc.timestamp_13(),
                'districtName': ReadConfig('keeperParams').conf_value('keeperParams', 'districtName'),
                'timestamp': commFunc.timestamp_13(),
                'appId': globalParams.get_value('app_id'),
                'roomNum': globalParams.get_value('room_no'),
                'cityCode': ReadConfig('keeperParams').conf_value('keeperParams', 'cityCode'),
                'districtId': ReadConfig('keeperParams').conf_value('keeperParams', 'districtId'),
                'appType': ReadConfig('keeperParams').conf_value('keeperParams', 'appType'),
                'keeperCode': globalParams.get_value('login_uid'),
                'osType': ReadConfig('keeperParams').conf_value('keeperParams', 'osType'),
                'imei': ReadConfig('keeperParams').conf_value('keeperParams', 'imei'),
                'versionInt': ReadConfig('keeperParams').conf_value('keeperParams', 'versionInt'),
                'isTopBaseFloor': ReadConfig('keeperParams').conf_value('keeperParams', 'isTopBaseFloor'),
                'villageName': globalParams.get_value('resblock_name'),
                'unit': globalParams.get_value('unit'),
                'floor': globalParams.get_value('floor'),
                'villageId': globalParams.get_value('resblock_id')
                }
        data['sign'] = commFunc.get_crm_sign(data)
        resp = self.http.http_post(url, data)
        return resp

    def query_bo_first_source_list(self):
        """
        http://s.t.ziroom.com/crm-reserve/busopp/queryBOFirstSourceList
        一级商机来源
        :return:
        {'orderCode': 1022, 'sourceCode': '1022', 'sourceName': '自主开发', 'cityCode': '110000', 'sourceId': '104'}
        """
        url = '/busopp/queryBOFirstSourceList'
        data = {'appType': ReadConfig('keeperParams').conf_value('keeperParams', 'appType'),
                'source': ReadConfig('keeperParams').conf_value('keeperParams', 'source'),
                'keeperCode': globalParams.get_value('login_uid'),
                'osType': ReadConfig('keeperParams').conf_value('keeperParams', 'osType'),
                'imei': ReadConfig('keeperParams').conf_value('keeperParams', 'imei'),
                'versionInt': ReadConfig('keeperParams').conf_value('keeperParams', 'versionInt'),
                'uuid': globalParams.get_value('app_id') + commFunc.timestamp_13(),
                'timestamp': commFunc.timestamp_13(),
                'appId': globalParams.get_value('app_id'),
                'boType': ReadConfig('keeperParams').conf_value('keeperParams', 'boType'),
                'cityCode': ReadConfig('keeperParams').conf_value('keeperParams', 'cityCode')
                }
        data['sign'] = commFunc.get_crm_sign(data)
        resp = self.http.http_post(url, data)

        first_source_list = resp.get('data')
        if first_source_list:
            first_source = first_source_list[random.randint(0, len(first_source_list) - 1)].get('sourceId')
            globalParams.set_value('firstSourceId', first_source)
        else:
            self.log.warning('获取商机一级来源，接口返回值：' + resp)
        return resp

    def query_bo_second_source_list(self):
        """
        http://s.t.ziroom.com/crm-reserve/busopp/queryBOSecondSourceList
        二级商机来源
        :return:
        """
        url = '/busopp/queryBOSecondSourceList'
        data = {'appType': ReadConfig('keeperParams').conf_value('keeperParams', 'appType'),
                'source': ReadConfig('keeperParams').conf_value('keeperParams', 'source'),
                'keeperCode': globalParams.get_value('login_uid'),
                'osType': ReadConfig('keeperParams').conf_value('keeperParams', 'osType'),
                'imei': ReadConfig('keeperParams').conf_value('keeperParams', 'imei'),
                'versionInt': ReadConfig('keeperParams').conf_value('keeperParams', 'versionInt'),
                'uuid': globalParams.get_value('app_id') + commFunc.timestamp_13(),
                'timestamp': commFunc.timestamp_13(),
                'appId': globalParams.get_value('app_id'),
                'firstSourceId': '104',
                'cityCode': ReadConfig('keeperParams').conf_value('keeperParams', 'cityCode')
                }
        data['sign'] = commFunc.get_crm_sign(data)
        resp = self.http.http_post(url, data)

        second_source_list = resp.get('data')
        if second_source_list:
            second_source = second_source_list[random.randint(0, len(second_source_list) - 1)].get('sourceId')
            globalParams.set_value('secondSource', second_source)
        else:
            self.log.warning('获取商机二级来源，接口返回值：' + resp)
        return resp

    def get_keeper_by_and_source_type(self):
        """
        http://s.t.ziroom.com/crm-reserve/busopp/getKeeperByAndSourceType
        商机来源获取管家信息
        :return:
        """
        url = '/busopp/getKeeperByAndSourceType'
        data = {'entryPersonName': globalParams.get_value('agent_name'),
                'source': ReadConfig('keeperParams').conf_value('keeperParams', 'source'),
                'entryPersonCode': globalParams.get_value('login_uid'),
                'firstSource': '104',
                'buildNum': globalParams.get_value('buildingNo'),
                'uuid': globalParams.get_value('app_id') + commFunc.timestamp_13(),
                'secondSource': globalParams.get_value('secondSource'),
                'timestamp': commFunc.timestamp_13(),
                'appId': globalParams.get_value('app_id'),
                'roomNum': globalParams.get_value('room_no'),
                'cityCode': ReadConfig('keeperParams').conf_value('keeperParams', 'cityCode'),
                'keeperId': globalParams.get_value('login_uid'),
                'districtId': ReadConfig('keeperParams').conf_value('keeperParams', 'districtId'),
                'appType': ReadConfig('keeperParams').conf_value('keeperParams', 'appType'),
                'keeperCode': globalParams.get_value('login_uid'),
                'osType': ReadConfig('keeperParams').conf_value('keeperParams', 'osType'),
                'imei': ReadConfig('keeperParams').conf_value('keeperParams', 'imei'),
                'versionInt': ReadConfig('keeperParams').conf_value('keeperParams', 'versionInt'),
                'unit': globalParams.get_value('unit'),
                'floor': globalParams.get_value('floor'),
                'villageId': globalParams.get_value('resblock_id')
                }
        data['sign'] = commFunc.get_crm_sign(data)
        resp = self.http.http_post(url, data)

        keeper_info = resp.get('data')
        if keeper_info:
            globalParams.set_value('keeperOwnerUid', keeper_info.get('keeperOwnerUid'))
            globalParams.set_value('toKeeperTypeName', keeper_info.get('toKeeperTypeName'))
        else:
            self.log.warning('获取商机一级来源，接口返回值：' + resp)
        return resp

    def create_busopp(self):
        """
        http://s.t.ziroom.com/crm-reserve/busopp/createBusOpp
        商机来源获取管家信息
        :return:
        """
        url = '/busopp/createBusOpp'
        data = {'entryPersonCode': globalParams.get_value('login_uid'),
                'buildNum': globalParams.get_value('buildingNo'),
                'secondSource': globalParams.get_value('secondSource'),
                'imei': ReadConfig('keeperParams').conf_value('keeperParams', 'imei'),
                'isTopFloor': ReadConfig('keeperParams').conf_value('keeperParams', 'isTopBaseFloor'),
                'uuid': globalParams.get_value('app_id') + commFunc.timestamp_13(),
                'keeperId': globalParams.get_value('login_uid'),
                'floor': globalParams.get_value('floor'),
                'firstSource': '104',
                'districtId': ReadConfig('keeperParams').conf_value('keeperParams', 'districtId'),
                'ownerPhone': ReadConfig('keeperParams').conf_value('keeperParams', 'ownerPhone'),
                'cityCode': ReadConfig('keeperParams').conf_value('keeperParams', 'cityCode'),
                'villageName': globalParams.get_value('resblock_name'),
                'districtName': ReadConfig('keeperParams').conf_value('keeperParams', 'districtName'),
                'ownerKeeperCode': globalParams.get_value('login_uid'),
                'entryPersonName': globalParams.get_value('agent_name'),
                'versionInt': ReadConfig('keeperParams').conf_value('keeperParams', 'versionInt'),
                'source': ReadConfig('keeperParams').conf_value('keeperParams', 'source'),
                'timestamp': commFunc.timestamp_13(),
                'keeperName': globalParams.get_value('agent_name'),
                'unit': globalParams.get_value('unit'),
                'villageId': globalParams.get_value('resblock_id'),
                'keeperOwnerUid': globalParams.get_value('keeperOwnerUid'),
                'roomNum': globalParams.get_value('room_no'),
                'ownerTel': globalParams.get_value('TelPhone'),
                'entryPersonPhone': globalParams.get_value('agent_phone'),
                'osType': ReadConfig('keeperParams').conf_value('keeperParams', 'osType'),
                'keeperCode': globalParams.get_value('login_uid'),
                'appId': globalParams.get_value('app_id'),
                'appType': ReadConfig('keeperParams').conf_value('keeperParams', 'appType'),
                'keeperPhone': globalParams.get_value('agent_phone'),
                'operatorName': globalParams.get_value('agent_name'),
                'operatorCode': globalParams.get_value('login_uid'),
                'ownerName': globalParams.get_value('userName')
                }
        address = data['districtName'] + data['villageName'] + data['buildNum'] + data['unit'] + data[
            'floor'] + '层' + data['roomNum']
        data['address'] = address
        data['sign'] = commFunc.get_crm_sign(data)
        resp = self.http.http_post(url, data)
        return resp

    def query_bo_list_by_keeper(self):
        """
        POST http://s.t.ziroom.com/crm-reserve/busopp/queryBOListByKeeper
        :return:
        """
        url = '/busopp/queryBOListByKeeper'
        data = {
            "trackState": ReadConfig('keeperParams').conf_value('keeperParams', 'trackState'),
            "appId": globalParams.get_value('app_id'),
            "uuid": globalParams.get_value('app_id') + commFunc.timestamp_13(),
            "timestamp": commFunc.timestamp_13(),
            "keeperCode": globalParams.get_value('login_uid'),
            "keeperId": globalParams.get_value('login_uid'),
            "osType": ReadConfig('keeperParams').conf_value('keeperParams', 'osType'),
            "appType": ReadConfig('keeperParams').conf_value('keeperParams', 'appType'),
            "versionInt": ReadConfig('keeperParams').conf_value('keeperParams', 'versionInt'),
            "source": ReadConfig('keeperParams').conf_value('keeperParams', 'source'),
            "imei": ReadConfig('keeperParams').conf_value('keeperParams', 'imei'),
            "cityCode": ReadConfig('keeperParams').conf_value('keeperParams', 'cityCode')
        }
        data['sign'] = commFunc.get_crm_sign(data)
        resp = self.http.http_post(url, data)

        response = resp.get('data')
        if response:
            globalParams.set_value('busopp_id', response[0].get('busOppId'))
            globalParams.set_value('house_id', response[0].get('houseId'))
        else:
            self.log.warning('查询busOppId、houseId失败，接口返回值：' + resp)
        return resp

    def change_bus_opp_has_look_over(self):
        """
        POST http://s.t.ziroom.com/crm-reserve/busopp/changeBusOppHasLookOver HTTP/1.1
        :return:
        """
        url = '/busopp/changeBusOppHasLookOver'
        data = {
            "uuid": globalParams.get_value('app_id') + commFunc.timestamp_13(),
            "appType": ReadConfig('keeperParams').conf_value('keeperParams', 'appType'),
            "timestamp": commFunc.timestamp_13(),
            "busOppId": globalParams.get_value('busopp_id'),
            "cityCode": ReadConfig('keeperParams').conf_value('keeperParams', 'cityCode'),
            "source": ReadConfig('keeperParams').conf_value('keeperParams', 'source'),
            "versionInt": ReadConfig('keeperParams').conf_value('keeperParams', 'versionInt'),
            "osType": ReadConfig('keeperParams').conf_value('keeperParams', 'osType'),
            "keeperCode": globalParams.get_value('login_uid'),
            "appId": globalParams.get_value('app_id'),
            "imei": ReadConfig('keeperParams').conf_value('keeperParams', 'imei')
        }
        data['sign'] = commFunc.get_crm_sign(data)
        resp = self.http.http_post(url, data)
        return resp

    def query_house_info(self):
        """
        POST http://s.t.ziroom.com/crm-reserve/house/queryHouseInfo HTTP/1.1
        :return:
        """
        url = '/house/queryHouseInfo'
        data = {
            "appId": globalParams.get_value('app_id'),
            "cityCode": ReadConfig('keeperParams').conf_value('keeperParams', 'cityCode'),
            "uuid": globalParams.get_value('app_id') + commFunc.timestamp_13(),
            "osType": ReadConfig('keeperParams').conf_value('keeperParams', 'osType'),
            "timestamp": commFunc.timestamp_13(),
            "imei": ReadConfig('keeperParams').conf_value('keeperParams', 'imei'),
            "houseId": globalParams.get_value('house_id'),
            "source": ReadConfig('keeperParams').conf_value('keeperParams', 'source'),
            "keeperCode": globalParams.get_value('login_uid'),
            "appType": ReadConfig('keeperParams').conf_value('keeperParams', 'appType'),
            "versionInt": ReadConfig('keeperParams').conf_value('keeperParams', 'versionInt')
        }
        data['sign'] = commFunc.get_crm_sign(data)
        resp = self.http.http_post(url, data)
        return resp

    def add_track_by_keeper(self):
        """
        POST http://s.t.ziroom.com/crm-reserve/busopp/addTrackByKeeper HTTP/1.1
        :return:
        """
        url = '/busopp/addTrackByKeeper'
        data = {
            "uuid": globalParams.get_value('app_id') + commFunc.timestamp_13(),
            "cityCode": ReadConfig('keeperParams').conf_value('keeperParams', 'cityCode'),
            "keeperCode": globalParams.get_value('login_uid'),
            "keeperName": globalParams.get_value('agent_name'),
            "timestamp": commFunc.timestamp_13(),
            "appId": globalParams.get_value('app_id'),
            "versionInt": ReadConfig('keeperParams').conf_value('keeperParams', 'versionInt'),
            "trackTime": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
            "busOppId": globalParams.get_value('busopp_id'),
            "price": ReadConfig('keeperParams').conf_value('keeperParams', 'price'),
            "source": ReadConfig('keeperParams').conf_value('keeperParams', 'source'),
            "imei": ReadConfig('keeperParams').conf_value('keeperParams', 'imei'),
            "appType": ReadConfig('keeperParams').conf_value('keeperParams', 'appType'),
            "osType": ReadConfig('keeperParams').conf_value('keeperParams', 'osType'),
            "keeperId": globalParams.get_value('login_uid'),
            "remark": ReadConfig('keeperParams').conf_value('keeperParams', 'remark'),
            "trackResult": ReadConfig('keeperParams').conf_value('keeperParams', 'trackResult')
        }
        data['sign'] = commFunc.get_crm_sign(data)
        resp = self.http.http_post(url, data)
        return resp

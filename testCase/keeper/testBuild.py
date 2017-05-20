#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Date    : 2017/4/24 18:10
# @Version : python 3.4
# @Author  : KingDow
from common import commFunc
from common import globalParams
from common.httpConfig import GetHttp
from common.logConfig import GetLog
from testCase.keeper.keeperParams.keeperParms import KeeperParams


class BuildInfo(object):
    def __init__(self):
        self.log = GetLog().log()
        self.http = GetHttp('crm_domain').get_http()

    def test_get_build_num_list(self):
        """
        获取楼盘列表
        :return:
        """
        url = '/house/getBuildNumList'
        data = {'source': KeeperParams().source,
                'uuid': KeeperParams().app_id() + commFunc.timestamp_13(),
                'timestamp': commFunc.timestamp_13(),
                'appId': globalParams.get_value('app_id'),
                'cityCode': KeeperParams().cityCode,
                'resblockId': KeeperParams().resblockId,
                'keeperId': globalParams.get_value('login_uid'),
                'districtId': KeeperParams().districtId,
                'appType': KeeperParams().appType,
                'keeperCode': globalParams.get_value('login_uid'),
                'osType': KeeperParams().osType,
                'imei': KeeperParams().imei,
                'versionInt': KeeperParams().versionInt
                }
        data['sign'] = commFunc.get_crm_sign(data)
        r = self.http.http_post(url, data)
        return r

    def test_get_unit_list(self):
        """
        获取楼栋单元下拉列表枚举值
        :return:
        """
        url = '/house/getUnitList'
        data = {'source': '1',
                'uuid': KeeperParams().app_id() + commFunc.timestamp_13(),
                'timestamp': commFunc.timestamp_13(),
                'appId': globalParams.get_value('app_id'),
                'cityCode': KeeperParams().cityCode,
                'resblockId': KeeperParams().resblockId,
                'keeperId': globalParams.get_value('login_uid'),
                'districtId': KeeperParams().districtId,
                'appType': KeeperParams().appType,
                'keeperCode': globalParams.get_value('login_uid'),
                'osType': KeeperParams().osType,
                'imei': KeeperParams().imei,
                'versionInt': KeeperParams().versionInt,
                'buildingNo': KeeperParams().buildingNo
                }
        data['sign'] = commFunc.get_crm_sign(data)
        r = self.http.http_post(url, data)
        return r

    def test_get_floor_list(self):
        """
        获取楼栋单元楼层下拉列表枚举值
        :return:
        """
        url = '/house/getFloorList'
        data = {'source': KeeperParams().source,
                'uuid': KeeperParams().app_id() + commFunc.timestamp_13(),
                'timestamp': commFunc.timestamp_13(),
                'appId': globalParams.get_value('app_id'),
                'cityCode': KeeperParams().cityCode,
                'resblockId': KeeperParams().resblockId,
                'keeperId': globalParams.get_value('login_uid'),
                'districtId': KeeperParams().districtId,
                'appType': KeeperParams().appType,
                'keeperCode': globalParams.get_value('login_uid'),
                'osType': KeeperParams().osType,
                'imei': KeeperParams().imei,
                'versionInt': KeeperParams().versionInt,
                'unit': KeeperParams().unit,
                'buildingNo': KeeperParams().buildingNo
                }
        data['sign'] = commFunc.get_crm_sign(data)
        r = self.http.http_post(url, data)
        return r

    def test_get_room_num_list(self):
        """
        获取房间下拉列表枚举值
        :return:
        """
        url = '/house/getRoomNumList'
        data = {'source': KeeperParams().source,
                'uuid': KeeperParams().app_id() + commFunc.timestamp_13(),
                'timestamp': commFunc.timestamp_13(),
                'appId': globalParams.get_value('app_id'),
                'cityCode': KeeperParams().cityCode,
                'resblockId': KeeperParams().resblockId,
                'keeperId': globalParams.get_value('login_uid'),
                'districtId': KeeperParams().districtId,
                'appType': KeeperParams().appType,
                'keeperCode': globalParams.get_value('login_uid'),
                'osType': KeeperParams().osType,
                'imei': KeeperParams().imei,
                'versionInt': KeeperParams().versionInt,
                'unit': KeeperParams().unit,
                'floor': KeeperParams().floor,
                'buildingNo': KeeperParams().buildingNo
                }
        data['sign'] = commFunc.get_crm_sign(data)
        r = self.http.http_post(url, data)
        return r

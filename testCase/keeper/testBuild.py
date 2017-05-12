#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Date    : 2017/4/24 18:10
# @Version : python 3.4
# @Author  : KingDow
from common import commFunc
from common.httpConfig import GetHttp
from common.logConfig import GetLog
from testCase.keeper.keeperParams.keeperParms import KeeperParams


class BuildInfo(object):
    def __init__(self):
        self.log = GetLog().log()
        self.http = GetHttp().get_http()

    def test_get_build_num_list(self):
        """
        获取楼盘列表
        :return:
        """
        url = '/house/getBuildNumList'
        data = {'source': KeeperParams().source,
                'uuid': KeeperParams().app_id() + commFunc.timestamp_13(),
                'timestamp': commFunc.timestamp_13(),
                'appId': KeeperParams().app_id(),
                'cityCode': KeeperParams().cityCode,
                'resblockId': KeeperParams().resblockId,
                'keeperId': KeeperParams().user_account,
                'districtId': KeeperParams().districtId,
                'appType': KeeperParams().appType,
                'keeperCode': KeeperParams().user_account,
                'osType': KeeperParams().osType,
                'imei': KeeperParams().imei,
                'versionInt': KeeperParams().versionInt
                }
        data['sign'] = commFunc.get_crm_sign(data)
        r = self.http.http_post(url, data)
        self.log.info('接口出参为: %s' % r.json())
        return r.json()

    def test_get_unit_list(self):
        """
        获取楼栋单元下拉列表枚举值
        :return:
        """
        url = '/house/getUnitList'
        data = {'sign': 'a92b209ecc21ad7472f5b8b3c355ad9b',
                'source': '1',
                'uuid': '10217570121493029018519',
                'timestamp': '1493029018519',
                'appId': '1021757012',
                'cityCode': '110000',
                'resblockId': '1111027374425',
                'keeperId': '20189548',
                'districtId': '23008613',
                'appType': '1',
                'keeperCode': '20189548',
                'osType': '2',
                'imei': '354782061807702',
                'versionInt': '20403',
                'buildingNo': '14%E5%8F%B7%E6%A5%BC'
                }
        r = self.http.http_post(url, data)
        return r.json()

    def test_get_floor_list(self):
        """
        获取楼栋单元楼层下拉列表枚举值
        :return:
        """
        url = '/house/getFloorList'
        data = {'sign': 'faaadd356049d942a933614cd2f50d6b',
                'source': '1',
                'uuid': '10217570121493029062055',
                'timestamp': '1493029062055',
                'appId': '1021757012',
                'cityCode': '110000',
                'resblockId': '1111027374425',
                'keeperId': '20189548',
                'districtId': '23008613',
                'appType': '1',
                'keeperCode': '20189548',
                'osType': '2',
                'imei': '354782061807702',
                'versionInt': '20403',
                'unit': '2%E5%8D%95%E5%85%83',
                'buildingNo': '14%E5%8F%B7%E6%A5%BC'
                }
        r = self.http.http_post(url, data)
        return r.json()

    def test_get_room_num_list(self):
        """
        获取房间下拉列表枚举值
        :return:
        """
        url = '/house/getRoomNumList'
        data = {'sign': 'e30cdc899e88a47347151a4a57fe2bc8',
                'source': '1',
                'uuid': '10217570121493029100092',
                'timestamp': '1493029100092',
                'appId': '1021757012',
                'cityCode': '110000',
                'resblockId': '1111027374425',
                'keeperId': '20189548',
                'districtId': '23008613',
                'appType': '1',
                'keeperCode': '20189548',
                'osType': '2',
                'imei': '354782061807702',
                'versionInt': '20403',
                'unit': '2%E5%8D%95%E5%85%83',
                'floor': '3',
                'buildingNo': '14%E5%8F%B7%E6%A5%BC'
                }
        r = self.http.http_post(url, data)
        return r.json()
a = BuildInfo()
a.test_get_build_num_list()

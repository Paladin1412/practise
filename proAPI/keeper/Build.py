#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Date    : 2017/4/24 18:10
# @Version : python 3.4
# @Author  : KingDow
import random
from common import commFunc
from common import globalParams
from common.httpConfig import GetHttp
from common.logConfig import GetLog
from common.readConfig import ReadConfig


class BuildInfo(object):
    def __init__(self):
        self.log = GetLog().log()
        self.http = GetHttp('crm_domain').get_http()

    def get_district_list(self):
        """
        管家登陆成功首页获取城市区域列表
        :return:{'districtName': '通州', 'districtId': '23008625'}, {'districtName': '房山', 'districtId': '23008616'},
        {'districtName': '昌平', 'districtId': '23008611'}, {'districtName': '门头沟', 'districtId': '23008620'},
        {'districtName': '丰台', 'districtId': '23008617'}, {'districtName': '亦庄开发区', 'districtId': '23008629'},
        {'districtName': '海淀', 'districtId': '23008618'}, {'districtName': '东城', 'districtId': '23008614'},
        {'districtName': '西城', 'districtId': '23008626'}, {'districtName': '顺义', 'districtId': '23008624'},
        {'districtName': '朝阳', 'districtId': '23008613'}, {'districtName': '大兴', 'districtId': '23008615'},
        {'districtName': '平谷', 'districtId': '23008622'}, {'districtName': '密云', 'districtId': '23008621'},
        {'districtName': '怀柔', 'districtId': '23008619'}, {'districtName': '石景山', 'districtId': '23008623'},
        {'districtName': '延庆', 'districtId': '23008628'}
        """
        url = '/house/getDistrictList'
        data = {'appType': ReadConfig('keeperParams').conf_value('keeperParams', 'appType'),
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

        # district_list = resp.get('data')
        # if district_list:
        #     for i in resp.get('data'):
        #         if i.get('districtName') == '朝阳':
        #             district = i.get('districtId')
        #             globalParams.set_value('districtId', district)
        return resp

    def get_village_list(self):
        url = '/house/getVillageList'
        data = {'source': ReadConfig('keeperParams').conf_value('keeperParams', 'source'),
                'uuid': globalParams.get_value('app_id') + commFunc.timestamp_13(),
                'timestamp': commFunc.timestamp_13(),
                'resblock': ReadConfig('keeperParams').conf_value('keeperParams', 'resblock'),
                'appId': globalParams.get_value('app_id'),
                'cityCode': ReadConfig('keeperParams').conf_value('keeperParams', 'cityCode'),
                'keeperId': globalParams.get_value('login_uid'),
                'districtId': ReadConfig('keeperParams').conf_value('keeperParams', 'districtId'),
                'appType': ReadConfig('keeperParams').conf_value('keeperParams', 'appType'),
                'keeperCode': globalParams.get_value('login_uid'),
                'osType': ReadConfig('keeperParams').conf_value('keeperParams', 'osType'),
                'imei': ReadConfig('keeperParams').conf_value('keeperParams', 'imei'),
                'versionInt': ReadConfig('keeperParams').conf_value('keeperParams', 'versionInt')
                }
        data['sign'] = commFunc.get_crm_sign(data)
        resp = self.http.http_post(url, data)

        resblock_list = resp.get('data')
        if resblock_list:
            resblock_id = resblock_list[random.randint(0, len(resblock_list) - 1)].get('resblock_id')
            resblock_name = resblock_list[random.randint(0, len(resblock_list) - 1)].get('resblock_name')
            globalParams.set_value('resblock_id', resblock_id)
            globalParams.set_value('resblock_name', resblock_name)
        else:
            self.log.warning('根据楼盘关键字查询楼盘名称楼盘id有误，接口返回值：' + resp)
        return resp

    #

    def get_build_num_list(self):
        """
        获取楼栋列表
        :return:
        """
        url = '/house/getBuildNumList'
        data = {'source': ReadConfig('keeperParams').conf_value('keeperParams', 'source'),
                'uuid': globalParams.get_value('app_id') + commFunc.timestamp_13(),
                'timestamp': commFunc.timestamp_13(),
                'appId': globalParams.get_value('app_id'),
                'cityCode': ReadConfig('keeperParams').conf_value('keeperParams', 'cityCode'),
                'resblockId': globalParams.get_value('resblock_id'),
                'keeperId': globalParams.get_value('login_uid'),
                'districtId': ReadConfig('keeperParams').conf_value('keeperParams', 'districtId'),
                'appType': ReadConfig('keeperParams').conf_value('keeperParams', 'appType'),
                'keeperCode': globalParams.get_value('login_uid'),
                'osType': ReadConfig('keeperParams').conf_value('keeperParams', 'osType'),
                'imei': ReadConfig('keeperParams').conf_value('keeperParams', 'imei'),
                'versionInt': ReadConfig('keeperParams').conf_value('keeperParams', 'versionInt')
                }
        data['sign'] = commFunc.get_crm_sign(data)
        resp = self.http.http_post(url, data)

        build_num_list = resp.get('data')
        if build_num_list:
            build_num = build_num_list[random.randint(0, len(build_num_list) - 1)].get('building_no')
            globalParams.set_value('buildingNo', build_num)
        else:
            self.log.warning('获取楼栋列表为空，接口返回值：' + resp)
        return resp

    def get_unit_list(self):
        """
        获取单元列表
        :return:
        """
        url = '/house/getUnitList'
        data = {'source': '1',
                'uuid': globalParams.get_value('app_id') + commFunc.timestamp_13(),
                'timestamp': commFunc.timestamp_13(),
                'appId': globalParams.get_value('app_id'),
                'cityCode': ReadConfig('keeperParams').conf_value('keeperParams', 'cityCode'),
                'resblockId': globalParams.get_value('resblock_id'),
                'keeperId': globalParams.get_value('login_uid'),
                'districtId': ReadConfig('keeperParams').conf_value('keeperParams', 'districtId'),
                'appType': ReadConfig('keeperParams').conf_value('keeperParams', 'appType'),
                'keeperCode': globalParams.get_value('login_uid'),
                'osType': ReadConfig('keeperParams').conf_value('keeperParams', 'osType'),
                'imei': ReadConfig('keeperParams').conf_value('keeperParams', 'imei'),
                'versionInt': ReadConfig('keeperParams').conf_value('keeperParams', 'versionInt'),
                'buildingNo': globalParams.get_value('buildingNo')
                }
        data['sign'] = commFunc.get_crm_sign(data)
        resp = self.http.http_post(url, data)

        unit_list = resp.get('data')
        if unit_list:
            unit = unit_list[random.randint(0, len(unit_list) - 1)].get('unit')
            globalParams.set_value('unit', unit)
        else:
            self.log.warning('获取单元列表为空，接口返回值：' + resp)
        return resp

    def get_floor_list(self):
        """
        获取楼栋单元楼层下拉列表枚举值
        :return:
        """
        url = '/house/getFloorList'
        data = {'source': ReadConfig('keeperParams').conf_value('keeperParams', 'source'),
                'uuid': globalParams.get_value('app_id') + commFunc.timestamp_13(),
                'timestamp': commFunc.timestamp_13(),
                'appId': globalParams.get_value('app_id'),
                'cityCode': ReadConfig('keeperParams').conf_value('keeperParams', 'cityCode'),
                'resblockId': globalParams.get_value('resblock_id'),
                'keeperId': globalParams.get_value('login_uid'),
                'districtId': ReadConfig('keeperParams').conf_value('keeperParams', 'districtId'),
                'appType': ReadConfig('keeperParams').conf_value('keeperParams', 'appType'),
                'keeperCode': globalParams.get_value('login_uid'),
                'osType': ReadConfig('keeperParams').conf_value('keeperParams', 'osType'),
                'imei': ReadConfig('keeperParams').conf_value('keeperParams', 'imei'),
                'versionInt': ReadConfig('keeperParams').conf_value('keeperParams', 'versionInt'),
                'unit': globalParams.get_value('unit'),
                'buildingNo': globalParams.get_value('buildingNo')
                }
        data['sign'] = commFunc.get_crm_sign(data)
        resp = self.http.http_post(url, data)

        floor_list = resp.get('data')
        if floor_list:
            floor = floor_list[random.randint(0, len(floor_list) - 1)].get('floor')
            globalParams.set_value('floor', floor)
        else:
            self.log.warning('获取楼层列表为空，接口返回值：' + resp)
        return resp

    def get_room_num_list(self):
        """
        获取房间下拉列表枚举值
        :return:
        """
        url = '/house/getRoomNumList'
        data = {'source': ReadConfig('keeperParams').conf_value('keeperParams', 'source'),
                'uuid': globalParams.get_value('app_id') + commFunc.timestamp_13(),
                'timestamp': commFunc.timestamp_13(),
                'appId': globalParams.get_value('app_id'),
                'cityCode': ReadConfig('keeperParams').conf_value('keeperParams', 'cityCode'),
                'resblockId': globalParams.get_value('resblock_id'),
                'keeperId': globalParams.get_value('login_uid'),
                'districtId': ReadConfig('keeperParams').conf_value('keeperParams', 'districtId'),
                'appType': ReadConfig('keeperParams').conf_value('keeperParams', 'appType'),
                'keeperCode': globalParams.get_value('login_uid'),
                'osType': ReadConfig('keeperParams').conf_value('keeperParams', 'osType'),
                'imei': ReadConfig('keeperParams').conf_value('keeperParams', 'imei'),
                'versionInt': ReadConfig('keeperParams').conf_value('keeperParams', 'versionInt'),
                'unit': globalParams.get_value('unit'),
                'floor': globalParams.get_value('floor'),
                'buildingNo': globalParams.get_value('buildingNo')
                }
        data['sign'] = commFunc.get_crm_sign(data)
        resp = self.http.http_post(url, data)

        room_no_list = resp.get('data')
        if room_no_list:
            room_no = room_no_list[random.randint(0, len(room_no_list) - 1)].get('room_no')
            globalParams.set_value('room_no', room_no)
        else:
            self.log.warning('获取房间列表为空，接口返回值：' + resp)
        return resp

#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Date    : 2017/4/24 16:37
# @Version : python 3.4
# @Author  : KingDow
import time

from common import commFunc
from common import globalParams
from common.httpConfig import GetHttp
from common.logConfig import GetLog
from testCase.keeper.keeperParams.keeperParms import KeeperParams


class KeeperLogin(object):
    def __init__(self):
        self.http = GetHttp('crm_domain').get_http()
        self.log = GetLog().log()

    def test_get_latest_version(self):
        """
        启动管家APP时获取最新版本号
        :return:
        """
        url = '/common/getLatestVersion'
        data = {'source': KeeperParams().source,
                'appType': KeeperParams().appType,
                'keeperCode': globalParams.get_value('login_uid'),
                'imei': KeeperParams().imei,
                'osType': KeeperParams().osType,
                'versionInt': KeeperParams().versionInt,
                'uuid': KeeperParams().app_id() + commFunc.timestamp_13(),
                'timestamp': commFunc.timestamp_13(),
                'appId': globalParams.get_value('app_id'),
                'cityCode': KeeperParams().cityCode
                }
        data['sign'] = commFunc.get_crm_sign(data)
        resp = self.http.http_post(url, data)
        return resp

    def test_get_district_list(self):
        """
        管家登陆成功首页获取城市区域列表
        :return:
        """
        url = '/house/getDistrictList'
        data = {'appType': KeeperParams().appType,
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

    def test_get_home_page_module(self):
        """
        获取首页管家功能模块
        :return:
        """
        url = '/orderUser/getHomePageModule'
        data = {'keeperId': globalParams.get_value('login_uid'),
                'appType': KeeperParams().appType,
                'source': KeeperParams().source,
                'keeperCode': globalParams.get_value('login_uid'),
                'osType': KeeperParams().osType,
                'imei': KeeperParams().imei,
                'versionInt': KeeperParams().versionInt,
                'roleCode': '1',
                'uuid': KeeperParams().app_id() + commFunc.timestamp_13(),
                'timestamp': commFunc.timestamp_13(),
                'appId': globalParams.get_value('app_id'),
                'cityCode': KeeperParams().cityCode
                }
        data['sign'] = commFunc.get_crm_sign(data)
        resp = self.http.http_post(url, data)
        return resp

    def test_get_schedule_by_keeperid_and_condition(self):
        url = '/orderUser/getScheduleByKeeperIdAndCondition'
        data = {'source': KeeperParams().source,
                'uuid': KeeperParams().app_id() + commFunc.timestamp_13(),
                'timestamp': commFunc.timestamp_13(),
                'appId': globalParams.get_value('app_id'),
                'cityCode': KeeperParams().cityCode,
                'keeperId': globalParams.get_value('login_uid'),
                'appType': KeeperParams().appType,
                'keeperCode': globalParams.get_value('login_uid'),
                'osType': KeeperParams().osType,
                'imei': KeeperParams().imei,
                'searchTitle': '',
                'versionInt': KeeperParams().versionInt,
                'searchDate': time.strftime("%Y-%m-%d")
                }
        data['sign'] = commFunc.get_crm_sign(data)
        resp = self.http.http_post(url, data)
        return resp

    def test_get_app_be_evaluate(self):
        """
        获取管家平均分积分
        :return:
        """
        url = '/hkApp/getAppBeEvaluate'
        data = {'appType': KeeperParams().appType,
                'source': KeeperParams().source,
                'keeperCode': globalParams.get_value('login_uid'),
                'osType': KeeperParams().osType,
                'imei': KeeperParams().imei,
                'versionInt': KeeperParams().versionInt,
                'uuid': KeeperParams().app_id() + commFunc.timestamp_13(),
                'timestamp': commFunc.timestamp_13(),
                'uid': globalParams.get_value('login_uid'),
                'appId': globalParams.get_value('app_id'),
                'cityCode': KeeperParams().cityCode
                }
        data['sign'] = commFunc.get_crm_sign(data)
        resp = self.http.http_post(url, data)
        return resp

    def test_get_target_info(self):
        """
        调用资产系统获取目标看板
        :return:
        """
        url = '/hkApp/getTargetInfo'
        data = {'appType': KeeperParams().appType,
                'source': KeeperParams().source,
                'keeperCode': globalParams.get_value('login_uid'),
                'osType': KeeperParams().osType,
                'imei': KeeperParams().imei,
                'versionInt': KeeperParams().versionInt,
                'uuid': KeeperParams().app_id() + commFunc.timestamp_13(),
                'userAccount': globalParams.get_value('login_uid'),
                'timestamp': commFunc.timestamp_13(),
                'appId': globalParams.get_value('app_id'),
                'cityCode': KeeperParams().cityCode
                }
        data['sign'] = commFunc.get_crm_sign(data)
        resp = self.http.http_post(url, data)
        return resp

    def test_get_all_module(self):
        """
        根据管家类型获取功能池列表
        :return:
        """
        url = '/orderUser/getAllModule'
        data = {'appType': KeeperParams().appType,
                'source': KeeperParams().source,
                'keeperCode': globalParams.get_value('login_uid'),
                'osType': KeeperParams().osType,
                'imei': KeeperParams().imei,
                'versionInt': KeeperParams().versionInt,
                'roleCode': '1',
                'uuid': KeeperParams().app_id() + commFunc.timestamp_13(),
                'timestamp': commFunc.timestamp_13(),
                'appId': globalParams.get_value('app_id'),
                'cityCode': KeeperParams().cityCode
                }
        data['sign'] = commFunc.get_crm_sign(data)
        resp = self.http.http_post(url, data)
        return resp

    def test_get_message_list(self):
        url = '/messageCenter/getMessageList'
        data = {'appType': KeeperParams().appType,
                'source': KeeperParams().source,
                'businessType': '1',
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

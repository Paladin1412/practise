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
from common.readConfig import ReadConfig


class KeeperLogin(object):
    def __init__(self):
        self.http = GetHttp('crm_domain').get_http()
        self.log = GetLog().log()

    def get_latest_version(self):
        """
        启动管家APP时获取最新版本号
        :return:
        """
        url = '/common/getLatestVersion'
        data = {'source': ReadConfig('keeperParams').conf_value('keeperParams', 'source'),
                'appType': ReadConfig('keeperParams').conf_value('keeperParams', 'appType'),
                'keeperCode': globalParams.get_value('login_uid'),
                'imei': ReadConfig('keeperParams').conf_value('keeperParams', 'imei'),
                'osType': ReadConfig('keeperParams').conf_value('keeperParams', 'osType'),
                'versionInt': ReadConfig('keeperParams').conf_value('keeperParams', 'versionInt'),
                'uuid': globalParams.get_value('app_id') + commFunc.timestamp_13(),
                'timestamp': commFunc.timestamp_13(),
                'appId': globalParams.get_value('app_id'),
                'cityCode': ReadConfig('keeperParams').conf_value('keeperParams', 'cityCode')
                }
        data['sign'] = commFunc.get_crm_sign(data)
        resp = self.http.http_post(url, data)
        return resp

    def get_home_page_module(self):
        """
        获取首页管家功能模块
        :return:
        """
        url = '/orderUser/getHomePageModule'
        data = {'keeperId': globalParams.get_value('login_uid'),
                'appType': ReadConfig('keeperParams').conf_value('keeperParams', 'appType'),
                'source': ReadConfig('keeperParams').conf_value('keeperParams', 'source'),
                'keeperCode': globalParams.get_value('login_uid'),
                'osType': ReadConfig('keeperParams').conf_value('keeperParams', 'osType'),
                'imei': ReadConfig('keeperParams').conf_value('keeperParams', 'imei'),
                'versionInt': ReadConfig('keeperParams').conf_value('keeperParams', 'versionInt'),
                'roleCode': '1',
                'uuid': globalParams.get_value('app_id') + commFunc.timestamp_13(),
                'timestamp': commFunc.timestamp_13(),
                'appId': globalParams.get_value('app_id'),
                'cityCode': ReadConfig('keeperParams').conf_value('keeperParams', 'cityCode')
                }
        data['sign'] = commFunc.get_crm_sign(data)
        resp = self.http.http_post(url, data)
        return resp

    def get_schedule_by_keeperid_and_condition(self):
        url = '/orderUser/getScheduleByKeeperIdAndCondition'
        data = {'source': ReadConfig('keeperParams').conf_value('keeperParams', 'source'),
                'uuid': globalParams.get_value('app_id') + commFunc.timestamp_13(),
                'timestamp': commFunc.timestamp_13(),
                'appId': globalParams.get_value('app_id'),
                'cityCode': ReadConfig('keeperParams').conf_value('keeperParams', 'cityCode'),
                'keeperId': globalParams.get_value('login_uid'),
                'appType': ReadConfig('keeperParams').conf_value('keeperParams', 'appType'),
                'keeperCode': globalParams.get_value('login_uid'),
                'osType': ReadConfig('keeperParams').conf_value('keeperParams', 'osType'),
                'imei': ReadConfig('keeperParams').conf_value('keeperParams', 'imei'),
                'searchTitle': '',
                'versionInt': ReadConfig('keeperParams').conf_value('keeperParams', 'versionInt'),
                'searchDate': time.strftime("%Y-%m-%d")
                }
        data['sign'] = commFunc.get_crm_sign(data)
        resp = self.http.http_post(url, data)
        return resp

    def get_app_be_evaluate(self):
        """
        获取管家平均分积分
        :return:
        """
        url = '/hkApp/getAppBeEvaluate'
        data = {'appType': ReadConfig('keeperParams').conf_value('keeperParams', 'appType'),
                'source': ReadConfig('keeperParams').conf_value('keeperParams', 'source'),
                'keeperCode': globalParams.get_value('login_uid'),
                'osType': ReadConfig('keeperParams').conf_value('keeperParams', 'osType'),
                'imei': ReadConfig('keeperParams').conf_value('keeperParams', 'imei'),
                'versionInt': ReadConfig('keeperParams').conf_value('keeperParams', 'versionInt'),
                'uuid': globalParams.get_value('app_id') + commFunc.timestamp_13(),
                'timestamp': commFunc.timestamp_13(),
                'uid': globalParams.get_value('login_uid'),
                'appId': globalParams.get_value('app_id'),
                'cityCode': ReadConfig('keeperParams').conf_value('keeperParams', 'cityCode')
                }
        data['sign'] = commFunc.get_crm_sign(data)
        resp = self.http.http_post(url, data)
        return resp

    def get_target_info(self):
        """
        调用资产系统获取目标看板
        :return:
        """
        url = '/hkApp/getTargetInfo'
        data = {'appType': ReadConfig('keeperParams').conf_value('keeperParams', 'appType'),
                'source': ReadConfig('keeperParams').conf_value('keeperParams', 'source'),
                'keeperCode': globalParams.get_value('login_uid'),
                'osType': ReadConfig('keeperParams').conf_value('keeperParams', 'osType'),
                'imei': ReadConfig('keeperParams').conf_value('keeperParams', 'imei'),
                'versionInt': ReadConfig('keeperParams').conf_value('keeperParams', 'versionInt'),
                'uuid': globalParams.get_value('app_id') + commFunc.timestamp_13(),
                'userAccount': globalParams.get_value('login_uid'),
                'timestamp': commFunc.timestamp_13(),
                'appId': globalParams.get_value('app_id'),
                'cityCode': ReadConfig('keeperParams').conf_value('keeperParams', 'cityCode')
                }
        data['sign'] = commFunc.get_crm_sign(data)
        resp = self.http.http_post(url, data)
        return resp

    def get_all_module(self):
        """
        根据管家类型获取功能池列表
        :return:
        """
        url = '/orderUser/getAllModule'
        data = {'appType': ReadConfig('keeperParams').conf_value('keeperParams', 'appType'),
                'source': ReadConfig('keeperParams').conf_value('keeperParams', 'source'),
                'keeperCode': globalParams.get_value('login_uid'),
                'osType': ReadConfig('keeperParams').conf_value('keeperParams', 'osType'),
                'imei': ReadConfig('keeperParams').conf_value('keeperParams', 'imei'),
                'versionInt': ReadConfig('keeperParams').conf_value('keeperParams', 'versionInt'),
                'roleCode': '1',
                'uuid': globalParams.get_value('app_id') + commFunc.timestamp_13(),
                'timestamp': commFunc.timestamp_13(),
                'appId': globalParams.get_value('app_id'),
                'cityCode': ReadConfig('keeperParams').conf_value('keeperParams', 'cityCode')
                }
        data['sign'] = commFunc.get_crm_sign(data)
        resp = self.http.http_post(url, data)
        return resp

    def get_message_list(self):
        url = '/messageCenter/getMessageList'
        data = {'appType': ReadConfig('keeperParams').conf_value('keeperParams', 'appType'),
                'source': ReadConfig('keeperParams').conf_value('keeperParams', 'source'),
                'businessType': '1',
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

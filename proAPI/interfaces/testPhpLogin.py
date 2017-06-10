#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Date    : 2017/4/24 16:46
# @Version : python 3.4
# @Author  : KingDow
from common import commFunc
from common import globalParams
from common.httpConfig import GetHttp
from common.logConfig import GetLog
from common.readConfig import ReadConfig


class PhpLogin(object):
    def __init__(self):
        self.http = GetHttp('interfaces_domain').get_http()
        self.log = GetLog().log()

    def php_login_normal(self, login_name, password):
        """
        管家app登录api
        :param login_name
        :param password
        :return:
        """
        url = '/index.php?_p=api_mobile&_a=login_normal'
        data = {'user_account': login_name,
                'password': password,
                'sign': commFunc.get_app_sign(login_name, commFunc.timestamp_10()),
                'appType': ReadConfig(conf_path='keeperParanmsPath').conf_value('LOGIN', 'appType'),
                'timestamp': commFunc.timestamp_10(),
                'companyFlag': ReadConfig(conf_path='keeperParanmsPath').conf_value('LOGIN', 'companyFlag'),
                'uid': login_name,
                'login_name': login_name
                }
        resp = self.http.http_post(url, data)

        if resp.get('data'):
            globalParams.set_value('login_uid', resp.get('data').get('uid'))
        return resp

    def php_statistical_information_quantity(self):
        url = '/?_p=api_newsign&_a=statistical_information_quantity'
        data = {'timestamp': commFunc.timestamp_10(),
                'user_account': globalParams.get_value('login_uid'),
                'sign': commFunc.get_app_sign(globalParams.get_value('login_uid'), commFunc.timestamp_10()),
                'get_num': 0,
                'send_num': 0
                }
        resp = self.http.http_post(url, data)
        return resp

    def php_steward_information(self):
        """
        获取管家类型业务组手机号信息
        :return:
        """
        url = '/index.php?_p=api_mobile&_a=stewardInformation'
        data = {'user_account': globalParams.get_value('login_uid'),
                'timestamp': commFunc.timestamp_10(),
                'companyFlag': ReadConfig(conf_path='keeperParanmsPath').conf_value('LOGIN', 'companyFlag'),
                'sign': commFunc.get_app_sign(globalParams.get_value('login_uid'), commFunc.timestamp_10())
                }
        resp = self.http.http_post(url, data)
        return resp

    def php_get_announcement_list(self):
        url = '/?_p=api_mobile&_a=getAnnouncementList'
        data = {'user_account': globalParams.get_value('login_uid'),
                'timestamp': commFunc.timestamp_10(),
                'uid': globalParams.get_value('login_uid'),
                'sign': commFunc.get_app_sign(globalParams.get_value('login_uid'), commFunc.timestamp_10())
                }
        resp = self.http.http_post(url, data)
        return resp

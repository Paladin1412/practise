#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Date    : 2017/4/24 16:46
# @Version : python 3.4
# @Author  : KingDow
from common import commFunc
from common.httpConfig import GetHttp
from common.logConfig import GetLog
from testCase.keeper.keeperParams.keeperParms import KeeperParams


class PhpLogin(object):
    def __init__(self):
        self.http = GetHttp().get_http()
        self.log = GetLog().log()

    def test_php_login_normal(self):
        url = '/index.php?_p=api_mobile&_a=login_normal'
        data = {'user_account': KeeperParams().login_name,
                'password': KeeperParams().password,
                'sign': commFunc.get_app_sign(KeeperParams().login_name, commFunc.timestamp_10()),
                'appType': KeeperParams().appType,
                'timestamp': commFunc.timestamp_10(),
                'companyFlag': KeeperParams().companyFlag,
                'uid': KeeperParams().login_name,
                'login_name': KeeperParams().login_name
                }
        r = self.http.http_post(url, data)
        self.log.info('接口出参为: %s' % r.json())
        return r.json()

    def test_php_statistical_information_quantity(self):
        url = '/?_p=api_newsign&_a=statistical_information_quantity'
        data = {'timestamp': commFunc.timestamp_10(),
                'user_account': KeeperParams().user_account,
                'sign': commFunc.get_app_sign(KeeperParams().user_account, commFunc.timestamp_10()),
                'get_num': 0,
                'send_num': 0
                }
        r = self.http.http_post(url, data)
        self.log.info('接口出参为: %s' % r.json())
        return r.json()

    def test_php_steward_information(self):
        url = '/index.php?_p=api_mobile&_a=stewardInformation'
        data = {'user_account': KeeperParams().user_account,
                'timestamp': commFunc.timestamp_10(),
                'companyFlag': KeeperParams().companyFlag,
                'sign': commFunc.get_app_sign(KeeperParams().user_account, commFunc.timestamp_10())
                }
        r = self.http.http_post(url, data)
        self.log.info('接口出参为: %s' % r.json())
        return r.json()

    def test_php_get_announcement_list(self):
        url = '/?_p=api_mobile&_a=getAnnouncementList'
        data = {'user_account': KeeperParams().user_account,
                'timestamp': commFunc.timestamp_10(),
                'uid': KeeperParams().user_account,
                'sign': commFunc.get_app_sign(KeeperParams().user_account, commFunc.timestamp_10())
                }
        r = self.http.http_post(url, data)
        self.log.info('接口出参为: %s' % r.json())
        return r.json()

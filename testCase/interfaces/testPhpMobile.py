#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Date    : 2017/4/24 18:04
# @Version : python 3.4
# @Author  : KingDow
from common import commFunc
from common.httpConfig import GetHttp
from common.logConfig import GetLog
from testCase.keeper.keeperParams.keeperParms import KeeperParams


class PhpMobile(object):
    def __init__(self):
        self.log = GetLog().log()
        self.http = GetHttp().get_http()

    def test_get_is_focus_resblock(self):
        url = '/index.php?_p=api_mobile&_a=getIsFocusResblock'
        data = {'timestamp': commFunc.timestamp_10(),
                'uid': KeeperParams().user_account,
                'user_account': KeeperParams().user_account,
                'house_num': KeeperParams().house_num,
                'sign': commFunc.get_app_sign(KeeperParams().user_account, commFunc.timestamp_10())
                }
        r = self.http.http_post(url, data)
        self.log.info('接口出参为: %s' % r.json())
        return r.json()

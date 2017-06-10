#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Date    : 2017/4/24 17:52
# @Version : python 3.4
# @Author  : KingDow
from common import commFunc
from common import globalParams
from common.httpConfig import GetHttp


class BusOpp(object):
    def __init__(self):
        self.http = GetHttp('busopp_domain').get_http()

    def test_query_opp_page_info(self):
        url = '/busopp/queryOppPageInfo'
        data = {'keeperId': globalParams.get_value('login_uid'),
                'appType': KeeperParams().appType,
                'source': KeeperParams().source,
                'keeperCode': globalParams.get_value('login_uid'),
                'osType': KeeperParams().osType,
                'imei': KeeperParams().imei,
                'versionInt': KeeperParams().versionInt,
                'uuid': globalParams.get_value('app_id') + commFunc.timestamp_13(),
                'timestamp': commFunc.timestamp_13(),
                'appId': globalParams.get_value('app_id'),
                'cityCode': KeeperParams().cityCode
                }
        data['sign'] = commFunc.get_crm_sign(data)
        resp = self.http.http_post(url, data)
        return resp

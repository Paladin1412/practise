#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Date    : 2017/4/24 17:52
# @Version : python 3.4
# @Author  : KingDow
from common.httpConfig import GetHttp


class BusOpp(object):
    def __init__(self):
        self.http = GetHttp().get_http()

    def test_query_opp_page_info(self):
        url = '/busopp/queryOppPageInfo'
        data = {'keeperId': 20189548,
                'sign': 'd943d7a455dbcf05700c0bfbd902748e',
                'appType': 1,
                'source': 1,
                'keeperCode': 20189548,
                'osType': 2,
                'imei': 354782061807702,
                'versionInt': 20403,
                'uuid': 10217570121493027285474,
                'timestamp': 1493027285474,
                'appId': 1021757012,
                'cityCode': 110000
                }
        r = self.http.http_post(url, data)
        print(r.json())
        return r.json()


a = BusOpp()
a.test_query_opp_page_info()

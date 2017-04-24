#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Date    : 2017/4/24 16:37
# @Version : python 3.4
# @Author  : KingDow
from common.httpConfig import GetHttp


class KeeperLogin(object):
    def __init__(self):
        self.http = GetHttp().get_http()

    def test_get_latest_version(self):
        url = '/common/getLatestVersion'
        data = 'sign=10397f810cc6a1dbc47cc99a99f189a6&source=1&appType=1&keeperCode=&imei=354782061807702&osType=2&' \
               'versionInt=20403&uuid=10217570121493022780326&timestamp=1493022780326&appId=1021757012&cityCode=310000&'
        r = self.http.http_post(url, data)
        return r.json()

    def test_get_district_list(self):
        url = '/house/getDistrictList'
        data = 'sign=e1b1c8163d8898fa904386769e70a694&appType=1&source=1&keeperCode=20189548&osType=2&' \
               'imei=354782061807702&versionInt=20403&uuid=10217570121493023351126&' \
               'timestamp=1493023351126&appId=1021757012&cityCode=110000&'
        r = self.http.http_post(url, data)
        return r.json()

    def test_get_home_page_module(self):
        url = '/orderUser/getHomePageModule'
        data = 'keeperId=20189548&sign=d14d0a7cb142aeba09a753f6a5a23eee&appType=1&source=1&keeperCode=20189548&' \
               'osType=2&imei=354782061807702&versionInt=20403&roleCode=1&uuid=10217570121493023351255&' \
               'timestamp=1493023351255&appId=1021757012&cityCode=110000&'
        r = self.http.http_post(url, data)
        return r.json()

    def test_get_schedule_by_keeperid_and_condition(self):
        url = '/orderUser/getScheduleByKeeperIdAndCondition'
        data = 'sign=caf17999f9553ac5fcccb4a032a189d2&source=1&uuid=10217570121493023351265&timestamp=1493023351265&' \
               'appId=1021757012&cityCode=110000&keeperId=20189548&appType=1&keeperCode=20189548&osType=2&' \
               'imei=354782061807702&searchTitle=&versionInt=20403&searchDate=2017-04-24&'
        r = self.http.http_post(url, data)
        return r.json()

    def test_get_app_be_evaluate(self):
        url = '/hkApp/getAppBeEvaluate'
        data = 'sign=50b111b203b5911bf92d1b9463116185&appType=1&source=1&keeperCode=20189548&osType=2&' \
               'imei=354782061807702&versionInt=20403&uuid=10217570121493023351275&timestamp=1493023351275&' \
               'uid=20189548&appId=1021757012&cityCode=110000&'
        r = self.http.http_post(url, data)
        return r.json()

    def test_get_target_info(self):
        url = '/hkApp/getTargetInfo'
        data = 'sign=9c5060cc773c064b3368577e72fcb8ad&appType=1&source=1&keeperCode=20189548&osType=2&' \
               'imei=354782061807702&versionInt=20403&uuid=10217570121493023351276&userAccount=20189548&' \
               'timestamp=1493023351276&appId=1021757012&cityCode=110000&'
        r = self.http.http_post(url, data)
        return r.json()

    def test_get_all_module(self):
        url = '/orderUser/getAllModule'
        data = 'sign=d73d07f33b32e89b88201c8302d944ba&appType=1&source=1&keeperCode=20189548&osType=2&' \
               'imei=354782061807702&versionInt=20403&roleCode=1&uuid=10217570121493023351521&' \
               'timestamp=1493023351521&appId=1021757012&cityCode=110000&'
        r = self.http.http_post(url, data)
        return r.json()

    def test_(self):
        url = '/messageCenter/getMessageList'
        data = 'sign=0c9739c3f943298fc2edda4635ccad05&appType=1&source=1&businessType=1&keeperCode=20189548&' \
               'osType=2&imei=354782061807702&versionInt=20403&uuid=10217570121493023557336&' \
               'timestamp=1493023557336&appId=1021757012&cityCode=110000&'
        r = self.http.http_post(url, data)
        return r.json()
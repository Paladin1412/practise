#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Date    : 2017/4/24 16:46
# @Version : python 3.4
# @Author  : KingDow
from common.httpConfig import GetHttp


class PhpLogin(object):
    def __init__(self):
        self.http = GetHttp().get_http()

    def test_php_login_normal(self):
        url = '/index.php?_p=api_mobile&_a=login_normal'
        data = 'user_account=huangcx9&password=123&sign=6efb00901a443bb58d182c2fa24b096e&' \
               'appType=1&timestamp=1493023346&companyFlag=0&uid=huangcx9&login_name=huangcx9&'
        r = self.http.http_post(url, data)
        return r.json()

    def test_php_statistical(self):
        url = '/?_p=api_newsign&_a=statistical_information_quantity'
        data = 'timestamp=1493023347&user_account=20189548&sign=94e376c0668906468250b1ee56a3e4e0&get_num=0&send_num=0&'
        r = self.http.http_post(url, data)
        return r.json()

    def test_php_steward(self):
        url = '/index.php?_p=api_mobile&_a=stewardInformation'
        data = 'user_account=20189548&timestamp=1493023347&sign=94e376c0668906468250b1ee56a3e4e0&'
        r = self.http.http_post(url, data)
        return r.json()

    def test_php_get_announcement_list(self):
        url = '/?_p=api_mobile&_a=getAnnouncementList'
        data = 'user_account=20189548&timestamp=1493023553&uid=20189548&sign=c057ebfde0a2b2ff3168aa7a3218a6c0&'
        r = self.http.http_post(url, data)
        return r.json()

#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Date    : 2017/4/24 18:04
# @Version : python 3.4
# @Author  : KingDow
from common.httpConfig import GetHttp
from common.logConfig import GetLog


class PhpMobile(object):
    def __init__(self):
        self.log = GetLog().log()
        self.http = GetHttp().get_http()

    def test_get_is_focus_resblock(self):
        url = '/index.php?_p=api_mobile&_a=getIsFocusResblock'
        data = 'timestamp=1493028151&uid=20189548&user_account=20189548&' \
               'house_num=1111027374425&sign=df43e3a725a8cd700f8f383ed9ac296c&'
        r = self.http.http_post(url, data)
        return r.json()

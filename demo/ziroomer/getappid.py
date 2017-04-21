#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Date    : 2017/3/27 13:55
# @Version : python 3.4
# @Author  : KingDow
from httpconfig import GetHttp
from logconfig import GetLog


class CommonApiParas(object):
    def __init__(self):
        gh = GetHttp()
        gl = GetLog()
        self.http = gh.get_http()
        self.log = gl.log()

    def get_appid(self):
        appid_url = "/crm-reserve/common/createAppId?appType=2&imei=352248061569009"
        res_json = self.http.http_get(appid_url).json()
        if res_json:
            app_id = res_json.get("data").get("appId")
            if not app_id:
                self.log.info("变量AppId值为空")
            else:
                self.log.debug("变量AppId:" + app_id)
                return app_id
        else:
            self.log.error("createAppId----------->>>>>>>>>>为空")

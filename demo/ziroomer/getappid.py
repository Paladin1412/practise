#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Date    : 2017/3/27 13:55
# @Version : python 3.4
# @Author  : KingDow
from globalparams import GlobalParams


class CommonApiParas(object):
    def __init__(self):
        self.log = GlobalParams().log(__name__)
        self.req = GlobalParams().get_http()

    def get_appid(self):
        domain_name = GlobalParams().crm_domain
        appid_url = domain_name + "/common/createAppId?appType=2&imei=352248061569009"
        res_json = self.req.http_get(appid_url).json()
        if res_json:
            app_id = res_json.getString("data").get("appId")
            if not app_id:
                self.log.info("变量getAppid值为空")
            else:
                self.log.debug("变量appid:" + app_id)
                return app_id
        else:
            self.log.info("getAppid服务器返回值----------->>>>>>>>>>为空")

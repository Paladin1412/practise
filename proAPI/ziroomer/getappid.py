#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Date    : 2017/3/27 13:55
# @Version : python 3.4
# @Author  : KingDow
from common import globalParams
from common.httpConfig import GetHttp
from common.logConfig import GetLog


class CommonApiParas(object):
    def __init__(self):
        self.http = GetHttp('crm_domain').get_http()
        self.log = GetLog().log()

    def get_appid(self):
        url = "/common/createAppId?appType=1&imei=352248061569009"
        try:
            res_json = self.http.http_get(url)
            if res_json:
                app_id = res_json.get("data").get("appId")
                if not app_id:
                    self.log.info("变量AppId值为空")
                else:
                    self.log.debug("变量AppId:" + app_id)
                    globalParams.set_value('app_id', app_id)
                    return app_id
            else:
                self.log.error("createAppId----------->>>>>>>>>>为空")

        except Exception as e:
            self.log.error("获取app_id失败! 错误信息：%s" % e)

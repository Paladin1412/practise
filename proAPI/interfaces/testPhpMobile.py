#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Date    : 2017/4/24 18:04
# @Version : python 3.4
# @Author  : KingDow
import sys

from common import commFunc
from common import globalParams
from common.httpConfig import GetHttp
from common.logConfig import GetLog
from common.readConfig import ReadConfig


class PhpMobile(object):
    def __init__(self):
        self.log = GetLog().log()
        self.http = GetHttp('interfaces_domain').get_http()

    def get_is_focus_resblock(self):
        """
        判断是否聚焦楼盘
        :return:is_focus=1 -->聚焦楼盘
        """
        url = '/index.php?_p=api_mobile&_a=getIsFocusResblock'
        data = {'timestamp': commFunc.timestamp_10(),
                'uid': globalParams.get_value('login_uid'),
                'user_account': globalParams.get_value('login_uid'),
                'house_num': ReadConfig(conf_path='keeperParanmsPath').conf_value('RESBLOCK', 'resblockId'),
                'sign': commFunc.get_app_sign(globalParams.get_value('login_uid'), commFunc.timestamp_10())
                }
        resp = self.http.http_post(url, data)

        if resp.get('data').get('is_focus') != 1:
            self.log.error("所选择的楼盘是非聚焦楼盘！楼盘id---->>%s" % data.get('resblockId'))
            sys.exit()
        return resp

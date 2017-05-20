#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Date    : 2017/4/25 11:51
# @Version : python 3.4
# @Author  : KingDow
from testCase.ziroomer.getappid import CommonApiParas


class KeeperParams(object):
    def __init__(self):
        self.appType = '1'
        self.companyFlag = '0'
        self.uid = 'suikk'
        # self.user_account = '20117602'
        self.password = '123'
        self.login_name = 'suikk'

        self.source = 1  # 请求类型：1是app请求；2是服务器请求
        self.app_id = CommonApiParas().get_appid
        self.resblockId = '1111027374425'  # 楼盘ID
        self.resblock = '芳园里'
        self.districtId = '23008613'
        self.buildingNo = '10号楼'
        self.unit = '1单元'
        self.floor = '3'
        self.cityCode = '110000'
        self.osType = '2'
        self.imei = '354782061807702'
        self.versionInt = '20403'

        self.condition = '13521672814'

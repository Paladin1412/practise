#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Date    : 2017/4/24 17:52
# @Version : python 3.4
# @Author  : KingDow
from common import commFunc
from common import globalParams
from common.httpConfig import GetHttp
from common.readConfig import ReadConfig


class BusOpp(object):
    def __init__(self):
        self.http = GetHttp('busopp_domain').get_http()

    def query_opp_page_info(self):
        url = '/busopp/queryOppPageInfo'
        data = {'keeperId': globalParams.get_value('login_uid'),
                'appType': ReadConfig('keeperParams').conf_value('keeperParams', 'appType'),
                'source': ReadConfig('keeperParams').conf_value('keeperParams', 'source'),
                'keeperCode': globalParams.get_value('login_uid'),
                'osType': ReadConfig('keeperParams').conf_value('keeperParams', 'osType'),
                'imei': ReadConfig('keeperParams').conf_value('keeperParams', 'imei'),
                'versionInt': ReadConfig('keeperParams').conf_value('keeperParams', 'versionInt'),
                'uuid': globalParams.get_value('app_id') + commFunc.timestamp_13(),
                'timestamp': commFunc.timestamp_13(),
                'appId': globalParams.get_value('app_id'),
                'cityCode': ReadConfig('keeperParams').conf_value('keeperParams', 'cityCode')
                }
        data['sign'] = commFunc.get_crm_sign(data)
        resp = self.http.http_post(url, data)
        return resp

    def query_opp_life_cycle_new(self):
        """
        POST http://busopp.t.ziroom.com/crm-reserve/busopp/queryOppLifeCycleNew HTTP/1.1
        :return:
        """
        url = '/busopp/queryOppLifeCycleNew'
        data = {
            "timestamp": commFunc.timestamp_13(),
            "busOppId": globalParams.get_value('busopp_id'),
            "imei": ReadConfig('keeperParams').conf_value('keeperParams', 'imei'),
            "cityCode": ReadConfig('keeperParams').conf_value('keeperParams', 'cityCode'),
            "source": ReadConfig('keeperParams').conf_value('keeperParams', 'source'),
            "keeperCode": globalParams.get_value('login_uid'),
            "versionInt": ReadConfig('keeperParams').conf_value('keeperParams', 'versionInt'),
            "appType": ReadConfig('keeperParams').conf_value('keeperParams', 'appType'),
            "uuid": globalParams.get_value('app_id') + commFunc.timestamp_13(),
            "appId": globalParams.get_value('app_id'),
            "osType": ReadConfig('keeperParams').conf_value('keeperParams', 'osType')
        }
        data['sign'] = commFunc.get_crm_sign(data)
        resp = self.http.http_post(url, data)
        return resp

    def get_child_list_by_ident(self, identifier='busoppTrackType'):
        """
        POST http://busopp.t.ziroom.com/crm-reserve/dictory/getChildListByIdent HTTP/1.1
        :return:
        """
        url = '/dictory/getChildListByIdent'
        data = {
            "osType": ReadConfig('keeperParams').conf_value('keeperParams', 'osType'),
            "keeperCode": globalParams.get_value('login_uid'),
            "cityCode": ReadConfig('keeperParams').conf_value('keeperParams', 'cityCode'),
            "identifier": identifier,
            "uuid": globalParams.get_value('app_id') + commFunc.timestamp_13(),
            "timestamp": commFunc.timestamp_13(),
            "appId": globalParams.get_value('app_id'),
            "imei": ReadConfig('keeperParams').conf_value('keeperParams', 'imei'),
            "appType": ReadConfig('keeperParams').conf_value('keeperParams', 'appType'),
            "versionInt": ReadConfig('keeperParams').conf_value('keeperParams', 'versionInt'),
            "source": ReadConfig('keeperParams').conf_value('keeperParams', 'source')
        }
        data['sign'] = commFunc.get_crm_sign(data)
        resp = self.http.http_post(url, data)

        response = resp.get('data')
        if response:
            if identifier == 'busoppTrackType':
                pass
            elif identifier == 'repair':
                globalParams.set_value('repairId', response[0].get("id"))
                globalParams.set_value('repairCode', response[0].get("code"))
            elif identifier == "payway":
                globalParams.set_value('paywayId', response[0].get("id"))
                globalParams.set_value('paywayCode', response[0].get("code"))
            else:
                print('identifier值输入有误，请重新输入！' + identifier)
        return resp

    def get_survey_info_list_by_house_id(self):
        """
        POST http://busopp.t.ziroom.com/crm-reserve/house/getSurveyInfoListByHouseId HTTP/1.1
        :return:
        """
        url = '/house/getSurveyInfoListByHouseId'
        data = {
            "isHistory": "0",
            "versionInt": ReadConfig('keeperParams').conf_value('keeperParams', 'versionInt'),
            "appType": ReadConfig('keeperParams').conf_value('keeperParams', 'appType'),
            "appId": globalParams.get_value('app_id'),
            "imei": ReadConfig('keeperParams').conf_value('keeperParams', 'imei'),
            "timestamp": commFunc.timestamp_13(),
            "uuid": globalParams.get_value('app_id') + commFunc.timestamp_13(),
            "source": ReadConfig('keeperParams').conf_value('keeperParams', 'source'),
            "houseId": globalParams.get_value('house_id'),
            "osType": ReadConfig('keeperParams').conf_value('keeperParams', 'osType'),
            "cityCode": ReadConfig('keeperParams').conf_value('keeperParams', 'cityCode'),
            "keeperCode": globalParams.get_value('login_uid')
        }
        data['sign'] = commFunc.get_crm_sign(data)
        resp = self.http.http_post(url, data)
        return resp

    def commit_survey(self):
        """
        POST http://busopp.t.ziroom.com/crm-reserve/house/commitSurvey HTTP/1.1
        :return:
        """
        url = '/house/commitSurvey'
        data = {
            "state": ReadConfig('keeperParams').conf_value('keeperParams', 'state'),
            "houseId": globalParams.get_value('house_id'),
            "appId": globalParams.get_value('app_id'),
            "changeFromNum": ReadConfig('keeperParams').conf_value('keeperParams', 'changeFromNum'),
            "repairCode": globalParams.get_value('repairCode'),
            "area": ReadConfig('keeperParams').conf_value('keeperParams', 'area'),
            "timestamp": commFunc.timestamp_13(),
            "toilet": ReadConfig('keeperParams').conf_value('keeperParams', 'toilet'),
            "osType": ReadConfig('keeperParams').conf_value('keeperParams', 'osType'),
            "keeperName": globalParams.get_value('agent_name'),
            "decorateType": ReadConfig('keeperParams').conf_value('keeperParams', 'decorateType'),
            "keeperCode": globalParams.get_value('login_uid'),
            "repairId": globalParams.get_value('repairId'),
            "changeToNum": ReadConfig('keeperParams').conf_value('keeperParams', 'changeToNum'),
            "cityCode": ReadConfig('keeperParams').conf_value('keeperParams', 'cityCode'),
            "versionInt": ReadConfig('keeperParams').conf_value('keeperParams', 'versionInt'),
            "surveySource": "0",
            "yearNum": ReadConfig('keeperParams').conf_value('keeperParams', 'yearNum'),
            "mouthNum": ReadConfig('keeperParams').conf_value('keeperParams', 'mouthNum'),
            "roomList": ReadConfig('keeperParams').conf_value('keeperParams', 'roomList'),
            "source": ReadConfig('keeperParams').conf_value('keeperParams', 'source'),
            "appType": ReadConfig('keeperParams').conf_value('keeperParams', 'appType'),
            "payWayCode": globalParams.get_value('paywayCode'),
            "imei": ReadConfig('keeperParams').conf_value('keeperParams', 'imei'),
            "payWayId": globalParams.get_value('paywayId'),
            "keeperId": globalParams.get_value('login_uid'),
            "uuid": globalParams.get_value('app_id') + commFunc.timestamp_13(),
            "keeperPhone": globalParams.get_value('agent_phone')
        }
        data['sign'] = commFunc.get_crm_sign(data)
        resp = self.http.http_post(url, data)
        return resp

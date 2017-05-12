#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Date    : 2017/4/24 17:49
# @Version : python 3.4
# @Author  : KingDow
from common.httpConfig import GetHttp
from common.logConfig import GetLog


class KeeperBusOpp(object):
    def __init__(self):
        self.log = GetLog().log()
        self.http = GetHttp().get_http()

    def test_query_perform(self):
        url = '/busopp/queryPerform'
        data = {'keeperId': '20189548',
                'sign': '686a4bb1e7d9fe9c3c89bae9ed93b43c',
                'appType': '1',
                'source': '1',
                'keeperCode': '20189548',
                'osType': '2',
                'imei': '354782061807702',
                'versionInt': '20403',
                'uuid': '10217570121493027285462',
                'timestamp': '1493027285462',
                'appId': '1021757012',
                'cityCode': '110000'
                }

        r = self.http.http_post(url, data)
        return r.json()

    def test_get_user_info_by_condition(self):
        url = '/user/getUserInfoByCondition'
        data = {'sign': '417fa99356bd717e8df2d0c3b67f9e94',
                'appType': '1',
                'source': '1',
                'keeperCode': '20189548',
                'osType': '2',
                'imei': '354782061807702',
                'versionInt': '20403',
                'uuid': '10217570121493027827581',
                'timestamp': '1493027827581',
                'condition': '13521672814',
                'appId': '1021757012',
                'cityCode': '110000'
                }

        r = self.http.http_post(url, data)
        return r.json()

    def test_get_village_list(self):
        url = '/house/getVillageList'
        data = {'sign': '903acdf1b9c82348f22d96d1e8916d2f',
                'source': '1',
                'uuid': '10217570121493028005816',
                'timestamp': '1493028005816',
                'resblock': '%E5%A4%A9%E5%85%86',
                'appId': '1021757012',
                'cityCode': '110000',
                'keeperId': '20189548',
                'districtId': '23008613',
                'appType': '1',
                'keeperCode': '20189548',
                'osType': '2',
                'imei': '354782061807702',
                'versionInt': '20403'
                }
        r = self.http.http_post(url, data)
        return r.json()

    def test_app_search_bus_opp_by_standard_info(self):
        url = '/busopp/appSearchBusOppByStandardInfo'
        data = {'sign': '5365564f90dba52cd12755bfa724df8c',
                'source': '1',
                'buildNum': '11%E5%8F%B7%E6%A5%BC',
                'uuid': '10217570121493029345710',
                'timestamp': '1493029345710',
                'appId': '1021757012',
                'roomNum': '402',
                'cityCode': '110000',
                'districtId': '23008613',
                'keeperId': '20189548',
                'appType': '1',
                'keeperCode': '20189548',
                'osType': '2',
                'imei': '354782061807702',
                'versionInt': '20403',
                'unit': '2%E5%8D%95%E5%85%83',
                'floor': '4',
                'villageId': '1111027374425'
                }
        r = self.http.http_post(url, data)
        return r.json()

    def test_check_bus_opp(self):
        url = '/busopp/checkBusOpp'
        data = {'sign': 'e2b6845d0bc81510be73b6c321e764d7',
                'source': '1',
                'buildNum': '11%E5%8F%B7%E6%A5%BC',
                'uuid': '10217570121493029345855',
                'districtName': '%E6%9C%9D%E9%98%B3',
                'timestamp': '1493029345855',
                'appId': '1021757012',
                'roomNum': '402',
                'cityCode': '110000',
                'districtId': '23008613',
                'appType': '1',
                'keeperCode': '20189548',
                'osType': '2',
                'imei': '354782061807702',
                'versionInt': '20403',
                'isTopBaseFloor': '0',
                'villageName': '%E8%8A%B3%E5%9B%AD%E9%87%8C',
                'unit': '2%E5%8D%95%E5%85%83',
                'floor': '4',
                'villageId': '1111027374425'
                }
        r = self.http.http_post(url, data)
        return r.json()

    def test_query_bo_first_source_list(self):
        url = '/busopp/queryBOFirstSourceList'
        data = {'sign': '0a874fd3de9afc418edaef93f919930a',
                'appType': '1',
                'source': '1',
                'keeperCode': '20189548',
                'osType': '2',
                'imei': '354782061807702',
                'versionInt': '20403',
                'uuid': '10217570121493029561108',
                'timestamp': '1493029561108',
                'appId': '1021757012',
                'boType': '1',
                'cityCode': '110000'
                }
        r = self.http.http_post(url, data)
        return r.json()

    def test_query_bo_second_source_list(self):
        url = '/busopp/queryBOSecondSourceList'
        data = {'sign': 'ac9c821069964ce1626e5893e310f322',
                'appType': '1',
                'source': '1',
                'keeperCode': '20189548',
                'osType': '2',
                'imei': '354782061807702',
                'versionInt': '20403',
                'uuid': '10217570121493029566321',
                'timestamp': '1493029566321',
                'appId': '1021757012',
                'firstSourceId': '104',
                'cityCode': '110000'
                }
        r = self.http.http_post(url, data)
        return r.json()

    def test_get_keeper_by_and_source_type(self):
        url = '/busopp/getKeeperByAndSourceType'
        data = {'entryPersonName': '%E9%BB%84%E6%98%A5%E6%99%93',
                'sign': '39b3de5578cc9fc2544aad0b6c057d57',
                'source': '1',
                'entryPersonCode': '20189548',
                'firstSource': '153',
                'buildNum': '11%E5%8F%B7%E6%A5%BC',
                'uuid': '10217570121493029809106',
                'secondSource': '151',
                'timestamp': '1493029809106',
                'appId': '1021757012',
                'roomNum': '402',
                'cityCode': '110000',
                'keeperId': '20189548',
                'districtId': '23008613',
                'appType': '1',
                'keeperCode': '20189548',
                'osType': '2',
                'imei': '354782061807702',
                'versionInt': '20403',
                'unit': '2%E5%8D%95%E5%85%83',
                'floor': '4',
                'villageId': '1111027374425'
                }
        r = self.http.http_post(url, data)
        return r.json()

#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Date    : 2017/4/24 18:10
# @Version : python 3.4
# @Author  : KingDow

from bs4 import BeautifulSoup
from common import commFunc
from common import globalParams
from common.dbConfig import GetMysql
from common.httpConfig import GetHttp
from common.logConfig import GetLog
from common.readConfig import ReadConfig


class ModelPrice(object):
    def __init__(self):
        self.log = GetLog().log()
        self.http = GetHttp('modelprice_domain').get_http()

    def modelprice_login(self):
        """
        GET http://modeprice.m.t.ziroom.com/index.php?r=login/login& HTTP/1.1
        计价模型登录，登录成功后自动加载首页
        :return:
        """
        url = '/index.php'
        param = {
            'r': 'login/login',
            'sign': commFunc.get_app_sign(globalParams.get_value('login_uid'), commFunc.timestamp_10()),
            'agent_part': globalParams.get_value('agent_part'),
            'city_code': ReadConfig('keeperParams').conf_value('keeperParams', 'cityCode'),
            'user_account': globalParams.get_value('login_uid'),
            'agent_name': globalParams.get_value('agent_name'),
            'timestamp': commFunc.timestamp_10(),
            'blonger_group': globalParams.get_value('bloger_group')
        }
        resp = self.http.http_get(url, param)
        return resp

    def guide_index(self):
        """
        GET http://modeprice.m.t.ziroom.com/index.php?r=zz/guide/index HTTP/1.1
        计价模型首页，选择产品类型
        :return:
        """
        url = '/index.php'
        param = {
            'r': 'zz/guide/index'
        }
        resp = self.http.http_get(url, param)
        return resp

    def resblock_info(self):
        """
        GET http://modeprice.m.t.ziroom.com/index.php?r=m-house-step/resblock-info HTTP/1.1
        楼盘信息
        :return:
        """
        url = '/index.php'
        param = {
            'r': 'm-house-step/resblock-info'
        }
        resp = self.http.http_get(url, param)
        return resp

    def district_info(self):
        """
        POST http://modeprice.m.t.ziroom.com/index.php?r=m-house-step/get-house-info HTTP/1.1
        区域信息
        :return:
        """
        url = '/index.php?r=m-house-step/get-house-info'
        data = {'type': 'district',
                'city_code': ReadConfig('keeperParams').conf_value('keeperParams', 'cityCode')
                }
        resp = self.http.http_post(url, data=data)
        return resp

    def get_resblock(self):
        """
        POST http://modeprice.m.t.ziroom.com/index.php?r=m-house-step/get-house-info HTTP/1.1
        精确楼盘信息
        :return:
        """
        url = '/index.php?r=m-house-step/get-house-info'
        data = {
            'type': 'loupan',
            'resblock': '弘善家园',
            'district_id': ReadConfig('keeperParams').conf_value('keeperParams', 'districtId')
        }
        resp = self.http.http_post(url, data)
        return resp

    def get_is_focus(self):
        """
        POST http://modeprice.m.t.ziroom.com/index.php?r=m-house-step/get-isfocus HTTP/1.1
        是否聚焦楼盘
        :return:
        """
        url = '/index.php?r=m-house-step/get-isfocus'
        data = {'house_num': globalParams.get_value('resblock_id')}
        resp = self.http.http_post(url, data)
        return resp

    def get_building_info(self):
        """
        POST http://modeprice.m.t.ziroom.com/index.php?r=m-house-step/get-house-info HTTP/1.1
        获取楼栋列表
        :return:
        """
        url = '/index.php?r=m-house-step/get-house-info'
        data = {
            'type': 'loudong',
            'resblock_id': globalParams.get_value('resblock_id'),
            'district_id': ReadConfig('keeperParams').conf_value('keeperParams', 'districtId')
        }
        resp = self.http.http_post(url, data)
        return resp

    def get_unit_info(self):
        """
        POST http://modeprice.m.t.ziroom.com/index.php?r=m-house-step/get-house-info HTTP/1.1
        获取楼栋单元列表
        :return:
        """
        url = '/index.php?r=m-house-step/get-house-info'
        data = {
            'type': 'danyuan',
            'building_no': globalParams.get_value('building_no'),
            'resblock_id': globalParams.get_value('resblock_id'),
            'district_id': ReadConfig('keeperParams').conf_value('keeperParams', 'districtId')
        }
        resp = self.http.http_post(url, data)
        return resp

    def get_floor_info(self):
        """
        POST http://modeprice.m.t.ziroom.com/index.php?r=m-house-step/get-house-info HTTP/1.1
        获取单元楼层列表
        :return:
        """
        url = '/index.php?r=m-house-step/get-house-info'
        data = {
            'type': 'louceng',
            'building_no': globalParams.get_value('building_no'),
            'resblock_id': globalParams.get_value('resblock_id'),
            'unit': globalParams.get_value('unit'),
            'district_id': ReadConfig('keeperParams').conf_value('keeperParams', 'districtId')
        }
        resp = self.http.http_post(url, data)
        return resp

    def get_room_info(self):
        """
        POST http://modeprice.m.t.ziroom.com/index.php?r=m-house-step/get-house-info HTTP/1.1
        获取楼层房间列表
        :return:
        """
        url = '/index.php?r=m-house-step/get-house-info'
        data = {
            'type': 'fangwu',
            'building_no': globalParams.get_value('building_no'),
            'resblock_id': globalParams.get_value('resblock_id'),
            'unit': globalParams.get_value('unit'),
            'floor': globalParams.get_value('floor'),
            'district_id': ReadConfig('keeperParams').conf_value('keeperParams', 'districtId')
        }
        resp = self.http.http_post(url, data)
        return resp

    def get_standard_info(self):
        """
        POST http://modeprice.m.t.ziroom.com/index.php?r=m-house-step/get-house-info HTTP/1.1
        获取standard_id
        :return:
        """
        url = '/index.php?r=m-house-step/get-house-info'
        data = {
            'type': 'standard_id',
            'building_no': globalParams.get_value('building_no'),
            'resblock_id': globalParams.get_value('resblock_id'),
            'unit': globalParams.get_value('unit'),
            'floor': globalParams.get_value('floor'),
            'district_id': ReadConfig('keeperParams').conf_value('keeperParams', 'districtId')
        }
        resp = self.http.http_post(url, data)
        standard_info = resp.get('data')[0]
        if standard_info:
            globalParams.set_value('standard_id', standard_info.get('standard_id'))
        else:
            self.log.warning('获取standard_id失败，请检查后重试！')
        return resp

    def commit_house_info(self):
        """
        POST http://modeprice.m.t.ziroom.com/index.php?r=m-house-step/commit-house-info HTTP/1.1
        提交房屋信息
        :return:
        """
        url = '/index.php?r=m-house-step/commit-house-info'
        data = {
            'city_code': ReadConfig('keeperParams').conf_value('keeperParams', 'cityCode'),
            'building_no': globalParams.get_value('building_no'),
            'resblock_id': globalParams.get_value('resblock_id'),
            'resblock': globalParams.get_value('resblock_name'),
            'unit': globalParams.get_value('unit'),
            'floor': globalParams.get_value('floor'),
            'district_id': ReadConfig('keeperParams').conf_value('keeperParams', 'districtId'),
            'district': ReadConfig('keeperParams').conf_value('keeperParams', 'districtName'),
            'room_no': globalParams.get_value('room_no'),
            'house_code_id': globalParams.get_value('standard_id'),
            'is_first_floor': ReadConfig('keeperParams').conf_value('keeperParams', 'isTopBaseFloor')
        }
        resp = self.http.http_post(url, data)
        assess_info = resp.get('data')
        if assess_info:
            globalParams.set_value('assess_code', assess_info.get('assess_code'))
        else:
            self.log.warning('获取assess_code失败，请检查后重试！')
        return resp

    def detail_house_info(self):
        """
        GET http://modeprice.m.t.ziroom.com/index.php?r=m-house-step/detail-house-info HTTP/1.1
        加载房屋信息
        :return:
        """
        url = '/index.php?r=m-house-step/detail-house-info'
        data = {'assess_code': globalParams.get_value('assess_code')}
        resp = self.http.http_post(url, data)
        return resp

    def get_rent_price(self):
        """
        POST http://modeprice.m.t.ziroom.com/index.php?r=m-room-step/get-rent-price HTTP/1.1
        得到出房评估价格
        :return:
        """
        url = '/index.php?r=m-room-step/get-rent-price'
        data = {
            'assess_code': globalParams.get_value('assess_code'),
            'pre_room': ReadConfig('keeperParams').conf_value('keeperParams', 'changeFromNum'),  # 改前房间数
            'after_room': ReadConfig('keeperParams').conf_value('keeperParams', 'changeToNum'),  # 改后房间数
            'decorate_type': ReadConfig('keeperParams').conf_value('keeperParams', 'decorateType'),  # 装修类型
            'saloon_area': ReadConfig('keeperParams').conf_value('keeperParams', 'saloon_area'),  # 客厅面积
            'room_area': ReadConfig('keeperParams').conf_value('keeperParams', 'saloon_area'),  # 房间面积
            'orientation': ReadConfig('keeperParams').conf_value('keeperParams', 'orientation'),  # 房间朝向
            'toliet': ReadConfig('keeperParams').conf_value('keeperParams', 'toliet'),  # 是否独卫
            'balcony': ReadConfig('keeperParams').conf_value('keeperParams', 'balcony'),  # 是否独立阳台
            'is_new_room': ReadConfig('keeperParams').conf_value('keeperParams', 'is_new_room'),  # 是否优化间
            'is_shelter': ReadConfig('keeperParams').conf_value('keeperParams', 'is_shelter'),  # 是否有遮挡
            'rent_type': ReadConfig('keeperParams').conf_value('keeperParams', 'rent_type'),
            'version': ReadConfig('keeperParams').conf_value('keeperParams', 'version')
        }
        resp = self.http.http_post(url, data)
        rent_price_info = resp.get('data')
        if rent_price_info:
            globalParams.set_value('rent_price', rent_price_info.get('rentPrice'))
        else:
            self.log.warning('计价模型计算出房评估价格有误，请检查后重试！')
        return resp

    def commit_room_info(self):
        """
        POST http://modeprice.m.t.ziroom.com/index.php?r=m-room-step/commit-room-info HTTP/1.1
        提交房间信息
        :return:
        """
        url = '/index.php?r=m-room-step/commit-room-info'
        data = {
            'assess_code': globalParams.get_value('assess_code'),
            'pre_room': ReadConfig('keeperParams').conf_value('keeperParams', 'changeFromNum'),  # 改前房间数
            'after_room': ReadConfig('keeperParams').conf_value('keeperParams', 'changeToNum'),  # 改后房间数
            'decorate_type': ReadConfig('keeperParams').conf_value('keeperParams', 'decorateType'),  # 装修类型
            'saloon_area': ReadConfig('keeperParams').conf_value('keeperParams', 'saloon_area'),  # 客厅面积
            'room_area': ReadConfig('keeperParams').conf_value('keeperParams', 'saloon_area'),  # 房间面积
            'orientation': ReadConfig('keeperParams').conf_value('keeperParams', 'orientation'),  # 房间朝向
            'toliet': ReadConfig('keeperParams').conf_value('keeperParams', 'toliet'),  # 是否独卫
            'balcony': ReadConfig('keeperParams').conf_value('keeperParams', 'balcony'),  # 是否独立阳台
            'is_new_room': ReadConfig('keeperParams').conf_value('keeperParams', 'is_new_room'),  # 是否优化间
            'is_shelter': ReadConfig('keeperParams').conf_value('keeperParams', 'is_shelter'),  # 是否有遮挡
            'yg': ReadConfig('keeperParams').conf_value('keeperParams', 'yg'),  # 衣柜
            'shzh': ReadConfig('keeperParams').conf_value('keeperParams', 'shzh'),  # 书桌
            'shf': ReadConfig('keeperParams').conf_value('keeperParams', 'shf'),  # 沙发
            'kt': ReadConfig('keeperParams').conf_value('keeperParams', 'kt'),  # 空调
            '1_1mch': ReadConfig('keeperParams').conf_value('keeperParams', '1_1mch'),  # 1.1m床
            '1_1mchd': ReadConfig('keeperParams').conf_value('keeperParams', '1_1mchd'),  # 1.1m床垫
            '1_5mch': ReadConfig('keeperParams').conf_value('keeperParams', '1_5mch'),  # 1.5m床
            '1_5mchd': ReadConfig('keeperParams').conf_value('keeperParams', '1_5mchd'),  # 1.5m床垫
            '1_8mch': ReadConfig('keeperParams').conf_value('keeperParams', '1_8mch'),  # 1.8m床
            '1_8mchd': ReadConfig('keeperParams').conf_value('keeperParams', '1_8mchd'),  # 1.8m床垫
            'stardard_rent_price': globalParams.get_value('rent_price'),
            'real_rent_price': globalParams.get_value('rent_price')
        }
        resp = self.http.http_post(url, data)
        return resp

    def get_hire_price(self):
        """
        POST http://modeprice.m.t.ziroom.com/index.php?r=m-house-step/get-hire-price HTTP/1.1
        获取收房价格
        :return:
        """
        url = '/index.php?r=m-house-step/get-hire-price'
        data = {
            'assess_code': globalParams.get_value('assess_code'),
            'public_toliet': ReadConfig('keeperParams').conf_value('keeperParams', 'toliet'),  # 公共卫生间
            'pre_room': ReadConfig('keeperParams').conf_value('keeperParams', 'changeFromNum'),  # 改前房间数
            'after_room': ReadConfig('keeperParams').conf_value('keeperParams', 'changeToNum'),  # 改后房间数
            'decorate_type': ReadConfig('keeperParams').conf_value('keeperParams', 'decorateType'),  # 装修类型
            'area': ReadConfig('keeperParams').conf_value('keeperParams', 'area'),  # 房屋面积
            'saloon_area': ReadConfig('keeperParams').conf_value('keeperParams', 'saloon_area'),  # 客厅面积
            'rent_type': ReadConfig('keeperParams').conf_value('keeperParams', 'rent_type'),
            'version': ReadConfig('keeperParams').conf_value('keeperParams', 'version'),
            'decorate_year': ReadConfig('keeperParams').conf_value('keeperParams', 'decorate_year'),
            'lease_year': ReadConfig('keeperParams').conf_value('keeperParams', 'yearNum'),
            'lease_month': ReadConfig('keeperParams').conf_value('keeperParams', 'mouthNum'),
            'owner_payment': ReadConfig('keeperParams').conf_value('keeperParams', 'owner_payment'),
            'payment': ReadConfig('keeperParams').conf_value('keeperParams', 'payment'),
            'fund': ReadConfig('keeperParams').conf_value('keeperParams', 'fund')
        }
        for i in range(1, int(data.get('payment')) + 1):
            data['vanancy_day[%s][vanancy_day]' % i] = '30'
        resp = self.http.http_post(url, data)
        return resp

    def get_assess_result(self):
        """
        GET http://modeprice.m.t.ziroom.com/index.php?r=m-house-step/get-assess-result HTTP/1.1
        得到评估结果
        :return:
        """
        url = '/index.php?r=m-house-step/get-assess-result'
        param = {'assess_code': globalParams.get_value('assess_code')}
        resp = self.http.http_get(url, param)
        soup = BeautifulSoup(resp, 'html.parser')
        real_sh_jg = soup.find_all('span', id='cksf')[0].string
        if real_sh_jg:
            globalParams.set_value('real_sh_jg', real_sh_jg)
        else:
            self.log.warning('解析评估结果HTML页面，获取参考收房价有误！')
        return resp

    def commit_assess_info(self):
        """
        POST http://modeprice.m.t.ziroom.com/index.php?r=m-assess-step/commit-assess-info HTTP/1.1
        提交评估
        :return:
        """
        url = '/index.php?r=m-assess-step/commit-assess-info'
        param = {
            'assess_code': globalParams.get_value('assess_code'),
            'real_sh_jg': globalParams.get_value('real_sh_jg'),
            'op': 'button_audit'
        }
        resp = self.http.http_get(url, param)
        return resp

    def assess_list_info(self):
        """
        GET http://modeprice.m.t.ziroom.com/index.php?r=assess HTTP/1.1
        查看评估列表
        :return:
        """
        url = '/index.php?r=assess'
        resp = self.http.http_get(url)
        return resp

    def view_assess_info(self):
        """
        GET http://modeprice.m.t.ziroom.com/index.php?r=assess/view&house_code_id=1115032204961 HTTP/1.1
        查看评估记录
        :return:
        """
        url = '/index.php?r=assess/view'
        param = {'house_code_id': globalParams.get_value('standard_id')}
        resp = self.http.http_get(url, param)
        return resp

    @staticmethod
    def get_access_id():
        mysql = GetMysql('mode_price', 'mode_price_config')
        mysql_conn = mysql.get_mysql_conn()
        mysql_cur = mysql_conn.cursor()
        assess_code = globalParams.get_value('assess_code')
        sql = 'Select id from mode_price.t_price_mode_assess where assess_code=%s' % assess_code
        mysql_cur.execute(sql)
        assess_id = mysql_cur.fetchall()
        globalParams.set_value('assess_id', assess_id)
        mysql.mysql_conn_close()
        return assess_id

    def admit_assess_info(self):
        """
        GET http://modeprice.m.t.ziroom.com/index.php?r=assess/admit-assess&type=report&id=126217 HTTP/1.1
        上报评估结果
        :return:
        """
        access_id = self.get_access_id()
        url = '/index.php'
        param = {
            'r': 'assess/admit-assess',
            'type': 'report',
            'id': access_id
        }
        resp = self.http.http_get(url, param)
        return resp

    def undo_assess_info(self):
        """
        GET http://modeprice.m.t.ziroom.com/index.php?r=assess/admit-assess&type=undo&id=126217 HTTP/1.1
        撤销评估结果
        :return:
        """
        url = '/index.php'
        param = {
            'r': 'assess/admit-assess',
            'type': 'undo',
            'id': globalParams.get_value('assess_id')
        }
        resp = self.http.http_get(url, param)
        return resp

    def del_assess_info(self):
        """
        GET http://modeprice.m.t.ziroom.com/index.php?r=assess/admit-assess&id=126217 HTTP/1.1
        删除评估结果
        :return:
        """
        url = '/index.php'
        param = {
            'r': 'assess/admit-assess',
            'id': globalParams.get_value('assess_id')
        }
        resp = self.http.http_get(url, param)
        return resp

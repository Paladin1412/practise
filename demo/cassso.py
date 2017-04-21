#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Date    : 2017/4/1 15:07
# @Version : python 3.4
# @Author  : KingDow

import requests
from bs4 import BeautifulSoup


class CasSso(object):
    def __init__(self):
        self.url = 'http://z.ziroom.com'
        self.userinfo = {
            'username': 'yangjb18',
            'password': 'Yang1234'
        }
        # self.header = {
        #     "Connection": "keep-alive",
        #     "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64)",
        #     "Content-Type": "application/x-www-form-urlencoded",
        #     "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"
        # }, headers=self.header, headers=self.header

    def cas_sso(self):
        r = requests.get(self.url)
        soup = BeautifulSoup(r.text, 'html.parser')
        hidden = soup.find_all('input', attrs={'type': "hidden"})
        hidden_auth = {}
        for i in hidden:
            hidden_auth[i.get('name')] = i.get('value')
        print(r.url)
        print(r.headers)
        # print(r.text)
        data = dict(hidden_auth, **self.userinfo)
        r2 = requests.post(r.url, data=data, cookies=r.cookies, allow_redirects=False)
        # print(r2.url)
        print(r2.headers.get('Location'))
        r3 = requests.get(r2.headers.get('Location'))
        print(r3.text)


cas = CasSso()
cas.cas_sso()




























# def cas_login(self):
#     self.set_header(self.header)
#     print("========以下进行CAS用户登录操作========")
#     first_url = '/AMS/security/security!index.action'
#     redirect_res = self.get(first_url).decode('utf-8')
#     redirect_url = re.findall(r'service=http%3A%2F%2F(.*?)%3A80%2FAMS', redirect_res, re.S | re.M)
#
#     print("========业务系统重定向跳转CAS========")
#     res = self.get('/CAS/login?service=http://%s:80%s' % (redirect_url[0], first_url), host='cas.ziroom.com')
#     lt = re.findall(r'name="lt" value="(.*?)" />', res.decode('utf-8'), re.S | re.M)
#     execution = re.findall(r'name="execution" value="(.*?)" />', res.decode('utf-8'), re.S | re.M)
#     event = re.findall(r'name="_eventId" value="(.*?)" />', res.decode('utf-8'), re.S | re.M)
#
#     print("========CAS校验用户名密码ticket========")
#     url = '/CAS/login?service=http:///%s:80%s' % (redirect_url[0], first_url)
#     data = 'username=%s&password=%s&lt=%s&execution=%s&_eventId=%s' % (
#         self.username, self.password, lt[0], execution[0], event[0])
#     cas_res = self.post(url, host='cas.ziroom.com', data=data)
#     return cas_res
#
# def user_login(self):
#     self.set_header(self.header)
#     print("========以下进行用户登录操作========\n")
#     data = "j_username=%s&j_password=%s" % (self.username, self.password)
#     url = "/AMS/security/security!login.action"
#     res = self.post(url, data=data)
#     return res
#
# def select_city(self):
#     if self.city_code == "110000":
#         territory_id = "11"  # 北京
#         print("@@@@@@@@当前登陆城市为：北京！@@@@@@@@")
#     elif self.city_code == "310000":
#         territory_id = "50"  # 上海
#         print("@@@@@@@@当前登陆城市为：上海！@@@@@@@@")
#     elif self.city_code == "440300":
#         territory_id = "24"  # 深圳
#         print("@@@@@@@@当前登陆城市为：深圳！@@@@@@@@")
#     else:
#         territory_id = "19"  # 民宿
#         print("@@@@@@@@当前登陆选择为：民宿！@@@@@@@@")
#
#     self.user_login() if '.t.' in self.host else self.cas_login()
#     url = "/AMS/security/security!selectCity.action"
#     params = "territoryId=%s&username=%s" % (territory_id, self.username)
#     print("========登陆成功，选择城市========")
#     res = self.get(url, params=params)
#     return res
#
# def index(self):
#     self.select_city()
#     print("========以下进行跳转资产首页操作========")
#     url = "/AMS/security/security!indexAMS.action"
#     res = self.get(url)
#     return res

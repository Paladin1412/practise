#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Date    : 2017/3/14 13:06
# @Version : python 3.4
# @Author  : KingDow
import requests
from globalparams import GlobalParams


class HttpConfig(object):
    def __init__(self, host, port=80, headers=None):
        self.host = 'http://' + host
        self.port = ':' + str(port)
        self.header = headers if headers else {}
        self.s = requests.Session()
        self.log = GlobalParams().log(__name__)

    def get_host(self):
        return self.host

    def set_host(self, host):
        self.host = host

    def set_port(self, port):
        self.port = port

    def set_header(self, header):
        self.header = header

    def http_post(self, url, data=None):
        url = self.host + self.port + url
        data = data if data else ''
        try:
            r = self.s.post(url=url, data=data, headers=self.header)
            if r.status_code == 200:
                self.log.info("发送post请求: %s  服务器返回:  %s" % (r.url, r.status_code))
            else:
                self.log.error("发送post请求: %s   服务器返回:  %s\n error info: %s " % (
                    r.url, r.status_code, r.text))
            return r
        except Exception as e:
            print('%s' % e)

    def http_get(self, url, param=None):
        url = self.host + self.port + url
        param = param if param else ''
        try:
            r = self.s.get(
                url=url, params=param, headers=self.header)
            if r.status_code == 200:
                self.log.info("发送post请求: %s  服务器返回:  %s" % (r.url, r.status_code))
            else:
                self.log.error("发送post请求: %s   服务器返回:  %s\n error info: %s " % (
                    r.url, r.status_code, r.text))
            return r
        except Exception as e:
            print('%s' % e)

    def http_put(self, url, data=None):
        r = self.s.put(url=url, data=data)
        return r

    def http_delete(self, url):
        r = self.s.delete(url=url)
        return r

    def http_head(self, url):
        r = self.s.head(url=url)
        return r

    def http_options(self, url):
        r = self.s.options(url=url)
        return r

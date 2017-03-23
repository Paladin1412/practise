#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Date    : 2017/3/14 13:06
# @Version : python 3.4
# @Author  : KingDow
import requests


class HttpConfig(object):
    def __init__(self, host, port=80, headers=None):
        self.host = 'http://' + host
        self.port = ':' + str(port)
        self.header = headers if headers else {}
        self.s = requests.Session()

    def get_host(self):
        return self.host

    def set_host(self, host):
        self.host = host

    def set_port(self, port):
        self.port = port

    def http_post(self, url, data=None):
        url = self.host + self.port + url
        data = data if data else ''
        r = self.s.post(
            url=url, data=data, headers=self.header)
        return r

    def http_get(self, url, param=None):
        url = self.host + self.port + url
        param = param if param else ''
        r = self.s.get(
            url=url, params=param, headers=self.header)
        return r

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

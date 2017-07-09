#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Date    : 2017/3/14 13:06
# @Version : python 3.4
# @Author  : KingDow
import requests
from common import readConfig
from common.logConfig import GetLog


class HttpConfig(object):
    def __init__(self, host, port=None, headers=None):
        if host.find('s.t.ziroom.com') != -1 or host.find('busopp.t.ziroom.com') != -1:
            self.host = host + '/crm-reserve'
        else:
            self.host = host
        if self.host.find('http') == -1:
            self.host = 'http://' + self.host
        self.port = ':' + str(port) if port else ''
        self.header = headers if headers else {}
        self.s = requests.Session()
        self.log = GetLog().log()

    def get_host(self):
        return self.host

    def set_host(self, host):
        self.host = host

    def set_port(self, port):
        self.port = port

    def set_header(self, header):
        self.header = header

    def http_get(self, url, param=None):
        url = self.host + self.port + url
        param = param if param else ''
        try:
            r = self.s.get(url=url, params=param, headers=self.header)
            if r.status_code == requests.codes.ok:
                self.log.info("发送get请求: %s，服务器返回: %s" % (r.url, r.status_code))
            else:
                self.log.error("发送get请求: %s，服务器返回: %s\n error info: %s" % (
                    r.url, r.status_code, r.text))
                self.log.error(r.raise_for_status())
            try:
                self.log.info('接口出参为: %s' % r.json())
                return r.json()
            except ValueError:
                self.log.info('接口出参为: %s' % r.text)
                return r.text
        except Exception as e:
            self.log.error('%s' % e)

    def http_post(self, url, data=None):
        url = self.host + self.port + url
        data = data if data else ''
        try:
            r = self.s.post(url=url, data=data, headers=self.header)
            if r.status_code == requests.codes.ok:
                self.log.info("发送post请求: %s 服务器返回: %s" % (r.url, r.status_code))
                self.log.info("请求入参为: %s" % data)
            else:
                self.log.error("发送post请求: %s ，请求入参为: %s，\n服务器返回: %s error info: %s " % (
                    r.url, data, r.status_code, r.text))
                self.log.error(r.raise_for_status())
            try:
                self.log.info('接口出参为: %s' % r.json())
                return r.json()
            except ValueError:
                self.log.info('接口出参为: %s' % r.text)
                return r.text
        except Exception as e:
            self.log.error('%s' % e)

    def multiple_post(self, url):
        url = self.host + self.port + url
        multiple_files = [
            ('images', ('foo.png', open('foo.png', 'rb'), 'image/png')),
            ('images', ('bar.png', open('bar.png', 'rb'), 'image/png'))]
        r = requests.post(url, files=multiple_files)
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


class GetHttp(object):
    def __init__(self, domain):
        read_config = readConfig.ReadConfig()
        self.domain = read_config.conf_value('HTTP', domain)
        self.header = read_config.conf_value('HTTP', 'header')
        self.http = None

    def get_http(self):
        if self.http is None:
            self.http = HttpConfig(host=self.domain, headers=self.header)
        return self.http

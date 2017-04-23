#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Date    : 2017/3/14 13:08
# @Version : python 3.4
# @Author  : KingDow
from common.httpConfig import GetHttp

if __name__ == '__main__':
    # gl = GetLog()
    # log = gl.log()
    # cap = CommonApiParas()
    # appId = cap.get_appid()
    # log.info('info')
    # log.error('error')
    # log.debug('debug')
    # log.critical('critical')
    # log.warning('warning')

    # log = GetLog().log()

    http = GetHttp().get_http()
    r = http.http_get('/')
    print(r.text)

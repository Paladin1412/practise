#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Date    : 2017/3/14 13:07
# @Version : python 3.4
# @Author  : KingDow
import hashlib
import os
import time

from common.logConfig import GetLog

log = GetLog().log()


def get_app_sign(uid, timestamp):
    key = "7srzT88FcNiRQA3n"
    if not uid:
        uid = "0"
    sign = to_md5(uid + timestamp + key)
    return sign


def to_md5(mystr):
    """
        指定字符串MD5加密
        :param mystr: 待MD5加密字符串
    """
    mybyte = mystr.encode(encoding='utf-8')
    m = hashlib.md5(mybyte)
    return m.hexdigest()


def timestamp_10():
    """
        返回当前时间unix10位时间戳
    """
    return str(int(time.time()))


def timestamp_13():
    """
        返回当前时间unix13位时间戳
    """
    return str(int(round(time.time() * 1000)))


def is_path(path):
    return os.path.isdir(path)


def is_path_exist(path):
    if not os.path.exists(path):
        os.makedirs(path)


def is_file_exist(path):
    try:
        with open(path) as f:
            f.close()
            return True
    except IOError:
        return False


def str2json(data, value_type='str'):
    data = data[:-1] if data[-1] == '&' else data
    if value_type == 'str':
        json_value = dict((l.split('=') for l in data.split('&')))
        if json_value:
            log.debug('转换str类型value dict成功：\n%s' % json_value)
            return json_value
    elif value_type == 'int':
        try:
            json_value = dict(((lambda i: (i[0], int(i[1])))(l.split('=')) for l in data.split('&')))
            if json_value:
                log.debug('转换int类型value dict成功：\n%s' % json_value)
                return json_value
        except Exception as e:
            log.error('转换int类型value dict报错：\n%s' % e)
    else:
        log.error("转换值类型输入有误，请输入'str'或'int'.")

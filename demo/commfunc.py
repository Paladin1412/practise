#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Date    : 2017/3/14 13:07
# @Version : python 3.4
# @Author  : KingDow
import os
import re
import time
import hashlib


def get_app_sign(uid, timestamp):
    key = "7srzT88FcNiRQA3n"
    if not uid:
        uid = "0"
    sign = to_md5(uid + timestamp + key)
    return sign


def to_md5(mystr):
    """
        指定字符串MD5加密
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


def cas_login(self):
    self.http.set_header(self.header)
    print("========以下进行CAS用户登录操作========")
    first_url = '/AMS/security/security!index.action'
    redirect_res = self.http.http_get(first_url).decode('utf-8')
    redirect_url = re.findall(r'service=http%3A%2F%2F(.*?)%3A80%2FAMS', redirect_res, re.S | re.M)

    print("========业务系统重定向跳转CAS========")
    res = self.http.http_get('/CAS/login?service=http://%s:80%s' % (
        redirect_url[0], first_url), host='cas.ziroom.com')
    lt = re.findall(r'name="lt" value="(.*?)" />', res.decode('utf-8'), re.S | re.M)
    execution = re.findall(r'name="execution" value="(.*?)" />', res.decode('utf-8'), re.S | re.M)
    event = re.findall(r'name="_eventId" value="(.*?)" />', res.decode('utf-8'), re.S | re.M)

    print("========CAS校验用户名密码ticket========")
    url = '/CAS/login?service=http:///%s:80%s' % (redirect_url[0], first_url)
    data = 'username=%s&password=%s&lt=%s&execution=%s&_eventId=%s' % (
        self.http.user_info.get('username'), self.http.user_info.get('password'), lt[0], execution[0], event[0])
    cas_res = self.http.post(url, host='cas.ziroom.com', data=data)
    return cas_res

#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Date    : 2017/3/14 13:07
# @Version : python 3.4
# @Author  : KingDow
import hashlib
import json
import os
import time
import urllib.parse
from common.logConfig import GetLog
from xml.etree import ElementTree as et

log = GetLog().log()


def get_app_sign(uid, timestamp):
    """
    获取app登陆验证sign值
    :param uid:
    :param timestamp:
    :return:
    """
    secret = "7srzT88FcNiRQA3n"
    if not uid:
        uid = "0"
    sign = to_md5(uid + timestamp + secret)
    return sign


def get_crm_sign(dict_data):
    """
    生成crm系统所需sign值
    :param dict_data:{'key1': 'value1', 'key2': 'value2'}
    :return:
    """
    secret = '7srzT88FcNiRQA3n'
    sort_dict_data = sorted(dict_data.items())  # 对字典表按照key：value进行自然排序
    my_str = urllib.parse.urlencode(sort_dict_data)
    data = my_str.replace('&', '') + secret
    sign = to_md5(data)
    return sign


def merge_dict(dict1, dict2):
    """
    合并两个字典
    :param dict1: {'key1': 'value1'}
    :param dict2: {'key2': 'value2'}
    :return: {'key1': 'value1', 'key2': 'value2'}
    """
    dict_merge = dict(dict1, **dict2)
    return dict_merge


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
    """
    判断是否正确路径
    :param path:
    :return:
    """
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


def data_format(mystr, to_format=0):
    """
    将fiddler抓包SyntaxView中参数转换dict
    :param to_format: 待转换格式，0表示string，1表示dict，默认0
    :param mystr:sign=123&appType=1&source=1&
    :return:{'appType': '1', 'source': '1', 'sign': '123'}
    """
    try:
        mydict = dict([s.split('=') for s in mystr.split('&') if s])
        json_str = json.dumps(mydict, indent=4, ensure_ascii=False)
        if int(to_format) == 0:
            return json_str
        elif int(to_format) == 1:
            return mydict
        else:
            print('待转换格式输入有误，请输入0 / 1，分别标识string / dict')
    except ValueError:
        print('data_format Error!')


def title_format(mystr):
    """
    将fiddler抓包接口驼峰命名转换python小写下划线格式
    :param mystr:
    :return:
    """
    newstr = "".join(["_" + ch if ch.isupper() else ch for ch in mystr])
    return newstr.lower()


def get_xml(xml_path):
    """
    解析xml文件
    :param xml_path:readConfig.confsPath.get('xmlPath')
    :return:
    """
    tree = et.parse(xml_path)
    root = tree.getroot()
    interface_info = []
    i_base = {
        "title": root.find("title").text,
        "host": root.find("host").text,
        "port": root.find("port").text,
        "No": root.find("No").text
    }
    interface_info.append(i_base)
    for elem in root.findall("InterfaceList"):
        i_app = {
            "param": [],
            "id": elem.find('id').text,
            "name": elem.find('name').text,
            "method": elem.find('method').text,
            "url": elem.find('url').text,
            "hope": elem.find('hope').text,
            "login": elem.find('login').text,
            "isList": elem.find('isList').text
        }
        for p in elem.findall("params"):
            param = {
                "name": p.find("name").text,
                "type": p.find("name").attrib.get("type"),
                "value": p.find("value").text,
                "must": p.find("must").text
            }
            i_app["param"].append(param)
        interface_info.append(i_app)
    return interface_info

#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Date    : 2017/7/9 14:53
# @Version : python 3.4
# @Author  : KingDow
import ast
import time
import unittest

from common import globalParams
from common import readConfig
from common.commFunc import get_xml

xpath = readConfig.confsPath.get('xmlPath')
api_info = get_xml(xpath)  # 读取api_xml
case_no_list = api_info[0].get('No')  # 读取http参数


class TestInterfaceCase(unittest.TestCase):
    """测试用例(组)类"""

    def __init__(self, test_name, index):
        super(TestInterfaceCase, self).__init__(test_name)
        self.index = index

    def setUp(self):
        """全局变量初始化"""
        globalParams.global_init()


def get_test_suite(index):
    """获取测试套件"""
    func_name = api_info[index].get('url')
    test_suite = unittest.TestSuite()
    test_suite.addTest(TestInterfaceCase(func_name, index))
    return test_suite


# 运行测试用例函数
def run_case(runner):
    case_list = ast.literal_eval(case_no_list)  # 把字符串类型的list转换为list
    if not len(case_list):  # 判断是否执行指定的用例ID
        temp_case = api_info
        for index in range(1, len(temp_case)):
            test_suite = get_test_suite(index)
            runner.run(test_suite)

    else:
        print(case_list)
        print(api_info)
        for i in case_list:
            for j in range(1, len(api_info)):
                if str(i) == api_info[j].get('id'):
                    test_suite = get_test_suite(j)
                    runner.run(test_suite)


# 运行测试套件
if __name__ == '__main__':
    start_time = time.time()
    # suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestInterfaceCase)
    # unittest.TextTestRunner().run(suite)

    runner = unittest.TextTestRunner()
    run_case(runner)
    end_time = time.time()
    sum_time = "%.2f" % (end_time - start_time)

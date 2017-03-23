#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Date    : 2017/3/23 19:56
# @Version : python 3.4
# @Author  : KingDow


class DemoTest:
    def setUp(self):
        print('function setup')

    def tearDown(self):
        print('function teardown')

    def testfunc1(self):
        print("this is Testfunc1")
        assert 2 == 2

    def test_func1(self):
        print("this is test_func1")
        assert 1 == 1

    def Testfunc2(self):
        print("this is Testfunc2")
        pass

    def test_func2(self):
        print("this is test_func2")
        pass

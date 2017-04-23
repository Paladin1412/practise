#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Date    : 2017/3/14 13:08
# @Version : python 3.4
# @Author  : KingDow

import os
import time
from pyh import *


class HtmlReport(object):
    def __init__(self):
        self.title = 'test_report_page'  # 网页标签名称
        self.filename = ''  # 结果文件名
        self.time_took = '00:00:00'  # 测试耗时
        self.tm = time.strftime('%Y%m%d%H%M%S', time.localtime())
        self.result1 = result1
        self.result2 = result2

    # 生成HTML报告
    def generate_html(self, head, file):
        page = PyH(self.title)
        page << h1(head, align='center')  # 标题居中

        page << div('基本信息', align='left')
        page << p('测试日期：' + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) + '&nbsp' * 18 +
                  '测试总耗时：' + self.time_took)
        print("\n正在玩命生成测试报告中，请稍候...")
        #  表格标题caption 表格边框border 单元边沿与其内容之间的空白cellpadding 单元格之间间隔为cellspacing
        page << p('', align='left')
        page << div('费用结算明细', align='left')
        tab = table(border='5', cellpadding='10', cellspacing='2', cl='table')
        tab1 = page << tab
        tab1 << tr(td('费用项', bgcolor='#ABABAB', align='center', width='170') +
                   td('实际合计', bgcolor='#ABABAB', align='center', width='170'))

        # 查询所有测试结果并记录到html文档
        my_result = ['a', 'b', 'c']
        for i in my_result:
            tab1 << tr(td('%s' % i[0]) + td('%s' % i[1]) + td('%s' % i[2]))

        page << p('', align='left')
        page << div('通用收款单费用结算', align='left')
        tab2 = table(border='5', cellpadding='10', cellspacing='2', cl='table')
        tab3 = page << tab2
        tab3 << tr(td('费用项', bgcolor='#ABABAB', align='center', width='235') +
                   td('实际合计', bgcolor='#ABABAB', align='center', width='235'))
        universal_result = ['a', 'b', 'c']
        for x in universal_result:
            tab3 << tr(td(td('%s' % x[0]) + td('%s' % x[1]) + td('%s' % x[2])))
        print("测试报告已经生成，请君审阅...")
        self._set_result_filename(file)
        page.printOut(self.filename)

    # 设置结果文件名
    def _set_result_filename(self, filename):
        self.filename = filename
        if os.path.isdir(self.filename):
            raise IOError("%s must point to a file" % os.path)
        elif '' == self.filename:
            raise IOError('filename can not be empty')
        else:
            parent_path, ext = os.path.splitext(filename)
            tm = time.strftime('%Y%m%d%H%M%S', time.localtime())
            self.filename = parent_path + tm + ext

    # 统计运行耗时
    def time_tooks(self, time_finish):
        self.time_took = time_finish
        return self.time_took

#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 12/17/2020 17:35 
# @Author : Julia
# @Version：V 0.1
# @File : excelTest.py
# @desc :

import xlrd
import os
from xlutils.copy import copy


def base_dir(filename=None):
    return os.path.join(os.path.dirname(__file__),filename)

'''excel操作'''
work = xlrd.open_workbook(base_dir("data.xlsx"))
sheet = work.sheet_by_index(0)
# print(sheet.nrows)
print(sheet.cell_value(9,3))

'''excel修改'''
# work = xlrd.open_workbook(base_dir('data.xlsx'))
# print(work)
# old_content=copy(work)
# ws = old_content.get_sheet(0)
# ws.write(9,3,'修改内容')
# old_content.save(base_dir('data.xlsx'))

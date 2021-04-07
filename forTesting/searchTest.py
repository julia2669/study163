#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 1/26/2021 17:48 
# @Author : Julia
# @Version：V 0.1
# @File : searchTest.py
# @desc :

import os
testfiles = []
testfilepaths = []
L = len(os.path.abspath('.'))
def searchfile(path):
    try:
        for item in os.listdir(path):
            # print(len(item))
            if os.path.isdir(os.path.join(path, item)):
                searchfile(os.path.join(path, item))
            else:
                if item.endswith('.docx') and '简历' in item:
                    print(item, path[L:])
                    # print('目录：', os.path.dirname(item))
    except Exception as e:
        pass



searchfile(os.path.abspath('C:\\'))
print('***'*10)
#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 12/2/2020 16:56 
# @Author : Julia
# @Version：V 0.1
# @File : operation_json.py
# @desc :

import json
import pprint
import os

def readJson():
    # return json.load(open('aa.json','r',encoding='utf-8'))
    jsonfile = os.path.join(os.path.dirname(__file__),'login.json')

    print(jsonfile)
    return json.load(open(jsonfile,'r',encoding='utf-8-sig'))['item']
    # with open('login2.json') as f:
    #     line = f.readline()
    #     if line.startswith(u'\0x90'):
    #         content = line.encode('utf-8-sig')[3:].decode('utf8')
    #         print(line)
    #         print(content)

#
#
# items = readJson()
# print(type(items))
# for item in items:
#     print(item)
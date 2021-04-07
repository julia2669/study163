#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 11/12/2020 18:51
# @Author : Julia
# @Version：V 0.1
# @File : md5_test.py
# @desc :

from urllib import parse
import hashlib

"""
1. 对请求参数做ASCII码排序
2. 做URL encode编码：age=18&city=xian&name=julia&work=tester
3. 做md5-sign
"""

dict1 = {'name': 'julia', 'age': 18, 'city': 'xian', 'work': 'tester'}


# datas = {'name': 'julia', 'age': 18, 'city': 'xian', 'work': 'tester', 'sign': sign}

# dict1 = dict(sorted(dict1.items(), key=lambda item: item[0]))
#
# datas = parse.urlencode(dict1)
#
# md5 = hashlib.md5()
# md5.update(datas.encode('utf-8'))
# print(md5.digest())
# print(md5.hexdigest())

def getMd5(**kwargs):
    dict1 = dict(sorted(kwargs.items(), key=lambda item: item[0]))
    datas = parse.urlencode(dict1)
    md5 = hashlib.md5()
    md5.update(datas.encode('utf-8'))
    return md5.hexdigest()


print(getMd5(name='julia', age=18))

#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 11/11/2020 18:23 
# @Author : Julia
# @Version：V 0.1
# @File : sysTest.py
# @desc :


import sys
import os
''' 
1.变量
2.常用的方法
3.sys常见问题
'''

# print(sys.argv)
# print(dir(sys))
# print(sys.version)
# print(sys.platform)

# '''
# 1.标准库: C:\Users\julizhou\AppData\Local\Continuum\anaconda3\envs\py37\lib
# 2.第三方库: C:\Users\julizhou\AppData\Local\Continuum\anaconda3\envs\py37\lib\site-packages
# 3.自定义的库： 部署之后找不到  sys.path.append()
# '''

for item in sys.path:
    print(item)
print()
day3_path = os.path.join(os.path.dirname(os.path.dirname(__file__)),'Day3')
sys.path.append(day3_path)
for item in sys.path:
    print(item)
#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 11/11/2020 17:05 
# @Author : Julia
# @Version：V 0.1
# @File : timeTest.py
# @desc :


import time as t

# 获取时间戳
print(int(t.time()))

# 获取当前时间
print(t.localtime())
print(t.localtime(t.time()))
print(t.strftime('%Y-%m-%d %H:%M:%S',t.localtime()))
nowTime = t.strftime('%Y-%m-%d %H:%M:%S',t.localtime())
t.sleep(2)
print(nowTime)
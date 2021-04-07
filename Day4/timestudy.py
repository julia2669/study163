#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 11/3/2020 16:31 
# @Author : Julia
# @Version：V 0.1
# @File : timestudy.py
# @desc :

import time as t

#休眠， 休眠1秒打印
t.sleep(1)
print('你好')

#从1970年开始的时间戳
print(t.time())


print(t.ctime())

print(t.ctime(t.time()))

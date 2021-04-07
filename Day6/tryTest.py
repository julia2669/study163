#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 11/17/2020 10:58 
# @Author : Julia
# @Version：V 0.1
# @File : tryTest.py
# @desc :


"""
1.try代码执行正常，不会执行except的代码
2.try代码执行异常，就会执行except的代码
"""

def div(a,b):
    return a/b

try:
    div(1,0)
except Exception as e:
    print(e.args)
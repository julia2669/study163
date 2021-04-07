#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 11/18/2020 17:22 
# @Author : Julia
# @Version：V 0.1
# @File : f4.py
# @desc :

"""
普通方法
特性方法
"""


class Person(object):
    def conn(self, user, password, host, port):
        pass

    def f1(self,*args,**kwargs):
        pass

    def info(self):
        print('我是普通方法')


per = Person()
per.conn('julia','pass','localhost',9999)
per.f1()
per.info()

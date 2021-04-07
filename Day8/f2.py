#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 11/18/2020 16:51 
# @Author : Julia
# @Version：V 0.1
# @File : f2.py
# @desc :

"""
一个类不管是否写了构造函数，它都是有构造函数的
一个类可以有多个构造函数,建议一个类只写一个构造函数
构造函数
1.初始化属性
2.
"""


class Person2(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __init__(self, address):
        self.address = address

    def info(self):
        print('信息：', self.name, self.age, self.address)


per1 = Person2('xian')

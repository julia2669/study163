#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 11/20/2020 13:37 
# @Author : Julia
# @Version：V 0.1
# @File : f8.py
# @desc :

"""
子类有自己的属性才需要写构造方法
"""


class Person(object):

    def __init__(self, name):
        self.name = name

    def info(self):
        print('父类', self.name)


class Son(Person):
    def __init__(self, name, address, age):
        super().__init__(name)
        self.age = age
        self.address = address

    def info(self):
        print(self.name, self.address, self.age)


s = Son('hua', 'zhejiang', 18)
s.info()

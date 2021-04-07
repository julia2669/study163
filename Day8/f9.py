#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 11/20/2020 14:15 
# @Author : Julia
# @Version：V 0.1
# @File : f9.py
# @desc :
"""
多个类的继承，从左到右的原则
多类继承多个父类必须在同一个级别
"""


class Person(object):
    def BloodType(self):
        print('人类')


class Mother(Person):
    def BloodType(self):
        print('母亲血型')


class Father(Person):
    def BloodType(self):
        print('父亲血型')


class Son(Mother,Father):
    pass


s = Son()
s.BloodType()
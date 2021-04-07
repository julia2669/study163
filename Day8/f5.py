#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 11/18/2020 17:34 
# @Author : Julia
# @Version：V 0.1
# @File : f5.py
# @desc :

'''
特性方法：这个方法不能有形式参数,调用不用加()
'''


# class Person(object):
#     @property
#     def getUserID(self):
#         pass
#
# per = Person()
# per.getUserID

'''
静态方法:直接使用类名来调用,它属于类
对象也可以调用静态方法，但是不建议这么做
'''

# class MySQL(object):
#     @staticmethod
#     def conn(user):
#         pass
#
# MySQL.conn('julia')


'''
类方法：直接使用类来调用，属于类
浏览器只打开一次
'''

# class Person(object):
#     @classmethod
#     def conn(cls):
#         pass


'''
属于类：
    类属性
    静态方法 @staticmethod
    类方法 @classmethod
属于对象：
    实例属性
    普通方法
    特性方法 @property
'''
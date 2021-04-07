#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 11/23/2020 15:01 
# @Author : Julia
# @Version：V 0.1
# @File : factoryTest.py
# @desc :

"""
__doc__: 打印出类的注释
"""


class Person(object):
    '''
    对人类的定义
    '''

    def info(self,username,password):
        '''
        获取用户信息
        :param username: 用户名
        :param password: 密码
        :return:
        '''

        pass
'''__call__:对象创建时直接返回__call__的内容，使用该方法可以模拟静态方法'''
class P1(object):
    def __new__(cls, *args,  **kwargs):
        print('call 方法')

per=P1()
per

str1 = 'admin'
print(dir(str1))

'''__str__:对象代表的含义，返回一个字符串，通过它可以把对象和字符串关联起来，方便某些程序的实现，
该字符串表示某个类，实现了__str__后，可以直接使用print语句输出对象，也可以通过函数str来触发__str__的执行

1.对象的意思
2.返回一个字符串，字符串和对象关联起来，改字符串表示某个类
'''

class Son(object):
    '''我是一类'''
    def __str__(self):
        return self.__doc__

s = Son()
print(s)


class Factory(object):
    def createFruit(self,fruit):
        if fruit == 'apple':
            return Apple()
        if fruit == 'banana':
            return Banana()

class Fruit(object):
    def __str__(self):
        return 'fruit'

class Apple(Fruit):
    def __str__(self):
        return 'apple'

class Banana(Fruit):
    def __str__(self):
        return 'banana'

if __name__=='__main__':
    factory = Factory()
    print(factory.createFruit('apple'))
    print(factory.createFruit('banana'))

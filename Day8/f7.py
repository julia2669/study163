#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 11/20/2020 13:18 
# @Author : Julia
# @Version：V 0.1
# @File : f7.py
# @desc :

"""
方法的继承
之类为什么重写父类的方法：子类有自己的特性
当子类重写了父类的方法后，对子类进行实例化后，子类调用的方法（父类，子类都存在），执行子类的方法

单类的继承原则：
1.从上到下：子类继承了父类，但是子类没有重写父类的方法，那么子类实例化后，调用的方法是直接调用父类当中的方法
2.从下到上：子类继承了父类，但是子类有重写父类的方法，那么子类实例化后，调用的方法是子类当中的方法（子类优先考虑自己的方法）
"""


class Fruit(object):
    def eat(self):
        print('水果是可以吃的')


class Apple(Fruit):
    def __init__(self, color):
        self.color = color

    def eat(self):
        print('苹果红了可以吃{}'.format(self.color))


class UsaApple(Apple):
    def eat(self):
        print('我是usa的方法')



apple = UsaApple('红色')
apple.eat()
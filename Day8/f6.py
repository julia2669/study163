#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 11/18/2020 17:53 
# @Author : Julia
# @Version：V 0.1
# @File : f6.py
# @desc :


'''继承'''
'''类属性的继承'''
# class Person(object):
#     ad = '地球'
#
# class UsaPerson(Person):
#     pass
#
# per=UsaPerson()
# print(per.ad)

'''实例属性的继承和继承的写法'''
'''子类需要继承父类的实例属性'''


class Fruit(object):
    def __init__(self, name):
        self.name = name


class Apple(Fruit):
    def __init__(self, name, brand, color):
        super().__init__(name)
        # super(Apple,self).__init__(name)  #super() 函数是用于调用父类(超类)的一个方法。 python2的写法
        # Fruit.__init__(self,name)
        self.color = color
        self.brand = brand

    def info(self):
        print('名称: {0}，品牌: {1}，颜色: {2}'.format(self.name, self.brand, self.color))


apple = Apple('苹果', '红富士', 'red')
apple.info()

'''子类不需要继承父类的属性'''
# class Fruit(object):
#     def __init__(self,name):
#         self.name = name
#
# class Apple(Fruit):
#     def __init__(self,name,brand,color):
#         self.color = color
#         self.brand = brand
#
#     def info(self):
#         print('品牌: {0}，颜色: {1}'.format(self.brand,self.color))
#
# apple = Apple('苹果','红富士','red')
# apple.info()

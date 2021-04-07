#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 11/17/2020 19:47 
# @Author : Julia
# @Version：V 0.1
# @File : Test_1.py
# @desc :

'''类：类是有一系列属性和方法组成'''


class F1(object):
    pass


'''
对象的创建---》就是类的实例化
三个特性：
1.对象的句柄---》区分不同的对象
2.属性 
    共有属性
        类属性
        实例属性
        局部变量
    私有属性
3.方法
'''


class Person(object):
    guojia = 'china'
    def __init__(self, name, age):
        # 实例属性
        self.name = name
        self.age = age

    def getName(self):
        return self.name

    def getAge(self):
        return self.age

    def setName(self, name):
        self.name = name

    def setAge(self, age):
        self.age = age

    def info(self):
        return 'name:{0}, age:{1}, 来自：{2}'.format(self.getName(),self.getAge(),self.guojia)


per = Person('wuya', '18')
per2 = Person('julia', '10')
per.setName('dingding')
print(per2.info(),per.info())


# class Person2(object):
#     def __init__(self, *args, **kwargs):
#         self.args = args
#         self.kwargs = kwargs
#
#     def info(self):
#         print('信息：', self.args)
#
#
# per1 = Person2('lis')
# per1.info()

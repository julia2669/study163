#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 11/18/2020 17:11 
# @Author : Julia
# @Version：V 0.1
# @File : f3.py
# @desc :

"""
析构函数
析构函数(destructor) 与构造函数相反，当对象结束其生命周期，
如对象所在的函数已调用完毕时，系统自动执行析构函数。析构函数往往用来做“清理善后” 的工作（例如在建立对象时用new开辟了一片内存空间，
delete会自动调用析构函数后释放内存）。
调用顺序：对象实例化后先执行类构造函数再执行调用方法最后执行析构方法
"""
'''
del xxx 不会主动调用__del__方法，只有引用计数 == 0时，__del__()才会被执行，
并且定义了__del_()的实例无法被Python的循环垃圾收集器收集，所以尽量不要自定义__del__()。
一般情况下，__del__() 不会破坏垃圾处理器。
'''


# class Person(object):
#     def __init__(self):
#         print('我是构造函数')
#
#     def __del__(self):
#         print('我是析构函数')
#
#     def info(self):
#         print('我是方法')
#
#
# per = Person()
# per.info()


# class Person(object):
#     def __init__(self,name):
#         print('我是构造函数')
#         self.name = name
#     def __del__(self):
#         # print("实例对象:%s"%self.name,id(self))
#         print("python解释器开始回收%s对象了" % self.name)
#
# print("类对象",id(Person))
# zhangsan  = Person("张三")
# print("实例对象张三:",id(zhangsan))
# print("------------")
# lisi  = Person("李四")
# print('---')
# print("实例对象李四:",id(lisi))
# print("实例对象张三:",id(zhangsan))



import time
class Animal(object):

    # 初始化方法
    # 创建完对象后会自动被调用
    def __init__(self, name):
        print('__init__方法被调用')
        self.__name = name
    # 析构方法
    # 当对象被删除时，会自动被调用
    def __del__(self):
        print("__del__方法被调用")
        print("%s对象马上被干掉了..."%self.__name)
# 创建对象
dog = Animal("哈皮狗")
# 删除对象
del dog
cat = Animal("波斯猫")
cat2 = cat
cat3 = cat
print(id(cat),id(cat2),id(cat3),)

print("---马上 删除cat对象")
del cat
print("---马上 删除cat2对象")
del cat2
print("---马上 删除cat3对象")
del cat3

print("程序2秒钟后结束")
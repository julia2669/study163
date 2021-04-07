#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 11/27/2020 17:16 
# @Author : Julia
# @Version：V 0.1
# @File : Test_1.py
# @desc :


'''所有的单测文件名都需要满足test_*.py格式或*_test.py格式。
在单测文件中，测试类以Test开头，并且不能带有 init 方法(注意：定义class时，需要以T开头，不然pytest是不会去运行该class的)
在单测类中，可以包含一个或多个test_开头的函数。
此时，在执行pytest命令时，会自动从当前目录及子目录中寻找符合上述约束的测试函数来执行。

-v 打印详细信息
-s 打印调试信息（print）
pytest --collect-only 收集pytest 会执行的文件方法类方法
-k 指定希望用到的测试用例 如smoketest的用例
-m 分组

and
or
not

-x
--maxfailnum

--duration

'''
import unittest

def test_001():
    assert 1

def testadd():
    assert 1

class TestClass(object):
    def test_002(self):
        assert 1


def add( a, b):
        return a+b


def test_add_integer():
        assert add(1,2)==3

def test_add_integer_str():
        assert add(1,'1')==2


def test_add_str():
        assert add('sss','1')=='sss1'



#
# def addr(x):
#     def wrapper(y):
#         return x+y
#     return wrapper
#
# addr5=addr(5)
# print(addr5(addr5(6)))
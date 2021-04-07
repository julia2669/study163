#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 11/24/2020 15:11 
# @Author : Julia
# @Version：V 0.1
# @File : uTest.py
# @desc :

import unittest


class F1(unittest.TestCase):
    def setUp(self):    ###每个test都会跑这个setup 如果要只执行一次需要用class method
        print('准备工作')


    def tearDown(self):
        print('收尾完成')


    def test_001(self):
        print('test001')


    def test_002(self):
        print('test002')


    def test_003(self):
        print('test003')


class F2(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('class方法 准备 只准备一次')

    @classmethod
    def tearDownClass(cls):
        print('class方法，收尾完成，只收一次')


    def test_001(self): ##执行顺序test_001的ASCII码顺序
        print('test001')


    def test_002(self):
        print('test002')


    def test_003(self):
        print('test003')

if __name__ == '__main__':
    unittest.main()

#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 11/25/2020 16:29 
# @Author : Julia
# @Version：V 0.1
# @File : f2.py
# @desc :


#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 11/24/2020 16:11
# @Author : Julia
# @Version：V 0.1
# @File : Test_1.py
# @desc :

import unittest
from selenium import webdriver

class F2(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @unittest.skip('忽略测试')
    def test_001(self):
        '''测试001'''
        pass


    def test_002(self):
        '''测试002'''
        pass

    @unittest.expectedFailure
    def test_003(self):
        '''测试003'''
        pass



if __name__ == '__main__':
    unittest.main(verbosity=2)



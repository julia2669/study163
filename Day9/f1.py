#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 11/24/2020 16:11 
# @Author : Julia
# @Version：V 0.1
# @File : Test_1.py
# @desc :

import unittest
from selenium import webdriver

class F1(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(15)
        cls.driver.get('http://www.baidu.com')

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


    def test_001(self):
        '''测试新闻链接'''
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_link_text('新闻').click()
        self.driver.switch_to.window(self.driver.window_handles[0])

    def test_002(self):
        '''测试错误case'''
        self.driver.find_element_by_partial_link_text('123').click()
        self.driver.switch_to.window(self.driver.window_handles[0])

    def test_003(self):
        '''测试地图链接'''
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_link_text('地图').click()
        self.driver.switch_to.window(self.driver.window_handles[0])

if __name__ == '__main__':
    suite = unittest.TestSuite(unittest.makeSuite(F1))
    unittest.TextTestRunner(verbosity=2).run(suite)



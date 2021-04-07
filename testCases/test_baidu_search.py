#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 11/26/2020 11:29 
# @Author : Julia
# @Version：V 0.1
# @File : test_baidu_search.py
# @desc :

from selenium import webdriver
import unittest

class baiDuSearch(unittest.TestCase):
    def setUp(self) -> None:
        option = webdriver.ChromeOptions()
        option.headless = True
        self.driver = webdriver.Chrome(options=option)
        self.driver.implicitly_wait(30)
        self.driver.get('https://www.baidu.com')


    def tearDown(self) -> None:
        self.driver.quit()

    def test_baidu_search_enable(self):
        '''首页：百度搜索输入框可编辑'''
        so = self.driver.find_element_by_id('kw')
        self.assertTrue(so.is_enabled())

    def test_baidu_search_func(self):
        '''首页：测试百度搜索功能'''
        so = self.driver.find_element_by_id('kw')
        so.send_keys('webdriver')
        self.driver.find_element_by_class_name('s_ipt').click()
        print(so.get_attribute('value'))
        self.assertEqual(so.get_attribute('value'),'webdriver')


if __name__ == '__main__':
    unittest.main(verbosity=2)


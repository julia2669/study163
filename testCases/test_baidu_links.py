#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 11/26/2020 11:29 
# @Author : Julia
# @Version：V 0.1
# @File : test_baidu_links.py
# @desc :

from selenium import webdriver
import unittest
import allure

@allure.feature('测试百度链接')
class baiDuLink(unittest.TestCase):
    def setUp(self) -> None:
        option = webdriver.ChromeOptions()
        option.headless = True
        self.driver = webdriver.Chrome(options=option)
        self.driver.implicitly_wait(30)
        self.driver.get('https://www.baidu.com')


    def tearDown(self) -> None:
        self.driver.quit()


    @allure.story('测试新闻链接')
    def test_baidu_news(self):
        '''首页：点击新闻是否正常的跳转'''
        self.driver.implicitly_wait(15)
        self.driver.find_element_by_link_text('新闻').click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.assertEqual(self.driver.current_url, 'http://news.baidu.com/')



    @allure.story('测试地图链接')
    def test_baidu_map(self):
        '''首页：点击地图是否正常的跳转'''
        self.driver.implicitly_wait(15)
        self.driver.find_element_by_link_text('地图').click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        # print(self.driver.current_url, type(self.driver.current_url))
        self.assertTrue(self.driver.current_url.startswith('https://map.baidu.com/'))

if __name__ == '__main__':
    unittest.main(verbosity=2)


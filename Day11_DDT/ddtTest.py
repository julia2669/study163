#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 1/26/2021 10:38 
# @Author : Julia
# @Version：V 0.1
# @File : ddtTest.py
# @desc :
import requests
import ddt
import csv
import unittest
import json

url = 'https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false'


def getHeaders():
    cookies = '''
    '''
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36",
        "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
        "referer": "https://www.lagou.com/jobs/list_^%^E8^%^87^%^AA^%^E5^%^8A^%^A8^%^E5^%^8C^%^96^%^E6^%^B5^%^8B^%^E8^%^AF^%^95?labelWords=^&fromSearch=true^&suginput=",
        "cookie": cookies    }
    return headers

# list1 = [i for i in range(1,3)]
list1 = [1,2,3]

@ddt.ddt
class Lagou(unittest.TestCase):

    @ddt.data((1,),(2,))
    @ddt.unpack
    def test_laGou(self,page=2):
        body = {'first': True, 'pn': page, 'kd': '自动化测试'}
        print(body)
        r = requests.post(
            url=url,
            headers=getHeaders(),
            data = json.dumps(body)
        )
        print(r.text)
        # print(r.json()['content']['positionResult']['result'][0]['city'])
        # self.assertEqual(r.json()['success'],True)


if __name__ == '__main__':
    unittest.main(verbosity=2)

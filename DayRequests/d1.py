#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 12/9/2020 11:04 
# @Author : Julia
# @Version：V 0.1
# @File : d1.py
# @desc :

import requests
from requests.auth import HTTPBasicAuth

# r = requests.get(url='http://localhost:8888/api/v1.0/books_uri',auth=HTTPBasicAuth('julia','pass'))
# print(r.text)

r = requests.get(url='http://localhost:8888/api/v1.0/books/1',auth=HTTPBasicAuth('julia','pass'))
print(r.text)
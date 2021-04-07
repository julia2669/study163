#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 12/2/2020 17:21 
# @Author : Julia
# @Version：V 0.1
# @File : test_json_login.py
# @desc :

import json
import requests
from Day10.operation_json import *
import pytest

@pytest.mark.parametrize('data',readJson())
def test_json_login(data):
    print(data['request']['body'])
    r = requests.post(url=data['request']['url'],
                      json=data['request']['body'],
                      headers=data['request']['headers']
                      )
    assert r.json()==data['response']


if __name__ == '__main__':
    pytest.main(["-s","-v","test_json_login.py"])

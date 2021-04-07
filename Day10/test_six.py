#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 12/1/2020 15:24 
# @Author : Julia
# @Version：V 0.1
# @File : test_six.py
# @desc :
import pytest


@pytest.mark.xfail(reason='mark fail test case')
def test_001():
    assert 1 == '1'


# test_001()
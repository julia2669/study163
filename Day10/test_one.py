#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 12/2/2020 16:30 
# @Author : Julia
# @Version：V 0.1
# @File : test_one.py
# @desc :

import pytest

def add(a,b):
    return a+b

'''
是对列表总的对象循环，然后一一的赋值
对象：
列表
元祖
字典
'''
@pytest.mark.parametrize('a,b,expect',[
    [1,1,2],
    [2,2,4],
    [3,3,6],
    [4,4,8],
    [5,5,10]
])
def test_add(a, b, expect):
    assert add(a,b) == expect


@pytest.mark.parametrize('a,b,expect',[
    (1,2,3),
    (2,3,5),
    (3,4,7),
    (4,5,9),
    (5,6,11)
])
def test_add_tuple(a, b, expect):
    assert add(a,b) == expect

@pytest.mark.parametrize('data', [
    {'a':1,'b':2,'expect':3},
    {'a':3,'b':2,'expect':5}
]
)
def test_add_dic(data):
    assert add(data['a'],data['b']) == data['expect']
#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 3/17/2021 15:24 
# @Author : Julia
# @Version：V 0.1
# @File : test1.py
# @desc :

def gen_example():
    print('before any yield')
    yield 'first yield'
    print('between yields')
    yield 'second yield'
    print('no yield anymore')

# gen = gen_example()
# gen.__next__()
# gen.__next__()
# gen.__next__()

def generator_example():
    yield 1
    yield 2

for i in generator_example():
    print(i)


#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 1/20/2021 16:17 
# @Author : Julia
# @Version：V 0.1
# @File : test.py
# @desc :

class Testdel():

    def __init__(self):
        with open('testc.py') as f:
            f.read()
            print('open will rase exception')

    def printm(self):
        print('-------')

    def __del__(self):
        print('del method')


a=Testdel()
print('----------')
b=Testdel()
# a.printm()
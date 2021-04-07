#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 11/11/2020 17:18 
# @Author : Julia
# @Version：V 0.1
# @File : osTest.py
# @desc :

import os

# print(os.system('ipconfig'))

# import os
# os.name #windows是nt，linux是posix
# os.uname() #linux支持显示
# os_info = os.name
# print(os_info)

# os.mkdir('c:/log')
# os.rmdir('c:/log')

# print('当前文件的目录：', os.path.dirname(__file__))
# print('当前文件的上一级目录：', os.path.dirname(os.path.dirname(__file__)))
# print('当前文件的上上一级目录：', os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

# base_dir = os.path.dirname(os.path.dirname(__file__))
# f = open(os.path.join(base_dir,'Day3/login.py'),'r')
# print(f.read())

'''请求参数是不确定的，可能有一个，可能有多个'''


def f1(*args, **kwargs):  # *代表要把传入的参数转为一个元组，而**代表要把传入额参数转为一个字典
    print("f1")
    return kwargs


def f2(*args, **kwargs):  # *代表要把传入的参数转为一个元组，而**代表要把传入额参数转为一个字典
    print("f2")
    return args


t1 = f1(name='julia', age='18')
t2 = f2(1, 2, 3, 4, 5, 6)
print(t1, t2)

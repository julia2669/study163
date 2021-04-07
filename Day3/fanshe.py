#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 11/2/2020 19:54 
# @Author : Julia
# @Version：V 0.1
# @File : fanshe.py
# @desc :反射

url=input('请输入路由地址:\n')
target_models,target_function=url.split('/')
m=__import__(target_models)
if hasattr(m,target_function):
    target_function=getattr(m,target_function)
    target_function()
else:
    print('Not Found 404 Page')
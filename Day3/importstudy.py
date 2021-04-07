#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 11/2/2020 19:13 
# @Author : Julia
# @Version：V 0.1
# @File : importstudy.py
# @desc :

#
# #通过__import__导入目标模块并且放入一个对象中
#
# f=__import__('login')
# #通过对象找login模块中index的字符串并调用
# f.index()
# f.login()

import Day3.login

# #调用login模块中的logout
# f = getattr(Day3.login,'logout')
# f()

#找到Person中的info并调用它
# obj=Day3.login.Person()
# obj2=Day3.login.Person()
# f=getattr(obj,'info')
# f()
# f=setattr(obj,'exit','This is a test')
# f=hasattr(obj,'exit')
# f2=hasattr(obj2,'exit')
# print(f)
# print(f2)

f=getattr(Day3.login,'Str1')
print(f)
f=delattr(Day3.login,'Str1')
print(f)

#在login模块中设置变量str2
f=setattr(Day3.login,'Str2','hello world')
f2=getattr(Day3.login,'Str2')
print(f2)

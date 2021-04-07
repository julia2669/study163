#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 11/17/2020 16:58 
# @Author : Julia
# @Version：V 0.1
# @File : fileTest.py
# @desc :

"""
open()函数的参数：
1.要操作的文件名称
2.以什么样的方式操作文件：
    r:只读模式
    w:只写模式【不可读，不存在就创建，存在就重写】
    x:只写模式【不可读，不存在就创建，存在就报错】
    a:增加模式【可读，不存在就创建，存在只增加内容】

    “+”表示可以同时读写某个文件，具体为：
    r+:读写
    w+:写读
    x+:写读
    a+:写读
"""

import json

# f=open('file.json','w')
temp={
    "name":"julia",
    "age":26,
    "address":"shanghai"
}
# f.writelines(json.dumps(temp))
# f.close()

json.dump(temp, open('file.json','w'))

'''
read() 读取文件的所有内容
read(7) 只读取文件中某些字符
--->By default the read() method returns the whole text, 
    but you can also specify how many characters you want to return:
    f = open("demofile.txt", "r")
    print(f.read(5)) 
readlines() 按行读取文件的内容，默认读取到文件的第一行
    readlines() 方法用于读取所有行(直到结束符 EOF)并返回列表，该列表可以由 Python 的 for... in ... 结构进行处理。

如果碰到结束符 EOF 则返回空字符串。
readline()--> return one line,
By calling readline() two times, you can read the two first lines:

'''
# f=open('file.json','r')
# print(f.read())
# print(f.readline())

'''文件的上下文处理'''
with open('file2','w') as f:
    f.write('julia')
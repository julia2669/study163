#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 4/7/2021 17:52 
# @Author : Julia
# @Version：V 0.1
# @File : nameScript.py
# @desc :

def myFunction():
    print('变量 __name__ 的值是 ' + __name__)
def main():
    myFunction()
if __name__ == '__main__':
    main()